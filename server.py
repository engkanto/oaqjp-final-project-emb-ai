from flask import Flask, jsonify, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyse = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyse)
    return res