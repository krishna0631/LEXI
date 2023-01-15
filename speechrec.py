from ast import While
import traceback
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyautogui
import datetime
import wikipedia
import pyjokes
import subprocess
import webbrowser
import wolframalpha
import json
import requests
import winshell
import ctypes
from urllib import request
import urlopen


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.say('Hello I am Lexi!, your Virtual personal Assistant')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = "Krishna"
    try:
        with sr.Microphone() as source:
            print('Listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command

def run_lexi():
    command = take_command()
    try :
        if 'play' in command:
            song = command.replace('play','')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'name' in command:
            talk('My Name is LEXI')
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Now the Time is ' + time)
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%d %B %Y')
            print(date)
            talk('Today is ' + date)
        # elif 'whatsapp' in command:
        #     talk('Opening Whatsapp')
        #     pywhatkit.sendwhatmsg('+916309673083','Hello',12,25)
        elif 'who' in command:
            info = command.replace('who', '')
            information = wikipedia.summary(info, 1)
            print(information)
            talk(information)
        # elif 'who is' in command:
        #     info = command.replace('who is', '')
        #     information = wikipedia.summary(info, 1)
        #     print(information)
        #     talk(information)
        elif 'what' in command:
            info = command.replace('what', '')
            information = wikipedia.summary(info, 2)
            print(information)
            talk(information)
        elif 'where is' in command:
            query = command.replace("where is", "")
            location = query
            talk("User asked to Locate")
            talk(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
        elif 'dictionary' in command:
            query = command.replace('dictionary', '')
            talk('Searching for' + query)
            webbrowser.open('https://www.dictionary.com/browse/' + query)
        elif 'directions' in command:
            query = command.replace('directions', '')
            talk('Searching for' + query)
            webbrowser.open('https://www.google.com/maps/dir/?api=1&destination=' + query)
        # elif 'screenshot' in command:
        #     talk('Taking Screen Shot')
        #     myScreenshot = pyautogui.screenshot()
        #     myScreenshot.save(r'C:\Users\Krishna\Desktop\ScreenShot.png')
        elif 'stop' in command:
            talk('Ok Bye')
            exit()
        elif 'weather' in command:
            talk('Checking Weather')
            webbrowser.open('https://www.google.com/search?q=weather')
        # elif 'open' in command:
        #     query = command.replace('open', '')
        #     talk('Opening' + query)
        #     webbrowser.open('https://www.' + query + '.com')
        elif 'who is' in command:
            query = command.replace('who is', '')
            talk('Searching for' + query)
            webbrowser.open('https://www.google.com/search?q=' + query)
        elif "restart" in command:
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in command or "sleep" in command:
            talk("Hibernating")
            subprocess.call("shutdown / h")
        elif "Shutdown" in command or "sign out" in command:
            talk("Make sure all the application are closed before sign-out")
            # time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        elif 'lock window' in command:
            talk("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in command:
            talk("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        elif 'empty recycle bin' in command:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            talk("Recycle Bin Recycled")
        # elif "what is" in command or "who is" in command:
        #     # Use the same API key
        #     # that we have generated earlier
        #     client = wolframalpha.Client("API_ID")
        #     res = client.query(command)
        #     try:
        #         print(next(res.results).text)
        #         talk(next(res.results).text)
        #     except StopIteration:
        #         print("No results")
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        # elif 'what are the latest news' in command or 'news' in command or 'what is the news' in command:
        #     try:
        #         jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey
        #         =\\times of India Api key\\''')
        #         data = json.load(jsonObj)
        #         i = 1
        #         talk('here are some top news from the times of india')
        #         print('''=============== TIMES OF INDIA ============''' + '\n')
        #         for item in data['articles']:
        #             print(str(i) + '. ' + item['title'] + '\n')
        #             print(item['description'] + '\n')
        #         talk(str(i) + '. ' + item['title'] + '\n')
        #         i += 1
        #     except Exception as e:
        #         print(str(e))
        elif "write a note" in command:
            talk("What should i write, sir")
            note = take_command()
            file = open('notes.txt', 'w')
            talk("Sir, Should i include date and time")
            snfm = take_command()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
    #     elif "show me the note" in command:
    #         talk("Showing Notes")
    #         file = open("jarvis.txt", "r")
    #         print(file.read())
    #         talk(file.read(6))
    #     elif "weather" in command:
    #         # Google Open weather website
    #         # to get API of Open weather
    #         api_key = "Api key"
    #         base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
    #         talk(" City name ")
    #         print("City name : ")
    #         city_name = take_command()
    #         complete_url = base_url + "appid =" + api_key + "&q =" + city_name
    #         response = requests.get(complete_url)
    #         x = response.json()
    #         if x["cod"] != "404":
    #             y = x["main"]
    #             current_temperature = y["temp"]
    #             current_pressure = y["pressure"]
    #             current_humidiy = y["humidity"]
    #             z = x["weather"]
    #             weather_description = z[0]["description"]
    #             print(" Temperature (in kelvin unit) = " + str(
    #             current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
    #             current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(
    #             weather_description))
    #     else:
    #         # talk('Please say the command again.')
    #         print(command)
    except:
         print(f"Something went wrong: {traceback.format_exc()}")

    # run_lexi()


run_lexi()

