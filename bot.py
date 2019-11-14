import os
import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, json, request
import requests
import time 


app = Flask(__name__)

day = 1 

@app.route('/', methods=['POST'])
def groupme_callback():
	json_body = request.get_json()
	if json_body['sender_id'] == '821534':
			message = json_body['text']
			if( message[:1] == 'H'):
				time.sleep(5)
				reply("We did it" )
	if json_body['sender_type'] != 'bot':
		message = json_body['text']
		### BOT CODE GOES HERE! ###
		if(message == "Start Xmas"):
			welcomeMSN = "Hello and welcome to your Christmas Countdown Bot\nEveryday from now until December 25th this GroupMe will recieve an automated message to spark Holiday Cheer!\n\nHappy Holidays and Let the Festivity’s Begin!!"
			time.sleep(5)
			reply(welcomeMSN)
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
