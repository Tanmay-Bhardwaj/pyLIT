import speech_recognition as sr
import pyttsx3 
from deep_translator import GoogleTranslator
from elevenlabs import play,stream,save
from elevenlabs.client import ElevenLabs

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
    text=recognizer.recognize_google(audio)


print(text)

def language_translate():
    translated_fr = GoogleTranslator(source='auto', target='fr').translate(text)
    translated_hi = GoogleTranslator(source='auto', target='hi').translate(text)
    translated_mr = GoogleTranslator(source='auto', target='mr').translate(text)
    
    print(translated_fr)
    print(translated_hi)
    print(translated_mr)
    
    
def audio_output(): 
    client = ElevenLabs(
        api_key="sk_87dd324e8bb4a3cf94cb6e1e7f04e37563a640ad62e26c5c"
    )

    audio = client.generate(
    text=text,
    voice="Thomas",
    model="eleven_multilingual_v2"
    )
    #stream(audio)
    save(audio,"output.mp3")
    


language_translate()
audio_output()
    