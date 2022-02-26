# project1-gguerrero1
link for heroku project here: https://gguerrero-movies.herokuapp.com/
This project uses the flask framework, pylint, Black python linter, and will be deployed using heroku
The TMDB API and Wikipedia MediaWiki API will be used
The libraries in the project are flask, os, random, requests dotenv, itertools, flask-SQLAlchemy, flask-login
postgresql will be used for the databaase
psycopg2-binary is also included

## Deployment Instructions
Ensure that the following items are installed in order to continue with deploying the project on heroku:
python
flask
requests
python-dotenv
postgresql
psycopg2-binary
flask-SQLAlchemy
flask-login
pylint
Black python linter
heroku cli

1. Make an account with TMDB, at https://www.themoviedb.org/, and apply for an api key
2. Make an account for Heroku at https://www.heroku.com/
3. Fork the project and clone it to a local repository using `git clone git@github.com:csc4350-sp22/milestone2-gguerrero1.git`
4. Open the project folder and create a .env with your api key in it. example: `TMDB_KEY="your key here"`
5. Using wsl or terminal navigate to the local repository and login to heroku using: `heroku login -i`
6. use: `heroku create` to create the heroku app
7. create a database with the command `heroku addons:create heroku-postgresql:hobby-dev`
8. use `heroku config` to see the the database url then copy and paste it into the .env file as `DATABASE_URL="your url here"` (replace the beginning portion "postgres" with "pstgresql" if needed)
9. use the command `python -c 'import secrets; print(secrets.token_hex())'` to generate a secret and copy and paste it into the .env file as `SECRET_KEY="your key here"` (if command does not work, try replacing python with python3)
10. You can now run app.py
11. Export the three variables in your .env file. Example: `export variable="value"`. Or go to your heroku app settings through the website, and input the variables manually into the config vars
12. use `git push heroku main` to push your code to your heroku app
13. use `heroku open` to get the link to get the app link

## Questions Milestone 1
a. What are at least 3 technical issues you encountered with your project? How did
you fix them?
The method to retreive the wikipedia link was a bit of an issue. The api response seemed to be a multi-dimensional list, so I looked up how to turn that into a 1-dimensional list and returned the element containing a url-like string. I used the source: https://www.geeksforgeeks.org/python-itertools-chain/

Another slight technical issue was getting a random movie to appear every time, but that was a simple issue to solve. I imported the random library and used it to select a random item from the list of hard coded movie IDs and then passed that as a parameter to the movie_data function. The source was the python documentation https://docs.python.org/3/library/random.html

b. What are known problems (still existing), if any, with your project?
    There are no problems with the project functionality, but the method to retrieve the wikipedia link does not seem optimal

c. What would you do to improve your project in the future?
    I'd like to add a search feature to allow users to lookup movies of their choice which might be possible throught html inputs and other api requests

## Questions Milestone 2
What are at least 2 technical issues you encountered with your project? How did you fix them?
- One issue I encountered was the website not working due to a lack of a secret key. in order to create a secure key I chose to generate one using the command from the documentation here: https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions

- Another issue I encountered happened when trying to separate the website route pages and the database table models into individual files. There were multiple errors and circular import issues but I was able to resolve it. For the route pages, I fixed it importing them from their own files into app.py as blurprints according to the source: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login. For the database table models, I was able to fix it by making the `db = SQLAlchemy()` variable in models.py, then importing and creating db in app.py under with another condition. The source of this idea came from the milestone-2 channel in the class discord

How did your experience working on this milestone differ from what you pictured while working through the planning process? What was unexpectedly hard? Was anything unexpectedly easy?
- There was much more debugging and troubleshooting in this milestone. There were muletiple issues that caused site errors or just made the site not work as intended, which I had to spend time on to fix
- Separating components into different files was harder than I thought. It took a sizable amount of time to make it functional without breaking the site
- Nothing was unexpectedly easy in this milestone, but taking in user input for the comments wasn't too difficult