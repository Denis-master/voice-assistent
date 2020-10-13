import speech_recognition as sr
import os
import webbrowser

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("распознавание речи")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source,phrase_time_limit=3)
    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print("Распознано: " + zadanie)
    except sr.UnknownValueError:
        print("не распознано")
        zadanie = command()
    return zadanie
def makeSomething(command):
    if command=='андрей':
        os.system("mpv start.mp3")
        os.system("python3 speech_ai1.py")
    if "открой на ivi" in command:
        adress = command.replace('открой на ivi','').strip()

        webbrowser.open('https://www.ivi.ru/search/?q='+adress)

        adress=''
    if "открой в браузере" in command:
        adress = command.replace('открой в браузере','').strip()
        webbrowser.open('https://www.google.com/search?q='+adress)
        adress=''
    if "закрой браузер" in command:
        os.system("killall chromium-browse")
 
while True:
    makeSomething(command())