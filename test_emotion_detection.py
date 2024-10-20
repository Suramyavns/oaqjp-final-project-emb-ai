from EmotionDetection.emotion_detection import *
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        statement = 'I am glad this happened'
        self.assertEqual(emotion_detector(statement)['dominant_emotion'],'joy')
    def test_anger(self):
        statement = 'I am really mad about this'
        self.assertEqual(emotion_detector(statement)['dominant_emotion'],'anger')
    def test_disgust(self):
            statement = 'I feel disgusted just hearing about this'
            self.assertEqual(emotion_detector(statement)['dominant_emotion'],'disgust')
    def test_sadness(self):
            statement = 'I am so sad about this'
            self.assertEqual(emotion_detector(statement)['dominant_emotion'],'sadness')
    def test_fear(self):
            statement = 'I am really afraid that this will happen'
            self.assertEqual(emotion_detector(statement)['dominant_emotion'],'fear')

if __name__=='__main__':
    unittest.main()