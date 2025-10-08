from lxml import html
import requests
import json
import re

# Constants
VIEW = "simple"
RES = 25
COLUMN = "def"
REQ = "money"
URL = f"https://libgen.is/search.php?req={REQ}&lg_topic=libgen&open=1&view={VIEW}&res={RES}&phrase=1&column={COLUMN}"
book_data_list = []


# Initial request
result_page = requests.get(URL)
if result_page.status_code != 200:
    print(f"Recived status code {result_page.status_code} , expected: 200, exiting..")
    exit(1)

# scarping logic
tree = html.fromstring(result_page.content)
book_rows = tree.xpath('//tr[td/a[contains(@href, "book/index.php")]]')

for row in book_rows:
    book_id = row[0].text_content().strip() # book id
    
    book_links = row.xpath('.//a[@href]') # book md5
    for link in book_links:
        href_attr = link.get("href")
        book_md5_list = re.findall(r'md5=([0-9a-fA-F]{32})', href_attr)
        if book_md5_list:
            book_md5 = book_md5_list[0]

    book_title_a = (row.xpath('.//a[contains(@href, "book/index.php")]'))[0].xpath('text()[normalize-space()]')
    book_title = book_title_a[0].strip()


    book_authors = row[1].text_content().strip() # book author
    book_pub = row[3].text_content().strip() # book publisher
    book_year = row[4].text_content().strip() # book date
    book_language = row[6].text_content().strip()
    book_size = row[7].text_content().strip()
    book_pages = row[5].text_content().strip()


    book_data = {
        "book_id": book_id,
        "book_md5": book_md5,
        "book_authors": book_authors,
        "book_title" : book_title,
        "book_publisher": book_pub,
        "book_year": book_year,
        "book_pages": book_pages,
        "book_language": book_language,
        "book_size": book_size
    }
    book_data_list.append(book_data)

for book in book_data_list[:30]:
    print(book["book_title"])
    
with open("book_info.json", "w") as f:
    json.dump(book_data_list, f, indent=4)
book_data_list = []
