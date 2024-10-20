from flask import Flask,jsonify,request,render_template
from EmotionDetection.emotion_detection import *
app = Flask(__name__)

@app.route('/',methods=['GET'])
def root():
    return render_template('index.html')

@app.route('/emotionDetector',methods=['GET'])
def emotionDetector():
    text = request.args.get('textToAnalyze')
    emotion = emotion_detector(text)
    if emotion['dominant_emotion']:
        return jsonify(emotion)
    return 'Invalid text! Please try again!\n'

if __name__=='__main__':
    app.run(debug=True)