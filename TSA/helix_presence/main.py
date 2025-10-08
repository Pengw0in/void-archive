from pypresence import Presence
import time
import sys

CLIENT_ID = "1371195202932310138"

rpc = Presence(CLIENT_ID)
rpc.connect()

filename = sys.argv[0] if len(sys.argv) > 1 else "Unknown file"
print(f"updating Discord status: Editing {filename}")

try:
    rpc.update(
        details=f"editing {filename}",
        start=time.time()
    )
except Exception as e:
    print(f"Failed to update on discord: {e}")

time.sleep(15)
rpc.close()
