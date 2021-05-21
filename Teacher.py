import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Student!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Student!")   

    else:
        speak("Good Evening Student!")  

    speak("I am Alexa Tell me what do you want to learn Today!! ")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open amazon' in query:
            speak("Ok going to amazon")
            webbrowser.open("https://amazon.in")

        elif 'open youtube' in query:
            speak("Ok going to youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Ok going to google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Ok going to stackoverflow")
            webbrowser.open("stackoverflow.com")  

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\Users\Ajay\AppData\Local\Programs\Microsoft VS Code\bin"
            os.startfile(codePath)

        elif 'email to adarsh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "codingwithadarsh@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Adarsh. I am not able to send this email") 

        elif 'open adarsh coding channel' in query:
            speak("Ok going to adarsh coding channel")
            webbrowser.open("https://www.youtube.com/channel/UCZMSYfG36TQTBem07bAhJfg")
            
        elif 'open white hat junior' in query:
            speak("Ok going to white hat jr")
            webbrowser.open("https://code.whitehatjr.com/s/dashboard")

        elif 'jarvis exit' in query:
            speak("ok sir goodbye have a nice day")
            exit()
        