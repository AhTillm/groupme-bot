import os
import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, json, request
import requests


andrew_responses = ["Wow Andrew!",
 	"You're doing great Sweetie!", 
	"Keep up the good work Andrew!", 
 	"If I were a person I would love you", 
 	"Say it louder for the people in the back, Andrew",
	"Andrew is the best Coordinator",
	"Outstanding Andrew!", 
	"Very thoughtful Andrew"]

app = Flask(__name__)

@app.route('/', methods=['POST'])
def groupme_callback():
	json_body = request.get_json()
	if json_body['sender_type'] != 'bot':
		# some degree of verification that it is sent via a groupme callback
		# could also check for "User-Agent: GroupMeBotNotifier/1.0", but that's plenty spoofable

		userName = json_body['name']
		### BOT CODE GOES HERE! ###
		if userName == os.environ['username']:
			message = random.choice(andrew_responses)
			reply(message)
	
	return "ok", 200

def reply(message):
	payload = {
		'bot_id' : os.environ['BOT_ID'],
		'text'   : message,
	}
	request = Request('https://api.groupme.com/v3/bots/post', urlencode(payload).encode())
	json = urlopen(request).read().decode()



if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	# app.run(host='0.0.0.0', port=port, debug=True)
	app.run(host='0.0.0.0', port=port)
