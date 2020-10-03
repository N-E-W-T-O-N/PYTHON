#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:17:02 2019

@author: newton
"""

import speech_recognition as sr
# This module is imported so that we can  
# play the converted audio 
#from  gtts import gTTS
#print(sr.Microphone.list_microphone_names)
r=sr.Recognizer()
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

with sr.Microphone() as source:
    print("Say some melodious word")
    r.pause_threshold=1
    r.adjust_for_ambient_noise(source,duration=1) 
    audio =r.listen(source)
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    print(r.recognize_google(audio,language="hi-IN"))
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))





# The text that you want to convert to audio 
#mytext = 'Welcome to geeksforgeeks!'
  
# Language in which you want to convert 
#language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should 
#  
# have a high speed 
#tts = gTTS(x)
#tts.save('dialog.mp3')

