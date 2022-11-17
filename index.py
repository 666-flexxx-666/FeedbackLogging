from flask import Flask, render_template, request
import logging
from datetime import datetime
import json

logging.getLogger("werkzeug").disabled = True
logging.basicConfig(filename='record.log', level=logging.DEBUG)

app = Flask(__name__)

file = open("static/messages.txt", "r")
messages = file.read()

messages_dict = json.loads(messages)
json_remove = '"\'{}b'

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


@app.route('/chat/')
def chat():
    now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" ")
    app.logger.debug(now + "successfully loaded chat.html for " + str(request.remote_addr))
    return render_template('chat.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user = data["user"]
    message = data["message"]
    new_key = int(list(messages_dict)[-1]) + 1
    messages_dict.update({str(new_key): {user: message}})
    messages_string = str(messages_dict).replace("'", '"')
    file = open("static/messages.txt", "w")
    file.write(messages_string)
    file.close()
    now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" ")
    app.logger.debug(now + "successfully POST for " + str(request.remote_addr))
    return request.json


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)


