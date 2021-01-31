#! encoding=utf-8
from flask import Flask
import time


print(__name__)
app = Flask(__name__)


@app.route('/dylan')
def index_dylan():
    time.sleep(2)
    test_dict = {1: 2, 3: 4}
    return test_dict


@app.route('/bob')
def index_bob():
    time.sleep(2)
    return 'hello bob'


@app.route('/margan')
def index_margan():
    time.sleep(2)
    return 'hello margan'


app.run(threaded=True)