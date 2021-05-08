#before using this u must ensure that u have a mic of good quality.
#u can modify code according to u , but this the way i made it.
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import pyjokes
import wolframalpha
import json
import pyaudio
import requests
import pywhatkit
import PyPDF2
print('Loading your AI personal assistant - Jarvis')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...") 
        statement=r.recognize_google(audio,language='en-in')
        print(f"user said:{statement}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return statement
speak("Loading your AI personal assistant Jarvis")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or 'bye' in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Jarvis is shutting down,Good bye')
            print('your personal assistant Jarvis is shutting down,Good bye')
            break


        if 'hello jarvis' in statement:
            speak('Hi Master! Nice to meet you!!')
        
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            speak("youtube - open now!")
            webbrowser.open_new_tab("https://www.youtube.com")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome - open now!")
            time.sleep(5)

        elif 'open gmail' in statement:
            speak("Google Mail - open now!")
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
            time.sleep(5)
        
        elif 'open vedantu' in statement:
            speak("Vedantu - open now!")  
            webbrowser.open_new_tab("https://www.vedantu.com/")          
            time.sleep(5)

        elif "weather" in statement:
            api_key="31f7xxxxxxxxxxxxxxxxx" #get your api id from the site "https://api.openweathermap.org/"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Jarvis - your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Deku!!")
            print("I was built by Deku!!")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        

        elif 'search'  in statement:
            speak('Searching!!!')
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="JGxxxxxxxxxxx" #get api id from site of wolframalpha -(https://www.wolframalpha.com/)
            client = wolframalpha.Client('JGxxxxxxxxxxxx')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


       
        elif "log off" in statement or "sign out" in statement:
             speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
             subprocess.call(["shutdown", "/l"])
      
        
        
        elif 'open music' in statement:
            Resso = "C:\\Users\\Deepak Kumar\\AppData\\Local\\Programs\\Resso\\Resso.exe"
            os.startfile(Resso)    
        
        elif 'open screen recorder' in statement:
            fp = "C:\\Program Files\\Free Cam 8\\freecam.exe"
            os.startfile(fp) 
        
        elif 'open telegram' in statement:
            tp="C:\\Telegram Desktop\\Telegram.exe"
            os.startfile(tp) 
        
        elif 'open snipping tool' in statement:
            st="%windir%\\system32\\SnippingTool.exe"
            os.startfile(st)
       
        elif 'open code' in statement:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    
       
        
        elif 'play' in statement:
            song = statement.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        
        
        elif 'joke' in statement:
            speak(pyjokes.get_joke())
            
        
        elif 'open amazon' in statement:
            speak('Amazon.com - open now !')
            webbrowser.open_new_tab('amazon.in')

        elif 'open instagram' in statement:
            speak('Instagram - open now !')
            webbrowser.open_new_tab('https://www.instagram.com/')  
        
        elif 'quiet' in statement or 'shant ho ja' in statement:
            speak('Okay master , shutting my mouth......hehehehehe!! ')
            input('Press Enter to unmute.......')
      #the below program is to just use jarvis as an audiobook if u r too lazy to read................xd 
      #use pdf whatever u want , just replace it in the code and also the pdf should be where u created jarvis.py. 
        elif 'ebook reader' in statement:
            speak('Switching to ebook reader mode!')
            book = open('c1.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            speaker = pyttsx3.init()
            for num in range(1, pages):
                page = pdfReader.getPage(num)
                text = page.extractText()
                speaker.setProperty('rate', 145)
                speaker.say(text)
                speaker.runAndWait()

time.sleep(3)            
                         
