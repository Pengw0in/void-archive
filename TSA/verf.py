import requests
import random
import string
import time

URL = "http://challenge.nahamcon.com:31799/"  # Replace with the actual URL

#Initialize known values,
correct = [""] * 32
present = set()
absent = set()

#Random charset (you can adjust based on the challenge charset),
charset = string.ascii_lowercase + string.digits

def generate_guess():
    guess = []
    for i in range(32):
        if correct[i]:
            guess.append(correct[i])
        else:
            guess.append(random.choice(charset))
    return "".join(guess)

def send_guess(guess_str):
    flag = f"flag{{{guess_str}}}"
    try:
        response = requests.post(URL, json={"guess": flag}, timeout=10)
        print("➡️ Sent Guess:", flag)
        print("📦 Status Code:", response.status_code)
        print("📨 Response Text:", response.text.strip() or "<EMPTY>")
        
        # Check if response is valid JSON
        if response.headers.get('content-type', '').startswith('application/json'):
            return response.json(), flag
        else:
            print("❌ Response is not JSON format")
            return {"error": "not_json", "text": response.text}, flag
            
    except requests.exceptions.Timeout:
        print("❌ Request timeout")
        return {"error": "timeout"}, flag
    except requests.exceptions.ConnectionError:
        print("❌ Connection error")
        return {"error": "connection"}, flag
    except Exception as e:
        print("❌ Error:", e)
        return {"error": str(e)}, flag

def update_knowledge(feedback, guess):
    for i, square in enumerate(feedback):
        if square == "🟩":
            correct[i] = guess[i]
        elif square == "🟨":
            present.add(guess[i])
        elif square == "⬛":
            if guess[i] not in correct and guess[i] not in present:
                absent.add(guess[i])

# Add attempt counter to prevent infinite loops
max_attempts = 1000
attempt = 0

#Main loop,
while attempt < max_attempts:
    attempt += 1
    guess = generate_guess()
    response, full_flag = send_guess(guess)

    # Debug the full response
    print(f"📨 Raw JSON Response: {response}")

    # Check for errors first
    if "error" in response:
        print(f"❌ Error in response: {response['error']}")
        time.sleep(1)  # Wait before retry
        continue

    # Safe access to 'result'
    if "result" not in response:
        print("❌ 'result' key not found in response. Response was:")
        print(response)
        break  # Stop the loop to prevent crashing

    feedback = response["result"]
    print(f"Guess: {full_flag} -> Feedback: {feedback}")

    update_knowledge(feedback, guess)

    if all(correct):
        print(f"🎉 Flag found: flag{{{''.join(correct)}}}")
        break
        
    print(f"Attempt {attempt}/{max_attempts}")

if attempt >= max_attempts:
    print("❌ Max attempts reached")