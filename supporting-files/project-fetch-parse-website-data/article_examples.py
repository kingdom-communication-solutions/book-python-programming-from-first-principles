# Worked examples from Project: Fetch & Parse Real Website Data.
# Run from a separate practice folder.

from bs4 import BeautifulSoup

def extract_article(html):
    soup = BeautifulSoup(html, "html.parser")
    heading = soup.find("h1")
    content = soup.select_one("#mw-content-text")
    if heading is None or content is None:
        raise ValueError("Article heading or content is missing")
    for paragraph in content.find_all("p"):
        intro = paragraph.get_text(" ", strip=True)
        if intro:
            return {"title": heading.get_text(" ", strip=True), "intro": intro}
    raise ValueError("Article has no non-empty paragraph")

samples = [
    ("Python (programming language)", "Python programs can process text and numbers."),
    ("Artificial intelligence", "AI systems perform tasks using computational models."),
    ("Web scraping", "A scraper extracts selected information from web pages."),
]
articles = []
for title, intro in samples:
    html = f'<h1>{title}</h1><div id="mw-content-text"><p></p><p>{intro}</p></div>'
    articles.append(extract_article(html))

for article in articles:
    print(article["title"])
    print(article["intro"])
