from http.server import BaseHTTPRequestHandler
from cowpy import cow
import json

file = open("../../static/messages.txt", "r")
messages = file.read()

messages_dict = json.loads(messages)
json_remove = '"\'{}b'

class hander(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        data = self.json
        user = data["user"]
        message = data["message"]
        new_key = int(list(messages_dict)[-1]) + 1
        messages_dict.update({str(new_key): {user: message}})
        messages_string = str(messages_dict).replace("'", '"')
        file = open("../../static/messages.txt", "w")
        file.write(messages_string)
        file.close()
        return self.json

