from plyer import notification
import time
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    '''Setting Up Speak Function through which it will interact with the user'''
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':

    notification.notify(
        title ="WATER TIME!!!",
        message = "Its Been an Hour!!!!",
        app_icon = "F:\\Python\\Projects(Succesfull)\\Healthy Programmer\\watericon.ico",
        timeout = 15
    )
    speak("water time")