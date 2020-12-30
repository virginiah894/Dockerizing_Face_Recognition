import speech_recognition as sr
r= sr.Recognizer()
def recording_audio():
    with sr.Microphone() as mainvoice:
        
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
print('How can I assist you?')
voice_info = recording_audio()
