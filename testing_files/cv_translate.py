import pytesseract as pyts #Ued to convert image to text(Uses Google OCR[needs to be installed on system])
from PIL import Image
from deep_translator import GoogleTranslator


'''IMPORTANT
need to install [tesseract-ocr-w64-setup-5.4.0.20240606.exe (64 bit)]
from https://github.com/UB-Mannheim/tesseract/wiki and add to path
{pyts.pytesseract.tesseract_cmd=r'PATH of TesseractOCR\ tesseract.exe'}'''

#Providing the system with image to identify
img=Image.open('test.png')
text=pyts.image_to_string(img)


#Translating the text to different languages
def language_translate():
    translated_fr = GoogleTranslator(source='auto', target='fr').translate(text)
    translated_hi = GoogleTranslator(source='auto', target='hi').translate(text)
    translated_mr = GoogleTranslator(source='auto', target='mr').translate(text)
    
    print(translated_fr)
    print(translated_hi)
    print(translated_mr)
    


language_translate()