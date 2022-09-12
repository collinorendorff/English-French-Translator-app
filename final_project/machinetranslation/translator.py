import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#setting up instance of IBM Watson Language Translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3 (
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url(url)

MODEL_ID1 = 'en-fr'

def english_to_french(english_text):
    #write the code here
    if english_text is None:
        return "No input text given, please enter text to be translated."

    temp = language_translator.translate(
        text=english_text,
        model_id=MODEL_ID1).get_result()
    translation = temp['translations'][0]['translation']
    french_text = translation
    return french_text

MODEL_ID2 = 'fr-en'

def french_to_english(french_text):
    if french_text is None:
        return "No input text given, please enter text to be translated."

    temp = language_translator.translate(
        text=french_text,
        model_id=MODEL_ID2).get_result()
    translation = temp['translations'][0]['translation']
    english_text = translation
    return english_text
