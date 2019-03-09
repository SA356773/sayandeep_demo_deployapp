from flask import Flask
from flask_ask import statement,question,Ask,session
import time
import os

app = Flask(__name__)
ask = Ask(app,"/webhook")
	
@ask.launch
def handle_launch():
	message = "Hello there, how can I help you ?"
	return question(message)

@ask.intent("AnimalInfoIntent")
def handle_animalInfoIntent():
	result = "This is demo joke on animals"
	return statement(result)


@ask.intent("AMAZON.FallbackIntent")
def handle_fallbackIntent():
	result = "Sorry, I couldn't get that, thank you"
	return statement(result)

if __name__ == '__main__':
    app.run(debug=True)
