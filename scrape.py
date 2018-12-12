import requests
from bs4 import BeautifulSoup
import pandas as pd

#reading webpage into python
r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
#parsing the html using beautiful soup
soup= BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs={'class':'short-desc'})

#loop that returns a dataset of extracted data
records = []
for result in results:
	date = result.find('strong').text + ', 2017'
	lie = result.contents[1][1:-2]
	explanation = result.find('a').text[1:-1]
	url = result.find('a')['href']
	records.append((date, lie, explanation, url))

#put the data into dataframe
df = pd.DataFrame(records, columns=['date', 'lie', 'explanation', 'url'])
df['date'] = pd.to_datetime(df['date'])
#extract data in a csv file
df.to_csv('trump_lies.csv', index=False, encoding='utf-8')
















