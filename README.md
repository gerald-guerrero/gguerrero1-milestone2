# project1-gguerrero1
link for heroku project here: https://gguerrero-movies.herokuapp.com/
This project uses the flask framework, pylint, and will be deployed using heroku
The TMDB API and Wikipedia MediaWiki API will be used
The libraries in the project are flask, os, random, requests dotenv, itertools, json

## Deployment Instructions
Ensure that the following items are installed in order to continue with deploying the project on heroku:
python
flask
requests
python-dotenv
pylint
heroku cli

1. Make an account with TMDB, at https://www.themoviedb.org/, and apply for an api key
2. Make an account for Heroku at https://www.heroku.com/
3. Fork the project and clone it to a local repository using `git clone git@github.com:csc4350-sp22/project1-gguerrero1.git`
4. Open the project folder and create a .env with your api key in it. example: `TMDB_KEY="your key here"`
5. You can now run app.py, and the app should work
6. Using wsl or terminal navigate to the local repository and login to heroku using: `heroku login -i`
7. use: `heroku create` to create the heroku app
8. go to your heroku app settings through the website, and input you api key in the config vars section. example: `TMDB_KEY` `your key here`
9. use `git push heroku main` to push your code to your heroku app
10. use `heroku open` to get the link to get the app link

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

How did your experience working on this milestone differ from what you pictured while working through the planning process? What was unexpectedly hard? Was anything unexpectedly easy?