from winreg import QueryReflectionKey
import pyttsx3.drivers
import speech_recognition as sr 
from datetime import datetime

import webbrowser
import os
import spotipy

import requests
import subprocess
import time

from functions.online_ops import find_my_ip, get_latest_news, get_random_joke,  get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from pprint import pprint

import json
import webbrowser

import subprocess
USERNAME = "Manoj"
BOTNAME = "Mister Bro"

username = 'Your spotify username'
clientID = 'Your client ID goes here'
clientSecret = 'Your client secret goes here'
redirect_uri = 'https://google.com/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
print(json.dumps(user_name, sort_keys=True, indent=4))
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
engine = pyttsx3.init()
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

from datetime import datetime
def wishMe():
    hour = datetime.now().hour
    if (hour >= 00) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 24):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}.")

import speech_recognition as sr
from random import choice


def takeCommand():
   

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("☆ ☆ ☆ ☆ Listening ☆ ☆ ☆ ☆")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='EN-in')
        print(f"User said: {query}\n")

    except Exception as e:
   
        print("Say that again please...")  
        return "None"
    return query


    
def takeCommandk():
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='KN-in')
        print(f"User said: {query}\n")

    except Exception as e:
      
        print("Say that again please...")  
        return "None"
    return query









    
    
    
def ConversationFlow():
  speak("you have selected your language as English")
  permission = takeCommand().lower()
  if "hey bro" in permission:
    speak("What can i do for you?")
   
    while True:

     
        query = takeCommand().lower()
        if 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen .')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia')
            search_query = takeCommand().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen ")
            print(results)
        
        elif 'joke' in query:
            speak(f"Hope you like this one {USERNAME}")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen ")
            pprint(joke)

       
        elif 'read out latest news' in query:
            speak(f"I'm reading out the latest news headlines {USERNAME}")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen.")
            print(*get_latest_news(), sep='\n')

        
        elif ' youtube' in query:
            speak('What do you want to play on Youtube?')
            video = takeCommand().lower()
            play_on_youtube(video)

        elif ' google' in query:
            speak('What do you want to search on Google?')
            query = takeCommand().lower()
            search_on_google(query)

        elif "whatsapp message" in query:
            speak('On what number should I send the message ?')
            number = input("Enter the number: ")
            speak("What is the message ?")
            message = takeCommand().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message ")
           


        elif "send an email" in query:
            speak("On what email address do I need to send? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject ?")
            subject = takeCommand().lower()
            speak("What is the message ?")
            message = takeCommand().lower()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email .")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error log")

        elif 'times of india' in query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Have a look!!')
                time.sleep(6)

        
        elif'open youtube' in query:
            webbrowser.open("youtube.com")
 

        elif 'open google' in query:
                webbrowser.open("google.com")

        elif 'open instagram' in query:
                webbrowser.open("instagram.com")  

        elif 'open facebook' in query:
                webbrowser.open("facebook.com")  


        elif 'play song from my library' in query:
                music_dir = 'F:\\song'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
               now = datetime.now()

               current_time1 = now.strftime("%H:%M:%S")
               speak(f"The time is {current_time1}")
            
        elif 'how are you' in query:
                speak("Im Absolutely Fine Manoj!! How about you?")

        elif 'hey' in query or 'hello' in query:
                speak("Hey bro!! whatsuppp!!!")  
    
        elif 'you are just amazing' in query:
                speak("Thankyou manoj , so you are!")
        
        elif 'play some song' in query:
                speak("Which song shall I play for you??")
                if True:
                 search_song = takeCommand()
                results = spotifyObject.search(search_song, 1, 0, "track")
                songs_dict = results['tracks']
                song_items = songs_dict['items']
                song = song_items[0]['external_urls']['spotify']
                webbrowser.open(song)
        
                print('Song has opened in your browser.')
            
        
            
        elif 'i am good to' in query:
                speak("That's Fantastic")


        elif 'open code' in query:
                codePath = "C:\\Users\\hegde\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
        elif 'open whatsapp' in query:
                    codePath="C:\\Users\\hegde\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                    os.startfile(codePath)
            
        elif 'who made you' in query or 'who created you' in query or "who discovered you" in query:
                    speak("I was built by Manoj and Manvitha")
          
        elif 'nothing'  in query or "no thanks" in query :
                    speak("i will take my leave now , you  can invoke me whenever you need me")
        
        elif "weather  for other city" in query or "can i get  weather  for other city" in query or "can i get  weather  of other place" in query:
                api_key="6196b067ceef529a5511d6ce3bc352b8"
                speak("whats the city name")
                city_name=takeCommand()
                res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric").json()
                weather = res["weather"][0]["description"]
                temperature = res["main"]["temp"]
                feels_like = res["main"]["feels_like"]
                speak(f"The current temperature in {city_name} is {temperature}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                speak("For your convenience, I am printing it on the screen.")
                print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

                
                

        elif "goodbye" in query or "okbye" in query or "stop" in query:
                    hour = datetime.now().hour
                    if (hour >= 23) and (hour < 6):
                     speak("i will take my leave now , you  can invoke me whenever you need me. Good night ,Sleep Tight!!!")
                     break
                    else :
                        (hour >= 6) and (hour < 23)
                        speak("i will take my leave now , you  can invoke me whenever you need me. Have a wonderfull day!!")
                        break
        elif "log off" in query or "sign out" in query:
                    speak("Ok , your pc will log off in some time ,make sure you exit from all applications")
                    subprocess.call(["shutdown", "/l"])
                    hour = datetime.now().hour
                    if (hour >= 23) and (hour < 6):
                     speak("Good night ,Sleep Tight!!!")
                     break
                    else :
                        (hour >= 6) and (hour < 23)
                        speak("Have a wonderfull day!! call me back soon!!")
                        break
                    time.sleep(10)
            
        elif "hibernate" in query :
                    speak("Ok , your pc will hibernate  in some time , make sure you exit from all applications")
                    subprocess.call(["shutdown", "/h"])
                    hour = datetime.now().hour
                    if (hour >= 23) and (hour < 6):
                     speak("Good night ,Sleep Tight!!!")
                     break
                    else :
                        (hour >= 6) and (hour < 23)
                        speak("Have a wonderfull day!! call me back soon!!")
                        break
                    time.sleep(10)
                
                    

        elif "shutdown" in query:
                    speak("Ok , your pc will shutdown in one minute, make sure you exit from all applications")
                    subprocess.call(["shutdown", "/s"])
                    hour = datetime.now().hour
                    if (hour >= 23) and (hour < 6):
                     speak("Good night ,Sleep Tight!!!")
                     break
                    else :
                        (hour >= 6) and (hour < 23)
                        speak("Have a wonderfull day!! call me back soon!!")
                        break
                    time.sleep(10)
                 

        
                    
        elif 'the weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

if __name__ == "__main__":
  
 
    speak(" speak your password")
    permission=takeCommand()
    if "2023" in permission:
        speak("Welcome back")
        wishMe()   
        ConversationFlow() 
    
    else:
        speak("Access Denied")
        exit
