from gtts import gTTS

# Replace this with any English phrase you want
english_text = "mumucik"

# Set language to English ('en')
tts = gTTS(text=english_text, lang='en')

# Save the audio file
tts.save("english_speech.mp3")

print("Audio saved as english_speech.mp3")
