from pypresence import Presence
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

CLIENT_ID = "1371195202932310138"
rpc = Presence(CLIENT_ID)
rpc.connect()

# Monitor the file path
file_to_monitor = sys.argv[1] if len(sys.argv) > 1 else "unknown_file.txt"

class FileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == file_to_monitor:
            print(f"File {file_to_monitor} is being edited!")
            rpc.update(details=f"Editing {file_to_monitor}", start=time.time())

# Set up the observer to watch the directory containing the file
event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, path=".", recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

# Close Discord RPC when finished
rpc.close()

