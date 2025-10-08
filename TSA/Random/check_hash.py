hash_in = input("Enter hash: ").strip()

with open("hash.txt", 'r') as file:
    content = file.load()

for hash_line in content:
    if hash_line == hash_in:
        print("Hash found in safe list.")
    else:
        print("Hash not found in safe list.")