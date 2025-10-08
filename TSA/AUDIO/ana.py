import os
import numpy as np
import pandas as pd
import librosa
import matplotlib.pyplot as plt
import seaborn as sns

class MusicTasteAnalyzer:
    def __init__(self):
        # Initialize lists to store song features
        self.song_names = []
        self.features_df = pd.DataFrame()

    def extract_features(self, file_path):
        """
        Extract comprehensive audio features from a music file
        """
        # Extract filename without extension
        song_name = os.path.splitext(os.path.basename(file_path))[0]
        
        try:
            # Load the audio file
            y, sr = librosa.load(file_path, sr=None)
            
            # Temporal features
            duration = librosa.get_duration(y=y, sr=sr)
            tempo = librosa.feature.rhythm.tempo(y=y, sr=sr).item()  # Updated tempo extraction
            
            # Spectral features
            spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
            spectral_bandwidth = np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr))
            spectral_rolloff = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))
            
            # Harmonic and Percussive features
            harmonic, percussive = librosa.effects.hpss(y)
            harmonic_energy = np.mean(librosa.feature.rms(y=harmonic))
            percussive_energy = np.mean(librosa.feature.rms(y=percussive))
            
            # Spectral contrast
            spectral_contrast = np.mean(librosa.feature.spectral_contrast(y=y, sr=sr))
            
            # Mel-frequency cepstral coefficients (MFCCs)
            mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
            mfcc_mean = np.mean(mfccs, axis=1)
            
            # Create a dictionary of features
            features = {
                'Song': song_name,
                'Duration': duration,
                'Tempo': tempo,  # Ensure Tempo is a scalar
                'Spectral Centroid': spectral_centroid,
                'Spectral Bandwidth': spectral_bandwidth,
                'Spectral Rolloff': spectral_rolloff,
                'Harmonic Energy': harmonic_energy,
                'Percussive Energy': percussive_energy,
                'Spectral Contrast': spectral_contrast
            }
            
            # Add MFCCs to features
            for i, mfcc_val in enumerate(mfcc_mean):
                features[f'MFCC_{i+1}'] = mfcc_val
            
            return features
        
        except Exception as e:
            print(f"Error processing {song_name}: {e}")
            return None


    def analyze_multiple_songs(self, file_paths):
        """
        Analyze multiple songs and create a comprehensive dataframe
        """
        # Reset the dataframe
        self.features_df = pd.DataFrame()
        self.song_names = []
        
        # Extract features for each song
        for file_path in file_paths:
            features = self.extract_features(file_path)
            if features:
                self.features_df = pd.concat([
                    self.features_df, 
                    pd.DataFrame([features])
                ], ignore_index=True)
                self.song_names.append(features['Song'])
        
        return self.features_df

    def visualize_features(self):
        """
        Create visualizations to compare song features
        """
        if self.features_df.empty:
            print("No songs analyzed. Please add songs first.")
            return

        # Set up the visualization
        plt.figure(figsize=(15, 10))
        
        # Radar Chart for Key Features
        features_to_plot = [
            'Tempo', 'Spectral Centroid', 'Spectral Bandwidth', 
            'Harmonic Energy', 'Percussive Energy', 'Spectral Contrast'
        ]
        
        # Normalize the features
        normalized_df = (self.features_df[features_to_plot] - 
                         self.features_df[features_to_plot].min()) / \
                        (self.features_df[features_to_plot].max() - 
                         self.features_df[features_to_plot].min())
        
        # Radar Chart
        angles = np.linspace(0, 2 * np.pi, len(features_to_plot), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))
        
        plt.subplot(121, polar=True)
        for i, song in enumerate(self.song_names):
            values = normalized_df.iloc[i].values.flatten()  # Ensure 1D array
            values = np.concatenate((values, [values[0]]))  # Circular wrap
            plt.polar(angles, values, 'o-', label=song)
        
        plt.title('Comparative Song Features')
        plt.xticks(angles[:-1], features_to_plot)
        plt.legend(loc='lower right', bbox_to_anchor=(1.2, -0.1))

        # Correlation Heatmap for MFCCs
        plt.subplot(122)
        mfcc_columns = [col for col in self.features_df.columns if col.startswith('MFCC_')]
        sns.heatmap(
            self.features_df[mfcc_columns].T, 
            cmap='coolwarm', 
            yticklabels=mfcc_columns, 
            xticklabels=self.song_names
        )
        plt.title('MFCC Comparison')
        plt.xlabel('Songs')
        plt.ylabel('MFCC Coefficients')
        
        plt.tight_layout()
        plt.show()

def main():
    # Create analyzer instance
    analyzer = MusicTasteAnalyzer()
    
    # Get multiple song paths
    print("Enter full paths to your favorite songs (one per line). Press Enter twice to finish:")
    file_paths = []
    while True:
        path = input().strip()
        if path == "":
            break
        file_paths.append(path)
    
    # Analyze songs
    features_df = analyzer.analyze_multiple_songs(file_paths)
    
    # Print features
    print("\nSong Features:")
    print(features_df)
    
    # Visualize features
    analyzer.visualize_features()

if __name__ == "__main__":
    main()
