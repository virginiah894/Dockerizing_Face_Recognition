import speech_recognition as sr
from time import ctime
import webbrowser
r= sr.Recognizer()
def recording_audio(ask=False):
    with sr.Microphone() as mainvoice:
        if ask :
            print(ask)
        
        audio = r.listen(mainvoice)
        voice_info = ''
        try:
            voice_info = r.recognize_google(audio)
            print(voice_info)
        except sr.UnknownValueError:
            print('Sorry I did not get that')
        except sr.RequestError:
            print('Sorry, the speech service is down')
        return voice_info

def response(voice_info):
    if 'What is your name' in voice_info:

        print('My name is Sirilol')
    if 'What time is it' in voice_info:
        print(ctime())
    if 'search' in voice_info:
        search =recording_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search) 

print('How can I assist you?')
voice_info = recording_audio()
response(voice_info)
response(voice_info)