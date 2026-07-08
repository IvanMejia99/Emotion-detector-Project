import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Parsear la respuesta JSON
    formatted_response = json.loads(response.text)
    
    # Extraer el diccionario de emociones
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Formatear la salida requerida
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }
    
    # Calcular la emoción dominante
    result['dominant_emotion'] = max(emotions, key=emotions.get)
    
    return result
