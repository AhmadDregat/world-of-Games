import os

from flask import Flask
from flask import Response
from Utils import SCORES_FILE_NAME

app = Flask(__name__)

@app.route('/')
def show_score():

    if os.path.exists(SCORES_FILE_NAME):
        file = open(SCORES_FILE_NAME, 'r')
        score = file.read()
        return (f'<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">{score}</div></h1></body></html>')
    else:
        return(f'<html><head><title>Scores Game</title></head><body><h1>The Exception is:  <div id="score">The file is not exist "{SCORES_FILE_NAME}" </div><h1>500<h1></h1></body></html>')


if __name__ == '__main__':
    app.run()

