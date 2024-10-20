import requests,json

def emotion_detector(text_to_analyse):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data={ "raw_document": { "text": text_to_analyse } }

    response = requests.post(url,headers=header,data=json.dumps(data))
    if response.status_code==400:
        output={
            'angry':None,
            'fear':None,
            'joy':None,
            'sadness':None,
            'disgust':None,
            'dominant_emotion':None,
        }
        return output
    data = json.loads(response.text)
    formatted_output = data['emotionPredictions'][0]['emotion']
    indices = list(formatted_output.values())
    dominant = max(indices)
    for key,value in formatted_output.items():
        if value==dominant:
            dominant=key
    formatted_output['dominant_emotion']=dominant

    return formatted_output