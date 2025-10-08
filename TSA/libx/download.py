from lxml import html
import requests
import json
import re

URL = "https://libgen.li/ads.php?md5=40CF5B521C6BFB21CDD86DBE239B10B8"

page = requests.get(URL)

with open("page.html", "w", encoding="utf-8") as f:
    f.write(page.text)

tree = html.fromstring(page.content)

part = tree.xpath(
    '//*[@id="main"]/tr[1]/td[2]/a/@href'
)
print(part[0])

key = re.findall(r'key=([0-9A-Z]{16})', part[0])

print(key)