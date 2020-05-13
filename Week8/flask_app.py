#!flask/bin/python
from flask import Flask
import csv

app = Flask(__name__)

@app.route('/csv/shows')
def index():
    sstring = ''
    with open('./shows.csv','rt')as f:
        for row in csv.reader(f):
            sstring += str(row) + '\n'
    return sstring

if __name__ == '__main__':
    app.run(debug=True)