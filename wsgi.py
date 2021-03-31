import time
import flask
import random


app = flask.Flask(__name__)


@app.route('/')
def home():
    sleep_time = random.random()
    time.sleep(sleep_time)
    return {'message': 'hello world', 'sleep': sleep_time}
