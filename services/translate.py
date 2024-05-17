import os
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

credentials_info = {
    "type": os.getenv("GOOGLE_CLOUD_TYPE"),
    "project_id": os.getenv("GOOGLE_CLOUD_PROJECT_ID"),
    "private_key_id": os.getenv("GOOGLE_CLOUD_PRIVATE_KEY_ID"),
    "private_key": os.getenv("GOOGLE_CLOUD_PRIVATE_KEY").replace('\\n', '\n'),
    "client_email": os.getenv("GOOGLE_CLOUD_CLIENT_EMAIL"),
    "client_id": os.getenv("GOOGLE_CLOUD_CLIENT_ID"),
    "auth_uri": os.getenv("GOOGLE_CLOUD_AUTH_URI"),
    "token_uri": os.getenv("GOOGLE_CLOUD_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("GOOGLE_CLOUD_AUTH_PROVIDER_CERT_URL"),
    "client_x509_cert_url": os.getenv("GOOGLE_CLOUD_CLIENT_CERT_URL")
}

credentials = service_account.Credentials.from_service_account_info(credentials_info)
translate_client = translate.Client(credentials=credentials)

def english_to_chinese(word):
    client = translate.Client()
    result = client.translate(word, target_language='zh-CN')

    return result['translatedText']
