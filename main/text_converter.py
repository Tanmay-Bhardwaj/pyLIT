from deep_translator import GoogleTranslator
from elevenlabs import play,stream,save
from elevenlabs.client import ElevenLabs


text=input=("Enter the text you want to convert:")
def language_translate():
    translated_fr = GoogleTranslator(source='auto', target='fr').translate(text)
    translated_hi = GoogleTranslator(source='auto', target='hi').translate(text)
    translated_mr = GoogleTranslator(source='auto', target='mr').translate(text)
    print(translated_fr)
    print(translated_hi)
    print(translated_mr)
    
    


language_translate()
    