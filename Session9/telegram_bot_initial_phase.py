import json
import requests
import os
url = "https://api.telegram.org/bot[token]/"

from flask import Response
from flask import request
from flask import Flask

app = Flask(__name__)

def get_all_updates():
    response = requests.get(url + 'getUpdates')
    return response.json()

def get_last_update(allUpdates):
    return allUpdates['result'][-1]

def get_chat_id(update):
    return update['message']['chat']['id']


def sendMessage(chat_id, text, notif=False):
    sendData = {'chat_id' : chat_id, 'text' : text, "disable_notification" : notif}

    response = requests.post(url + 'sendMessage', sendData)
    return response


@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id = get_chat_id(msg)
        text = msg['message'].get('text', '')
        if text == '/start':
            sendMessage(chat_id, "khosh Amadid!!")
        elif 'new' in text:
            contacts = read_json()
            username = msg['message']['from']['username']
            if username not in contacts.keys():
                contacts[username] = []
            contact = text.split(maxsplit=1)[1]
            contacts[username].append(contact)
            write_json(contacts)
        elif text == 'list':
            contacts = read_json()
            username = msg['message']['from']['username']
            if username not in contacts.keys():
                sendMessage(chat_id, 'Your contacts list is empty.')
            else:
                for contact in contacts[username]:
                    sendMessage(chat_id, contact)
        return Response('ok', status=200)
    else:
        return "<h2>myBot</h2>"

def write_json(data, filename="contactList.json"):
    with open(filename, 'w') as target:
        json.dump(data, target, indent=4, ensure_ascii=False)


def read_json(filename="contactList.json"):
    with open(filename, 'r') as target:
        data = json.load(target)
    return data


# while True:
#     data = get_all_updates()
#     lastUpdate = get_last_update(data)
#     response = sendMessage(get_chat_id(lastUpdate), 'khobam!!')
try:
    read_json()
except:
    write_json({})

#when you want to run your code in test mode:
#app.run(debug=True)

app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
