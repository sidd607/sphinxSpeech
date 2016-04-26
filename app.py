from flask import Flask, abort, request, jsonify, make_response
from flask import *
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from twisted.python import log
from twisted.internet import reactor
import sys

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/webSpeech')
def webSpeech():
	return render_template('webSpeech.html')

@app.route('/sphinxDemo')
def sphinxDemo():
	return render_template('sphinxDemo.html')


if __name__ == '__main__':
	app.run(debug = True)
