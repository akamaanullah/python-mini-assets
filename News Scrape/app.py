import requests
from bs4 import BeautifulSoup

def get_news():
    url = "https://www.bbc.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    headlines = soup.find_all('h3')
    for idx, headline in enumerate(headlines[:5]):
        print(f"{idx + 1}. {headline.get_text()}")

get_news()
