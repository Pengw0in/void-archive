import requests
from bs4 import BeautifulSoup

url = "https://anigo.to/az-list/F/genres/harem"

# Send the request
response = requests.get(url)

# Get the content as a string
html_content = response.text

# Use BeautifulSoup to pretty-format the HTML
soup = BeautifulSoup(html_content, 'html.parser')
pretty_html = soup.prettify()

# Write the formatted HTML to a file
output_file = "anigo_response.html"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(pretty_html)

print(f"HTML content has been written to {output_file}")

