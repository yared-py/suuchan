import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('VEQRVA-U492EJY9G5')

voices = engine.getProperty('voices')
engine.setProperty('voice', 'english')

class voice:
    def talk(audio):
        print('SuuChan: ' + audio)
        engine.say(audio)
        engine.runAndWait()

    def tiempo():
        time = int(datetime.datetime.now().hour)
        if time >= 0 and time < 12:
            talk('good mornig sir Elizondo!')
        if time >= 12 and time < 18:
            talk('good afternoon sir Elizondo!')
        if time >= 18 and time != 0:
            talk('good nigth sir Elizondo!')
voz = voice()
voz.tiempo()
voz.talk('Hello onichan, Im raphtalia your virtual asisten')
voz.talk('How can i help you?')
