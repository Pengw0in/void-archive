from textblob import TextBlob
import matplotlib.pyplot as plt

def read_messages_from_file(file_path):
    """Reads messages from the file and returns a list of messages."""
    with open(file_path, 'r', encoding='utf-8') as file:
        messages = file.readlines()
    # Strip any leading/trailing whitespace
    return [msg.strip() for msg in messages if msg.strip()]

def analyze_messages(messages):
    # Metrics
    humor_keywords = ["lol", "haha", "sure", "obviously", "really?", "great idea", "lmao"]
    directive_keywords = ["fix", "try", "solution", "let's", "should", "must"]
    
    # Initialize metrics
    humor_count = 0
    word_count = 0
    directive_count = 0
    sentiments = []

    for msg in messages:
        # Humor detection
        if any(kw in msg.lower() for kw in humor_keywords):
            humor_count += 1
        
        # Word count for conciseness
        word_count += len(msg.split())
        
        # Directive/problem-solving detection
        if any(kw in msg.lower() for kw in directive_keywords):
            directive_count += 1
        
        # Sentiment analysis
        blob = TextBlob(msg)
        sentiments.append(blob.sentiment.polarity)
    
    # Calculate average values
    avg_words = word_count / len(messages) if messages else 0
    avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0

    # Calculate ratios
    humor_ratio = (humor_count / len(messages)) * 100 if messages else 0
    directive_ratio = (directive_count / len(messages)) * 100 if messages else 0

    # Return calculated metrics
    return {
        "Humor Ratio (%)": humor_ratio,
        "Average Words per Message": avg_words,
        "Directive Message Ratio (%)": directive_ratio,
        "Average Sentiment": avg_sentiment
    }

def compare_metrics(metrics1, metrics2, labels):
    """Compares metrics from two sets of data and plots them side by side."""
    metric_names = list(metrics1.keys())
    values1 = list(metrics1.values())
    values2 = list(metrics2.values())

    x = range(len(metric_names))  # Number of metrics
    width = 0.35  # Width of the bars

    plt.figure(figsize=(10, 6))
    plt.bar([i - width/2 for i in x], values1, width=width, label=labels[0], color='blue')
    plt.bar([i + width/2 for i in x], values2, width=width, label=labels[1], color='orange')

    plt.title("Comparison of Message Metrics")
    plt.ylabel("Scores")
    plt.xticks(ticks=x, labels=metric_names, rotation=25, ha='right')  # Adjust rotation and alignment
    plt.legend()
    plt.tight_layout()  # Ensures everything fits in the graph
    plt.show()

# File paths
file1_path = '/Users/lohithsrikar/Documents/TSA/P1/1.txt'
file2_path = '/Users/lohithsrikar/Documents/TSA/P1/2.txt'

# Read messages
messages1 = read_messages_from_file(file1_path)
messages2 = read_messages_from_file(file2_path)

# Analyze metrics
metrics1 = analyze_messages(messages1)
metrics2 = analyze_messages(messages2)

# Print metrics for debugging/comparison
print("Metrics for File 1:")
for key, value in metrics1.items():
    print(f"{key}: {value:.2f}")

print("\nMetrics for File 2:")
for key, value in metrics2.items():
    print(f"{key}: {value:.2f}")

# Compare and visualize metrics
compare_metrics(metrics1, metrics2, labels=["File 1", "File 2"])
