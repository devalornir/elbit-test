import random
import requests
from flask import Flask
from bs4 import BeautifulSoup

# crawl IMDB top 250 and randomly select a movie

app = Flask(__name__)

URL = 'http://www.imdb.com/chart/top'

@app.route("/")
def main():
    response = requests.get(URL)

    bsobj = BeautifulSoup(response.text, 'html.parser')

    movietags = bsobj.select('td.titleColumn')
    inner_movietags = bsobj.select('td.titleColumn a')
    ratingtags = bsobj.select('td.posterColumn span[name=ir]')

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1] # last item
        return year
    
    years = [get_year(tag) for tag in movietags]
    actors_list = [tag['title'] for tag in inner_movietags] # access attributes 'title'
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in ratingtags] # access attributes 'data-value'

    n_movies = len(titles)

    while(True):
        idx = random.randrange(0, n_movies)

        return f'Random movie from IMDB top 250\n\n{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Staring: {actors_list[idx]}'

        # comment the next line out to test user input with docker run -t -i
        break

        user_input = input('Do you want another movie (y/[n])?')
        if user_input != 'y':
            break

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
