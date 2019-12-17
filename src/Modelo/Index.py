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


class Talk:
    @staticmethod
    def speak(audio):
        print('Cleo: ' + audio)
        engine.say(audio)
        engine.runAndWait()

voz = Talk()

class time:
    @staticmethod
    def greetMe():
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            voz.speak('good morning!')

        if currentH >= 12 and currentH < 18:
            voz.speak('Good afternoon!')

        if currentH >= 18 and currentH !=0:
            voz.speak('Good night!')

class Query:
    def myCommand():
   
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            print("Escuchando...")
            r.pause_threshold =  1
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print('User: ' + query + '\n')
        
        except sr.UnknownValueError:
            voz.speak('Im sorry Sir Elizondo tries typing the command!')
            query = str(input('Command: '))

        return query


time = time()

time.greetMe()
voz.speak('onii chan, Im suuchan')
voz.speak('How can I help you?')
