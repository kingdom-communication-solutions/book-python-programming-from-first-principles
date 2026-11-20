# Worked examples from Fetching and Parsing Online Data.
# Run from a separate practice folder.

import json

response_text = '{"id": 1, "title": "Learning Python", "userId": 2}'
post = json.loads(response_text)
print(post["id"])
print(post["title"])

from bs4 import BeautifulSoup

html = """
<html><body>
  <h1>Latest News</h1>
  <ul>
    <li class="headline"><a href="/story1">Python Workshop Opens</a></li>
    <li class="headline"><a href="/story2">New Tools for Data Science</a></li>
    <li class="headline"><a href="/story3">Digital Humanities in Practice</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")
headlines = []
for item in soup.find_all("li", class_="headline"):
    link = item.find("a")
    if link is not None and link.has_attr("href"):
        headlines.append((link.get_text(strip=True), link["href"]))

for title, url in headlines:
    print(f"{title} -> {url}")

from bs4 import BeautifulSoup

soup = BeautifulSoup('<div id="summary"><p>Archive <b>open.</b></p></div>', "html.parser")
content = soup.select_one("#summary")
if content is not None:
    print(content.get_text(" ", strip=True))
