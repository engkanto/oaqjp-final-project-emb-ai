import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonfeed = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=jsonfeed, headers=header)

    formatted_response = json.loads(response.text)

    emotion = formatted_response['emotionPredictions'][0]['emotion']

    return emotion | {'dominant_emotion': max(emotion, key=emotion.get)}
