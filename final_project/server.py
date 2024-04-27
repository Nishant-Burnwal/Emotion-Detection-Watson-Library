"""
This module provides a Flask application for emotion detection.
It uses the EmotionDetection.emotion_detection module to detect
emotions in a given text.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Emotion Detection function
    Accepts a text input, detects emotions, and returns the emotion scores.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # creating variables for emotions
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # returning final output
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    output = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust':{disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness':{sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return output

@app.route("/")
def render_index_page():
    """
    Renders the index.html template for the application.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
