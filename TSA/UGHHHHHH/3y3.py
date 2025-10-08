import subprocess

def encode(primary: str, accent: str) -> str:
    # Format the message like: [#5865f2,#57f287]
    message = f"[#{primary},#{accent}]"
    padding = ""  # Not used, but kept for parity

    # Encode only characters between ASCII 0x20 and 0x7F by shifting into the private Unicode range
    encoded = ''.join(
        chr(codepoint + 0xE0000)
        for char in message
        if 0x20 <= (codepoint := ord(char)) <= 0x7F
    )

    result = (padding or "") + " " + encoded
    return result

primary = input("Primary color: ")
accent = input("Accent color: ")

result = encode(primary, accent)

subprocess.run('pbcopy', universal_newlines=True, input=result)
print("Result copied to clipboard!")