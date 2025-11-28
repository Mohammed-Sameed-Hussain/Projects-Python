import requests
from bs4 import  BeautifulSoup


response = requests.get("https://news.ycombinator.com/news")
web_response = response.text

soup = BeautifulSoup(web_response,'html.parser')



news_spans = soup.find_all(name='span', class_='titleline')
upvotes = soup.find_all(name='span', class_='score')



for article_span, score_span in zip(news_spans, upvotes):
    
    # 1. Extract Article Info
    article_tag = article_span.find('a')
    
    if article_tag:
        text = article_tag.text
        link = article_tag.get('href')
        
        # 2. Extract Score Info
        points = score_span.text
        
        print(f"Text: {text}")
        print(f"Link: {link}")
        print(f"Points: {points}")
        print("---")