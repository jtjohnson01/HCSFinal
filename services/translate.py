import os
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'

translate_client = translate.Client()

def english_to_chinese(word):
    client = translate.Client()
    result = client.translate(word, target_language='zh-CN')

    return result['translatedText']
