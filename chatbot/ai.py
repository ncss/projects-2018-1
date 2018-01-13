# -*- coding:utf8 -*-
# !/usr/bin/env python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import tornado


class ChatBotWebSockets(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WS Open")
        self.chatBot = ChatBot()
        self.chatBot.set_callback(self.send_message)



    def on_message(self, message):
        self.chatBot.send_message(message)

    def send_message(self, message):
        self.write_message(message)


# html
# Animate
# + Websockets connection
# + integration

import os.path
import sys
import json

from pprint import pprint

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '6f9e90c82ed74f66b58be8351a924b11 '



class ChatBot:
    def __init__(self):
        self.callback = None

    def send_message(self, message):
        ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

        request = ai.text_request()

        request.lang = 'en'  # optional, default value equal 'en'
        request.session_id = "1234"
        request.query = message

        response = request.getresponse()

        dictResponse = json.loads(response.read())

        self.receive_message(dictResponse['result']['fulfillment']['speech'].strip())

    def receive_message(self, message):
        self.callback(message)

    def set_callback(self, callback):
        self.callback = callback


chatBot = ChatBot()
chatBot.set_callback(print)
chatBot.send_message("hey")


# def send(string):
#     ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
#
#     request = ai.text_request()
#
#     request.lang = 'en'  # optional, default value equal 'en'
#     request.session_id = "1234"
#     request.query = string
#
#     response = request.getresponse()
#
#     dictResponse = json.loads(response.read())
#     # pprint (response.read())
#     print("Com:", dictResponse['result']['fulfillment']['speech'].strip())
#
#
# def receive(function):
#     function(response)
#
# if __name__ == '__main__':
#     inp = input("You: ")
#     while inp.strip() != "":
#         send(inp)
#         inp = input("You: ")
