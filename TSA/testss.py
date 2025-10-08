import jwt
import time

payload = {
  "auth": 1747828426599,
  "agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
  "role": "user",
  "iat": int(time.time())
}
secret = "your-secret-key"
token = jwt.encode(payload, secret, algorithm="HS256")
print(token)