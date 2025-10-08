import re

def extract_my_messages(file_path, output_path, my_name):
    def contains_link_or_emoji(message):
        # Check for links (starting with http, www, or containing .com, etc.)
        link_pattern = r"http[s]?://|www\.|\.com|\.org|\.net"
        if re.search(link_pattern, message):
            return True

        # Check for emojis (Unicode ranges for emojis)
        emoji_pattern = r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F]"
        if re.search(emoji_pattern, message):
            return True

        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.readlines()

    my_messages = []
    for line in data:
        # Match the WhatsApp message pattern
        match = re.match(r"^\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2} - (.*?): (.*)$", line)
        if match:
            name, message = match.groups()
            if (
                name.strip() == my_name and
                "<Media omitted>" not in message and
                not contains_link_or_emoji(message)
            ):
                my_messages.append(message)

    # Write the extracted messages to a new file
    with open(output_path, 'w', encoding='utf-8') as out_file:
        for msg in my_messages:
            out_file.write(msg + "\n")

    print(f"Extracted {len(my_messages)} messages. Saved to {output_path}.")

# Adjust file paths for your system
file_path = 'test2.txt'  # Replace <your_username>
output_path = '2.txt'  # Update path for output file
my_name = "Warisha"  # Replace with your WhatsApp display name

# Run the function
extract_my_messages(file_path, output_path, my_name)
