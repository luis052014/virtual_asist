import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia
import pyautogui,webbrowser
from time import sleep
from unicodedata import normalize
import re
import whatimage
import weather
from os import getenv
from dotenv import load_dotenv



name_asist ='alexo'
key = getenv("GOOGLE_KEY")
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[21].id)

source = sr.Microphone()
#yor contacts in the dic key as name contact iqual to whattsap and the value is numberphone
contacts_autorized = {
                    'girl':'585545455',
                    'dad':'5553843640',
                    'mom':'1111822336',
}


def normalizar(message: str):
    # -> NFD y eliminar diacríticos
    message = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", message), 0, re.I
    )

    # -> NFC
    return normalize( 'NFC', message)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
   
    with source:
        listener.adjust_for_ambient_noise(source)
        print("Escuchando...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice,language='es-ES')
        rec = rec.lower()
        print(rec)
        if name_asist in rec:
            rec =rec.replace(name_asist,'')
            print(rec)

 

    return rec

def run():
    try:
        rec = listen()
        if 'reproduce' in rec:
            music = rec.replace('reproduce','')
            talk('Reproduciendo'+ music)
            pywhatkit.playonyt(music)

        elif 'quién es' in rec:
            people = rec.replace('quién es','')
            talk('Buscando información en wikipedia de'+people)
            info = wikipedia.summary(people,1)
            talk(info)

        elif 'busca' in rec:
            search = rec.replace('busca','')
            talk('Buscando en google'+search)
            pywhatkit.search(search)


        elif 'cuántos suscriptores tiene' in rec:
            name_subs = rec.replace('cuántos suscriptores tiene','')
            data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername='+ name_subs.replace(" ","") + '&key=' + key).read()
            subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
            talk(name_subs+ " tiene {:,d}".format(int(subs))+ "subscriptores")

        elif 'hora' in rec:
            hora = datetime.datetime.now().strftime('%H:%M %p')
            talk("Son las "+hora)

        elif 'cómo está el clima' in rec:
            city_name = rec.replace('cómo está el clima en ','')
            info = weather.weather_api(city_name)
            talk('Buscando clima de '+ city_name)
            print(info)
            talk(info)

        if 'envía' in rec:
            msg = rec.replace('envía ','')
            msg_list = msg.split(' ')
            name = msg_list[2]

            if name in contacts_autorized.keys():
                number = contacts_autorized.get(name)
                msg = msg.replace(name,'')

                if 'mensaje a' in msg:
                    msg = msg.replace('mensaje a  ','')
                    talk('Enviando mensaje a '+ name)
                    webbrowser.open('https://web.whatsapp.com/send?phone=+52'+number)
                    sleep(11)
                    msg = normalizar(msg)
                    msg.capitalize()
                    pyautogui.typewrite(msg)
                    pyautogui.press("enter")

                elif 'meme a'in msg:
                    talk('Enviando meme a ',name)
                    try:
                        whatimage.choice_meme_image(number)
                    except:
                        talk('No hay memes para enviár')

                elif 'amor a ' in msg :
                    talk('Enviando imagen de amor a ',name)

                    try:
                        whatimage.choice_love_image(number)
                    except:
                        talk('No hay imágenes de amor para enviár')
            else:
                talk('El contácto no está autorizado para enviarle mensajes')


        else:
            talk("No entendí, repite por favor")

    except:
        pass

def run_asist():
    while True:
        run()

if __name__=='__main__':
    run_asist()
