from flask import Flask, render_template, request
import logging
from datetime import datetime

logging.basicConfig(filename='record.log', level=logging.DEBUG)


app = Flask(__name__)

now = ""
@app.route('/')
def main():
    now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" ")
    app.logger.debug( now + "successfully loaded index.html for " + str(request.remote_addr))
    return render_template('index.html')


@app.route('/feedback/')
def form():
    now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" ")
    app.logger.debug(now + "successfully loaded form.html for " + str(request.remote_addr))
    return render_template('form.html')

