import json
import os
from bs4 import BeautifulSoup


# Read through JSON file, create docID, parse content with listed encoding, tokenize,
# stemming and other language processing, add doc as postings to inverted index (dictionary)

for file in os.listdir("cyberclub_ics_uci_edu"):
    with open("cyberclub_ics_uci_edu/" + file) as f:
        data = json.load(f)
        soup = BeautifulSoup(data['content'], 'lxml', from_encoding = data['encoding'])
        print(soup.get_text())