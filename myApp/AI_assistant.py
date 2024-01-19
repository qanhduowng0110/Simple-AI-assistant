import speech_recognition
import pyttsx3
from datetime import date, datetime
import pyowm
import webbrowser

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""

def weather_forecast(city_input):
    api_key = pyowm.OWM('xxx') #Enter API Key
    weather_bot = api_key.weather_manager()
    weather_place = weather_bot.weather_at_place(city_input)
    the_weather = weather_place.weather
    temps = the_weather.temperature('celsius')
    avr_temp = temps['temp']
    status = the_weather.detailed_status
    humid = the_weather.humidity
    robot_brain = "The weather in "+ str(city_input) +" is: " + str(status) +", the temperature is: " + str(avr_temp) +" Celsius, the humidity is: " + str(humid) + "%."
    return robot_brain
    
while True:
    with speech_recognition.Microphone() as mic:
        robot_ear.adjust_for_ambient_noise(mic)
        print("I'm listening...")
        audio = robot_ear.record(mic,duration=5)
    print("...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("Lien: " + you)

    if you == "":
        robot_brain = "I can't hear you"
    elif "hello" in you:
        robot_brain = "Hello Lien, my love!"
    elif you == "how are you":
        robot_brain = "I'm fine, thank you. And you?"
    elif you == "how old are you":
        robot_brain = "I don't know, my father neither!"
    elif "today" in you:
        today = date.today()
        day = today.strftime("%B %d, %Y")
        robot_brain = "Today is " + day
    elif "time" in you:
        time = datetime.now()
        robot_brain = time.strftime("It's %H:%M")
    elif "I love you" in you:
        robot_brain = "I love you too! Moahhhh"
    elif "open Google" in you:
        webbrowser.open('https://www.google.com/')
        robot_brain = "Google Chrome opened!"
    elif "open Youtube" in you:
        webbrowser.open('https://www.youtube.com//')
        robot_brain = "Youtube opened!"
    elif "open Netflix" in you:
        webbrowser.open('https://www.netflix.com/vn/')
        robot_brain = "Netflix opened!"
    elif "weather" in you:
        with speech_recognition.Microphone() as mic:
            robot_ear.adjust_for_ambient_noise(mic)
            question ="Where do you want to know the weather?"
            print("Quang Anh: " + question)
            robot_mouth.say(question)
            robot_mouth.runAndWait()
            audio1 = robot_ear.record(mic, duration=5)
            print("...")
        try:
            answer = robot_ear.recognize_google(audio1)
        except:
            answer = ""
        print("Lien: " + answer)
        if answer == "":
            robot_brain = "I can't hear you"
        else:
            try:
                robot_brain = weather_forecast(answer)
            except:
                robot_brain = "I don't know the city you mentioned!"
            
    elif "bye" in you or "turn off" in you:
        robot_brain = "Goodbye, See ya!"
        print("Quang Anh: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "Ask something different!"

    print("Quang Anh: " + robot_brain)

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
