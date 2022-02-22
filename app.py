import flask
import os
from TMDB import movie_data
from WIKI import wiki_data
import random
app = flask.Flask(__name__)

@app.route("/")
def index():
    id_list = []
    id_list.append(1891)
    id_list.append(604)
    id_list.append(155)

    title, tagline, genres, image = movie_data(random.choice(id_list))
    url = wiki_data(title)
    
    return flask.render_template(
        "index.html",
        title=title,
        tagline=tagline,
        genres=genres,
        image=image,
        url=url
    )

app.run(
    host='0.0.0.0',
    port=int(os.getenv('PORT', 8080)),
    debug=True
)