import regex as re
import subprocess
import sys

result = (re.search(r'(?<=https:\/\/wallhaven\.cc\/w\/)[a-zA-Z0-9]+', sys.argv[1])).group()
print(result)
print(f"https://w.wallhaven.cc/full/w5/{result}.png")
subprocess.run(["curl",f"https://w.wallhaven.cc/full/w5/{result}.png", "-o", f"{result}.png"])

