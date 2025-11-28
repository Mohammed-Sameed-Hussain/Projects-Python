import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
web_response = response.text


soup = BeautifulSoup(web_response, "html.parser")
movie_tags = soup.find_all(name='h3', class_='title')

movies = []

for movie_tag in movie_tags :
    
    movies.append(movie_tag.getText())


movies.reverse()

with open("Top 100 Movies of All Time", 'w') as txt_file:
    for movie in movies:
        txt_file.write(movie + '\n')

