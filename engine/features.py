import os
from pipes import quote
import re
import sqlite3
import struct
import subprocess
import time
import webbrowser
from playsound3 import playsound
import eel
import pyaudio
import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import pvporcupine
import datetime
import requests
from openai import OpenAI

from engine.helper import extract_yt_term, remove_words


con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()
            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])
            elif len(results) == 0:
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing "+search_term+" on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Please specify a song or video to play on YouTube.")

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
            keyword_index=porcupine.process(keyword)
            if keyword_index>=0:
                print("hotword detected")
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is " + current_time)

def get_date():
    today = datetime.date.today().strftime("%B %d, %Y")
    speak("Today is " + today)

def get_weather():
    api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
    city = "Virar"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(url)
    weather_data = response.json()
    
    if weather_data["cod"] != "404":
        main = weather_data["main"]
        weather = weather_data["weather"][0]
        temperature_celsius = round(main["temp"] - 273.15, 2)
        weather_description = weather["description"]
        
        speak("The weather in " + city + " is " + weather_description + " with a temperature of " + str(temperature_celsius) + " degrees Celsius.")
    else:
        speak("Could not find weather information for that city.")

def chatBot(query):
    try:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=query,
            max_tokens=150
        )
        response_text = response.choices[0].text
        print(response_text)
        speak(response_text)
        return response_text
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("I'm sorry, I was unable to process your request.")
        return ""