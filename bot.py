import os
import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, json, request
import requests
import time 


app = Flask(__name__)

#"You're not santa you smell like beef and cheese"
seconds_per_day = 60*60*24
responses = {
	"1": "ONE DAY REMAINING QUOTE",
	"2": "TWO DAYS REMAINING QUOTE",
	"3": "THREE DAYS REMAINING QUOTE",
	"4": "FOUR DAYS REMAINING QUOTE",
	"5": "FIVE DAYS REMAINING QUOTE",
	"6": "SIX DAYS REMAINING QUOTE", 
	"7": "SEVEN DAYS REMAINING QUOTE",
	"8": "EIGHT DAYS REMAINING QUOTE",
	"9": "NINE DAYS REMAINING QUOTE",
	"10": "TEN DAYS REMAINING QUOTE",
	"11": "ELEVEN DAYS REMAINING QUOTE",
	"12": "TWEVELE DAYS REMAINING QUOTE",
	"13": "THIRTEEN DAYS REMAINING QUOTE",
	"14": "FORTEEN DAYS REMAINING QUOTE",
	"15": "FIFTHTEEN DAYS REMAINING QUOTE",
	"16": "SIXTEEN DAYS REMAINING QUOTE",
	"17": "SEVENTEEN DAYS REMAINING QUOTE",
	"18": "EIGHTTEEN DAYS REMAINING QUOTE",
	"19": "NINETEEN DAYS REMAINING QUOTE",
	"20": "TWENTY DAYS REMAINING QUOTE",
	"21": "TWENTY-ONE DAYS REMAINING QUOTE",
	"22": "TWENTY-TWO DAYS REMAINING QUOTE",
	"23": "TWENTY-THREE DAYS REMAINING QUOTE",
	"24": "TWENTY-FOUR DAYS REMAINING QUOTE",
	"25": "TWENTY-FIVE DAYS REMAINING QUOTE"
}

@app.route('/', methods=['POST'])
def groupme_callback():
	json_body = request.get_json()
	if json_body['sender_id'] == '821534':
			message = json_body['text']
			if( message[:1] == 'H'):
				time.sleep(1)
				##Start on 25 days away
				messageReply = "24: "+responses["24"]
				reply( messageReply)
			else: 
				splitMSN = message.split(":", 1)
				if(int(splitMSN[0])-1 > 0):
					time.sleep(1)
					daysLeft = str(int(splitMSN[0])-1)
					messageReply = daysLeft+": "+responses[daysLeft]
					reply(messageReply)
					
	if json_body['sender_type'] != 'bot':
		
		message = json_body['text']
		if(message == "Start Xmas"):
			welcomeMSN = "Hello and welcome to your Christmas Countdown Bot 🎄🎁🎄\nEveryday from now until December 25th this GroupMe will recieve an automated message to spark Holiday🎄🎅 Cheer!\n\nHappy Holidays and Let the Festivities Begin!!\nAuthor: Josh Norman jmnorma@clemson.edu"
			time.sleep(5)
			reply(welcomeMSN)
			
		if( message == "Xmas Bomb"):
			BombMessage = """🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n 
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎄🎄🎄🎄🎄🎄🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄\n
							🎄🎄🎁🎄🎁🎄🎄🎄🎄🎁🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎄🎄🎁🎄🎄🎁🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎄🎄🎄🎁🎁🎄🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎄🎄🎄🎁🎁🎄🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎄🎄🎄🎁🎁🎄🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎄🎄🎄\n 
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎄🎄🎄\n"
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎁🎁🎁🎁🎁🎁🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎁🎁🎁🎁🎁🎁🎁🎁🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎁🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎁🎁🎁🎁🎁🎁🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎁🎁🎁🎁🎁🎁🎁🎁🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎁🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄\n
							🎄🎄🎄🎁🎁🎄🎄🎄🎄🎁🎁🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎁🎁🎄🎄🎁🎁🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎁🎁🎁🎁🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄\n
							🎄🎄🎄🎁🎁🎄🎄🎄🎄🎁🎁🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎁🎁🎄🎄🎁🎁🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎁🎁🎁🎁🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎁🎁🎄🎄🎁🎁🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎁🎁🎄🎄🎄🎄🎁🎁🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n 
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎄🎄🎄🎄🎄🎄🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄\n
							🎄🎄🎁🎄🎁🎄🎄🎄🎄🎁🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎄🎄🎁🎄🎄🎁🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎄🎄🎄🎁🎁🎄🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎄🎄🎄🎁🎁🎄🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎁🎄🎄🎄🎁🎁🎄🎄🎄🎁🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎁🎁🎄🎄🎁🎁🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄\n
							🎄🎄🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎁🎁🎁🎁🎁🎁🎁🎁🎁🎄🎄🎄\n
							🎄🎄🎁🎁🎁🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎁🎁🎁🎁🎁🎁🎁🎁🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎁🎁🎁🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎁🎁🎄🎄🎄🎄\n
							🎄🎄🎁🎁🎁🎁🎁🎁🎁🎁🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n
							🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n"""
			reply("Does this statement even work ")

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
