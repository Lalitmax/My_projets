import datetime
import pyttsx3
import smtplib
import speech_recognition as sr
import webbrowser
import os
import subprocess
import random
import math
import wikipedia
import pywhatkit as wtp

# create date today
date=datetime.datetime.now()
date=str(date)
date=date.split()
date=date[0]

# create random number
r=random.randint(0,7)


# Create a engine
engine=pyttsx3.init()

# set voice of male or female
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# set voice rate
rate=engine.getProperty('rate')
engine.setProperty('rate',178)

# create current datetime
cur_time=datetime.datetime.now().strftime('%H:%M:%S')

# take only hour
hour=int(datetime.datetime.now().hour)
minut=int(datetime.datetime.now().minute)

# whether
import requests



def speak(text):
    engine.say(text)
    engine.runAndWait()



def wishme():
    if hour>=0 and hour<=12:
        print('good morning sir,\n I am maxi, \n  how may i help you')
        speak('good morning sir, I am maxi, \n  how may i help you')


    elif hour>=12 and hour<=18:
        print('good afternoon sir, \nI am maxi,  how may i help you')
        speak('good afternoon sir, I am maxi,  how may i help you')

    else:
        print('good evening sir,\n I am maxi,  how may i help you')
        speak('good evening sir, I am maxi,  how may i help you')

def sendmail(mail):
    Gmail=None # enter your Gmail
    Psw=None  # enter password
    Port=587 # this is Gmail port number
    To_send=None # which person you want to send mail

    Srvr=smtplib.SMTP('smtp.gmail.com',Port)
    Srvr.starttls()
    Srvr.login(Gmail,Psw)
    Srvr.sendmail(Gmail,To_send,mail)
    print('Email successfully sent')


 
#  take command for do anything   
def command():
    r=sr.Recognizer()
    with sr.Microphone() as mic:
        print('listening...')
        r.pause_threshold=2
        audio=r.listen(mic)

    try:
        print('recognizing...')
        text=r.recognize_google(audio)
        text=text.lower()
    except Exception as e:
        print(e)
        print("sorry, i don't understand")
        speak("sorry, i don't understand")
        return 'none'
    return text

def doooo(text):
    if text in ['what is the time', "what's the time",'is time','time now',]:
        if hour>=12:
            print(hour,":",minut,'PM')
            speak(str(hour)+":"+str(minut)+'PM')
        else:
            print(hour,":",minut,'AM')
            speak(str(hour)+":"+str(minut)+'Am')

    elif ("weather") in text:
        

        t=text.split()
        
       
        
        city_name=t[-1]
        data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=882bef32516f8990d82b762cae54604c").json()

        weather="weather is, "+data["weather"][0]["main"]
        Temp="temperature is, "+str(int(data["main"]["temp"]-273.5))+" degree Celsius"
        description='description is, '+data["weather"][0]['description']
        name="Name, "+data["name"]+","
        code="Code is, "+str(data["cod"])



        print(weather)
        print(Temp)
        print(description)
        print(name)
        print(code)
        speak(weather)
        speak(Temp+description)
        speak(name+code)
       
        


    elif "temperature" in text:
        t=text.split()
        
        city_name=t[-1]
        data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=882bef32516f8990d82b762cae54604c").json()

       
        Temp="The temperature is, "+str(int(data["main"]["temp"]-272))+" degree Celsius,"
        name="in, "+data["name"]
        print(Temp)
        print(name)
        speak(Temp+name)
        

        

    elif text in ['send mail to lalit','send email to lalit','send mail lalit']:
        print('what do you want to write.. ')
        mail=command()
        sendmail(mail)
    elif text in ["exit","quit"]:
        exit()
    elif text in ["play video","play song","video"]:
        webbrowser.open("www.youtube.com")
        exit()
    elif text in ['open google','google open']:
        webbrowser.open('www.google.com')
        speak('opening google')
        exit()
    elif text in ['open youtube','youtube open']:
        webbrowser.open('www.youtube.com')
        speak('opening youtube')
        exit()
    elif text in ['open telegram','telegram open']:
        webbrowser.open('www.telegram.com')
        speak('opening')
        exit()
    elif text in ['open whatsapp','whatsapp open']:
        webbrowser.open('www.whatsap.com')
        speak('opening whatsapp')
        exit()
    elif text in ['open gmail','gmail open']:
        webbrowser.open('www.gmail.com')
        speak('opening gmail')
        exit()
    elif text in ['open github','github open']:
        webbrowser.open('www.github.com')
        speak('opening github')
        exit()
    elif text in ['open linkedin','linkedin open']:
        webbrowser.open('www.linkedin.com')
        speak('opening linkedin')
        exit()
    elif text in ['open instagram','instagram open']:
        webbrowser.open('www.instagram.com')
        speak('opening insta gram')
        exit()
    elif text in ['open music','play music','music open','music play']:
        os.startfile("wmplayer")
        exit()
       
    elif text in ["open documents","documents open"]:
        os.startfile("Documents")
        speak("opening documents")
        exit()
    elif text in ["open wordpad","wordpad open"]:
        os.startfile("wordpad")
        speak("opening wordpad")
        exit()
    elif text in ["open ms paint","ms paint open","open paint","paint open","open microsoft paint"]:
        os.startfile("mspaint")
        speak("opening ms paint")
        exit()
    elif text in ["open calculator","calculator open"]:
        os.startfile("calc")
        speak("opening calculator")
        exit()
    elif text in ["open task manager","task manager open"]:
        os.startfile("taskmgr")
        speak("opening task manager")
        exit()
    elif text in ["open notepad","notepad open"]:
        os.startfile("notepad")
        speak("opening notepad")
        exit()
    elif text in ["open c drive","open cdrive","cdrive open","c drive open"]:
        os.startfile("c:")
        speak("opening c drive")
        exit()
    elif text in ["open settings","settings open","open setting","setting open"]:
        os.startfile("dpiscaling")
        speak("opening settings")
        exit()
    elif text in ["open disk management","disk management open"]:
        os.startfile("diskmgmt.msc")
        speak("opening disk management")
        exit()
    elif text in ["open this pc","this pc open"]:
        os.startfile('\"')
        speak("opening this pc")
        exit()
    elif text in ["open control Panel","control Panel open"]:
        os.startfile("control")
        speak("opening control Panel")
        exit()
    elif text in ["open character map", "character map open"]:
        os.startfile('charmap')
        speak("opening character map")
        exit()
    elif text in ["open keyboard","keyboard open"]:
        os.startfile("osk")
        exit()
    elif text in ["open file explorer","file explorer open"]:
        os.startfile("explorer")
        speak("opening file explorer")
        exit()
    elif text in ["shutdown","shut down","shutdown laptop","laptop shut down","laptop shutdown","shut down laptop","shutdown computer","shut down computer","computer shutdown","computer shut down"]:
        os.startfile("shutdown")
        speak("shutdown")
        exit()
    elif text in ["restart","restart laptop","laptop restart","computer restart","restart computer"]:
        os.startfile("shutdown -r")
        exit()
    elif text in ["open powershell","powershell open"]:
        os.startfile("powershell")
        speak("opening powershell")
        exit()

    elif text in ["open excel","excel open"]:
        os.startfile("excel")
        exit()
    elif text in ["open chrome","chrome open","open google chrome","google chrome open"]:
        os.startfile("chrome")
        speak("opening chrome")
        exit()
    elif text in ["open brave","brave open"]:
        os.startfile('Brave')
        speak("opening brave")
        exit()
    elif text in ["open firefox","firefox open"]:
        os.startfile('firefox')
        speak("opening firefox")
        exit()
    elif text in ["open cmd","cmd open"]:
        os.startfile("cmd")
        exit()
    elif text in ["open code","code open"]:
        os.startfile("code")
        exit()
    elif text in ["open microsoft edge","Microsoft edge open"]:
        os.startfile("msedge")
        speak("opening microsoft edge")
        exit()
    elif text in ["open photoshop","photoshop open"]:
        os.startfile("photoshop")
        speak("opening photoshop")
        exit()
    elif text in ["open outlook","outlook open"]:
        os.startfile("outlook")
        speak("opening outlook")
        exit()
    elif text in ["open powerpoint","powerpoint open"]:
        os.startfile("powerpnt")
        speak("opening powerpoint")
        exit()
    elif text in ['how are you']:
        print('i am fine.\ntell me how may i help you')
        speak('i am fine, tell me how may i help you')
    elif text in ['what is your name',"what's your name"]:
        print('''well, my name's maxy" \ni wish that everyone\nhad a nickname as cool as mine\nso plz keep small and sort your name  ''')
        speak('''well, my name is maxy, i wish that everyone had a nickname as cool as mine, so plz keep small your name  ''')
    elif text in ['are you marry me',"will you marry me"]:
        print("this is one of things \nwe'd both have to agree\non i'd prefer to keep \nour friendship as it is.")
        speak("this is one of things, we'd both have to agree on i'd prefer to keep  our friendship as it is. ")
    elif text in ['what can you do for me']:
        print("i can do all the work \n which is in my might")
        speak("i can do all the work, which is in my might")
    elif text in ["do something for me"]:
        print("Ask me any problem \ni will try to solve it \nfor you")
        speak("Ask me any problem, i will try to solve it for you")
    elif text in ['date',"what's date","what is date","date","what's the date today","today date","today's date"]:
        print(date)
        speak(date)
    elif text in ["tell me some jokes","tell some jokes","tell me some joke","kucch joke sunao","kuchh jokes sunao",'tell me joke ','tell me jokes']:
        print("Air hostess asked lalu \nPrasad yadav. \nSir are you vegetarian or \nNon vegetarian \nLalu said I am indian \nAir hostess said okay, \nAre you shakahari or mansahari \nLalu said hat sasuri I am Bihari")
        speak("Air hostess asked lalu Prasad yadav. Sir are you vegetarian or Non vegetarian, Lalu said I am indian. Air hostess said okay, Are you shakahari or mansahari, Lalu said hat sasuri I am Bihari")
    elif "wikipedia" in text:
        result=wikipedia.summary(text,sentences=2)
        print(result)
        speak(result)
    elif "print table of" in text:
        nu=text.split()
        nu=int(nu[-1])
        for i in range(1,11):
            print(i*nu,end=" ")
        print()
        exit()
    elif "on youtube" in text:
        try:
            wtp.playonyt(text)
            speak('playing')
        except:
            speak("network Error Occurred ")
        
    elif "how to make" in text:
        try:
            wtp.playonyt(text)
            speak("playing")
        except:
            speak("network Error Occurred ")
        
        
    elif text in ["do you know chitkara university"]:
        print("yes i know chitkara university, \nit is best private university in punjab ")
        speak("yes i know chitkara university, it is best private university in punjab ")
    elif  "factorial" in text:

        fact=str(text)
        fact=fact.split()
        fact=int(fact[-1])
       
        fact=math.factorial(fact)
        print(fact)
        speak(fact)
    elif text in ["open coding ninjas","coding ninjas open","coding ninjas"]:
        webbrowser.open('https://www.codingninjas.com')
        exit()
    elif text in ["open vs code","open visual studio code","vs code open","visual studio code open"]:
        vs_pasth="C:\\Users\\lalit\\OneDrive\\Desktop\\Visual Studio Code.lnk"
        webbrowser.open(vs_pasth)
        exit()

    
    else:
        print("sorry i don't understand")
        speak("sorry i don't understand")









if __name__ == '__main__':
    while(1):
       text= command()

       doooo(text)
