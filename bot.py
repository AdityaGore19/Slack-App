import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slack import WebClient
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)
slack_client = WebClient(token=os.environ['SLACK_TOKEN'])

@app.route('/slack/forward', methods=['POST'])
def forward_message():
    command = request.form.get('command')
    text = request.form.get('text')

    if command == '/forward':
        # Post the original message in Channel 1
        slack_client.chat_postMessage(channel='#channel1', text=text)
        
        # Post the message to Channel 2 in uppercase
        slack_client.chat_postMessage(channel='#channel2', text=text.upper())
        
        return Response(), 200
    else:
        return Response("Invalid command", status=400)

if __name__ == "__main__":
    app.run(debug=True)
