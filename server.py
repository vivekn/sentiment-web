from flask import Flask, render_template, request, jsonify
from info import classify2
from math import e
from redis import Redis
from config import STATS_KEY, HOST, RHOST, RPASS, RPORT

app = Flask(__name__)
app.debug = True
conn = Redis(RHOST, RPORT, password=RPASS)

def percentage_confidence(conf):
	return 100.0 * e ** conf / (1 + e**conf)

def get_sentiment_info(text):
	flag, confidence = classify2(text)
	if confidence > 0.5:
		sentiment = "Positive" if flag else "Negative"
	else:
		sentiment = "Neutral"
	conf = "%.4f" % percentage_confidence(confidence) 
	return (sentiment, conf)

@app.route('/')
def home():
	conn.incr(STATS_KEY + "_hits")
	return render_template("index.html")

@app.route('/api/text/', methods=["POST"])
def read_api():
	text = request.form.get("txt")
	sentiment, confidence = get_sentiment_info(text)
	result = {"sentiment": sentiment, "confidence": confidence}
	conn.incr(STATS_KEY + "_api_calls")
	return jsonify(result=result)

@app.route('/web/text/', methods=["POST"])
def evaldata():
	text = request.form.get("txt")
	result, confidence = get_sentiment_info(text)
	conn.incr(STATS_KEY + "_web_calls")
	return jsonify(result=result, confidence=confidence, sentence=text)

@app.route('/docs/api/')
def api():
	return render_template('api.html', host=HOST)
	