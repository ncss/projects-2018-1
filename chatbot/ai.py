import tornado
import os.path
import sys
import json
import database.company
import apiai

class ChatBotWebSockets(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WS Open")
        self.chatBot = ChatBot()
        self.chatBot.set_callback(self.send_message)

    def on_message(self, message):
        self.chatBot.send_message(message)

    def send_message(self, message):
        self.write_message(message)

from pprint import pprint



CLIENT_ACCESS_TOKEN = '6f9e90c82ed74f66b58be8351a924b11 '



class ChatBot:
    def __init__(self):
        self.callback = None

        self.language = ""
        self.size = 0
        self.formality = 0

    def send_message(self, message):
        ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

        request = ai.text_request()

        request.lang = 'en'  # optional, default value equal 'en'
        request.session_id = "1234"
        request.query = message

        response = request.getresponse()

        dictResponse = json.loads(response.read())

        responseMessage = dictResponse['result']['fulfillment']['speech'].strip()


        try:
            if responseMessage.startswith("____"):
                self.size = int(message)

                self.receive_message("I would recommend you checkout:")
                self.receive_message(str(database.company.suggestComp(self.formality, self.size, self.language)[0]))

            elif responseMessage.startswith("___"):
                self.formality = int(message)
            elif responseMessage.startswith("__"):
                self.language = message
        except ValueError:
            self.receive_message("That wasn't a valid number.")

        self.receive_message(responseMessage)

    def receive_message(self, message):
        self.callback(message.strip("_"))

    def set_callback(self, callback):
        self.callback = callback
