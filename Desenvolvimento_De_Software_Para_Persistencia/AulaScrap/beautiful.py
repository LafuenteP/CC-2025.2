from bs4 import BeautifulSoup

with open("beautiful.html", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
    print("Title:", soup.title.get_text())