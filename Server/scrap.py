import sys, json
from bs4 import BeautifulSoup
import requests
import pandas as pd

data = json.loads(sys.argv[1])

url = data['tabUrl']
selectors = data['selectors']
labels = data['labels']
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
newdata = {}

for i in range(len(selectors)):
    newdata[labels[i]] = [item.text for item in soup.select(selectors[i])]
# Print the data in stringified
print('From Python')
df = pd.DataFrame(newdata)

df.to_csv('Scraped_data.csv', index=False)

# json format so that we can
# easily parse it in Node.js

# json.dumps({'response': ['Data Scraped From Python']})
