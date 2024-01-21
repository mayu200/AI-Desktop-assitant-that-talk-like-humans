import pyttsx3
import speech_recognition 
from Searchnow import searchGoogle
from Searchnow import searchYoutube
from Searchnow import searchWikipedia
import pyaudio
import os 
import requests
from bs4 import BeautifulSoup
import datetime
import random
import pygame.mixer as mixer
import webbrowser
import pyautogui
import keyboard



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


#Greet Me Function
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break 
#Conversation with AI            
                elif "hello" in query:
                    speak("Hello sir,how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how r u?" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")

#play music
                
                elif "play music" in query:
                    music_dir = r"C:\Users\Mayuri\Desktop\Phase 1 (major project)\Music"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir,songs[0]))
                    

#News function
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()


#Youtube controls
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmuted")
                elif "full screen" in query:
                    pyautogui.press("f")
                    speak("going full screen")
                elif "exit full screen" in query:
                    pyautogui.press("F")
                    speak("exiting full screen")
                elif "go forward" in query:
                    pyautogui.press("l")
                    speak("going forward 10 second")
                elif "go back" in query:
                    pyautogui.press("j")
                    speak("going back 10 seconds")
                elif "increase" in query:
                    pyautogui.hotkey('shift','.')
                    speak("playback speed incresing") 
                elif "decrease" in query:
                    pyautogui.hotkey('shift',',')
                    speak("playback speed decresing")  
                elif "next video" in query:
                    pyautogui.hotkey('shift','n')
                    speak("playing next video")
                    
#Alarm

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")


                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                


#Open and Close apps/websites 
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

#Searching from WEB(Google,YouTube, Wiki)
                elif "google" in query:
                    from Searchnow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from Searchnow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from Searchnow import searchWikipedia
                    searchWikipedia(query)

#Automating Temperature

                elif "temperature" in query:
                    search = "temperature in Maharashtra"
                    url =f"https://www.google.co.in/search?q={search}" 
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text       
                    speak(f"current{search} is {temp}")

 #Automating Time               
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

#Remember function
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("Vikram","")
                    speak("You told me"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me " + remember.read()) 




                    