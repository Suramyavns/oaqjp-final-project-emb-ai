'''
This is the main server script for the application
'''

from flask import Flask,jsonify,request,render_template
from EmotionDetection import emotion_detection
app = Flask(__name__)

@app.route('/',methods=['GET'])
def root():
    '''
    Root path of this server
    '''
    return render_template('index.html')

@app.route('/emotionDetector',methods=['GET'])
def emotion_detector():
    '''
    REST endpoint to get the emotion analysis for the query text
    '''
    text = request.args.get('textToAnalyze')
    emotion = emotion_detection.emotion_detector(text)
    if emotion['dominant_emotion']:
        return jsonify(emotion)
    return 'Invalid text! Please try again!\n'

if __name__=='__main__':
    app.run(debug=True)
