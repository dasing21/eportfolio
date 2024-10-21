import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/Data_science"
word = "Data Scientist"


def scrape_and_parse(url, word):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")


text = soup.get_text().lower()
word_count = text.count(word.lower())

data = {"url": url, "word": word, "occurences of word": word_count}

with open("word_count_data.json", "w") as f:
    json.dump(data, f, indent=4)

if __name__ == "__main__":
    scrape_and_parse(url, word)

# EXAMPLE OF OUTPUT
# {
#     "url": "https://en.wikipedia.org/wiki/Data_science",
#     "word": "Data Scientist",
#     "occurences of word": 13,
# }