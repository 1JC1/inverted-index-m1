import json
import os
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer


# Read through JSON file, create docID, parse content with listed encoding, tokenize,
# stemming and other language processing, add doc as postings to inverted index (dictionary)
index = dict()
docID = 0

stemmer = SnowballStemmer("english", ignore_stopwords=True)

for file in os.listdir("cyberclub_ics_uci_edu"):
    with open("cyberclub_ics_uci_edu/" + file) as f:
        data = json.load(f)
        soup = BeautifulSoup(data['content'].encode(data['encoding']), 'lxml', from_encoding = data['encoding'])
    tokens = word_tokenize(soup.get_text())
    
    for token in tokens:
        stem = stemmer.stem(token)

            