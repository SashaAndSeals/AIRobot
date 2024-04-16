import os
try: 
    import google.generativeai as ai
except:
    os.system("pip install google-generativeai")
    import google.generativeai as ai
try:
    import pyttsx3
except: 
    os.system("sudo apt install espeak")
    os.system("install pyttsx3")
    import pyttsx3
try:
    import speech_recognition as sr
except:
    os.system("sudo apt-get install flac")
    os.system("sudo apt-get install portaudio19-dev")
    os.system("pip install pyaudio")
    os.system("pip install SpeechRecognition")
    import speech_recognition as sr
sound = pyttsx3.init()
sound.setProperty("voice", "english")
sound.setProperty("rate", 150)
f = open("API_KEY.txt","r")
GOOGLE_API_KEY = f.read().splitlines()[0]
f.close()
ai.configure(api_key = GOOGLE_API_KEY)
model = ai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
chat.send_message("Can you write shorter answers in all future answers in this chat?")
r = sr.Recognizer()
with sr.Microphone() as m:
    while True:
        audio = r.listen(m)
        try:
            q = r.recognize_google(audio)
        except:
            continue
        print(q)
        response = chat.send_message(q).text.replace("*","")
        print(response)
        for line in response.splitlines():
            if not(line==""):
                sound.say(line)
        sound.runAndWait()


