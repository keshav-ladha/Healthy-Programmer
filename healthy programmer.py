from pygame import mixer
import datetime
from time import time
import pyttsx3
from plyer import notification

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    '''Setting Up Speak Function through which it will interact with the user'''
    engine.say(audio)
    engine.runAndWait()

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg}:{datetime.datetime.now()}\n")


if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    waterseconds = 3600
    eyesseconds = 2700
    exerciseseconds = 3600
    while True:
        if time() - init_water > waterseconds:
            notification.notify(
                title="WATER TIME!!!",
                message="Its Been an Hour!!!!",
                app_icon="F:\\Python\\Projects(Succesfull)\\Healthy Programmer\\watericon.ico",
                timeout=15
            )
            speak("Water drinking time..!... Enter 'drank' to stop the alarm.'")
            musiconloop("alarm.mp3", "drank")
            init_water = time()
            log_now("Drank Water At:")
        if time() - init_eyes > eyesseconds:
            notification.notify(
                title="PLEASE RELAXE YOUR EYES!!!",
                message="Its Been an Hour!!!!",
                app_icon="F:\\Python\\Projects(Succesfull)\\Healthy Programmer\\eyesicon.ico",
                timeout=15
            )
            speak("Eyes time..!... Enter 'done' to stop the alarm.'")
            musiconloop("alarm.mp3", "done")
            init_eyes = time()
            log_now("Eyes Relived At:")
        if time() - init_exercise > exerciseseconds:
            notification.notify(
                title="WAKE UP AND WALK UP!!!",
                message="Its Been an Hour!!!!",
                app_icon="F:\\Python\\Projects(Succesfull)\\Healthy Programmer\\exicon.ico",
                timeout=15
            )
            speak("Exercise time..!... Enter 'done' to stop the alarm.'")
            musiconloop("alarm.mp3", "done")
            init_exercise = time()
            log_now("Exercise At:")
