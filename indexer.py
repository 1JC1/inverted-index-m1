import json
import os
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
import re


# Read through JSON file, create docID, parse content with listed encoding, tokenize,
# stemming and other language processing, add doc as postings to inverted index (dictionary)
main_index = defaultdict(list)
url_index = dict()
docID = 0

stemmer = SnowballStemmer("english", ignore_stopwords=True)

for file in os.listdir("cyberclub_ics_uci_edu"):
    file_index = defaultdict(int)
    
    with open("cyberclub_ics_uci_edu/" + file) as f:
        data = json.load(f)
        soup = BeautifulSoup(data['content'].encode(data['encoding']), 'lxml', from_encoding = data['encoding'])
        tokens = word_tokenize(soup.get_text())
    
    for token in tokens:
        alphanum = re.sub(r'[^a-zA-Z0-9]', '', token)
        
        if len(alphanum) != 0:
            stem = stemmer.stem(alphanum)
        #print(f'Token: {token}, Stem: {stem}')
        
        file_index[stem] += 1
    
    for stem, freq in file_index.items():
        main_index[stem].append((docID, freq))
        url_index[docID] = data['url']
    
    docID += 1

print(main_index)
        

            