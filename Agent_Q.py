'''
    python 3.6.2
    
    ## Agent Q ##

    Why ?
    Being a James bond fan and python lover, I always thought of simplfying my work.

    Google Speech Recognition and Windows 10 native speaker.

    Users - To use Agent Q, you must have atleast windows 10 and install the below modules by using pip install.

    Developer - Most of the things are hard coded as this is not AI, so there certain keywords on which Q works. For timetable either say today or
    the day of which you require Time Table. Most probably it will tell you today TimeTable if it doen't understand.

    NOTE: Suggestion's are Welcome.

'''

from tkinter import *
from tkinter import ttk
import webbrowser
import speech_recognition as sr
from pygame import mixer
import win32com.client as wincl
import datetime

speak = wincl.Dispatch("SAPI.SpVoice")

root = Tk()
root.title('Agent Q')
root.iconbitmap('agentico.ico')

style = ttk.Style()
style.theme_use('winnative')

photo = PhotoImage(file='microphone1.png').subsample(35,45)

label1 = ttk.Label(root, text='Query:')
label1.grid(row=0, column=0)
entry1 = ttk.Entry(root, width=40)
entry1.grid(row=0, column=1, columnspan=4)

btn2 = StringVar()

#
# Time Table ECE B batch15
#
TimeTable = {
    'Monday':{
        10:'Communication',
        11:'Management',
        12:'Electromagnetic Theory',
        14:'LIC'
        },
    'Tuesday':{
        11:'Eletromagnetic Theory'
        },
    'Wednesday':{
        9:'DS Lab',
        11:'Management',
        12:'Design Class',
        14:'Linear Intergrated'
        },
    'Thursday':{
        11:'Communication',
        12:'Design Class',
        14:'Lab View Lab'
        },
    'Friday':{
        9:'Communication',
        10:'Electromagnetic Theory',
        11:'Management Class',
        14:'Linear Integrated Circuit',
        15:'Design Lab'
        }
    }

def ScheduleTT(message):
    current_time = datetime.datetime.now()
    day = current_time.strftime("%A")
    
    if day == message or message == 'today':
        s = 'today'
    else:
        s = 'on'+message

    message = message.lower()

    if(message == 'monday'):
        message = 'Monday'
    elif(message == 'tuesday'):
        message = 'Tuesday'
    elif(message == 'wednesday'):
        message = 'Wednesday'
    elif(message == 'thursday'):
        message = 'Thursday'
    elif(message == 'friday'):
        message = 'Friday'
    else:
        if(day == 'Saturday' or day == 'Sunday'):
            speak.Speak("You don't have any class sir !")
            return;
        else:
            message = day
            s = 'today'

    if len(TimeTable[message].keys()) > 3:
        speak.Speak('You look busy'+s)
    else:
        speak.Speak("Your Timetable looks easy"+s)
    
    for i in TimeTable[message].keys():
        speak.Speak('At'+str(i)+TimeTable[message][i])

    speak.Speak("That's all sir")

def callback():
    
    if btn2.get() == 'google' and entry1.get() != '':
        webbrowser.open('http://google.com/search?q='+entry1.get())
        
    elif btn2.get() == 'duck' and entry1.get() != '':
        webbrowser.open('http://duckduckgo.com/?q='+entry1.get())

    elif btn2.get() == 'schedule' and entry1.get() != '':
        ScheduleTT(entry1.get())

    elif btn2.get() == 'youtube' and entry1.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())

    else:
        pass

def get(event):

    if btn2.get() == 'google' and entry1.get() != '':
        webbrowser.open('http://google.com/search?q='+entry1.get())
        
    elif btn2.get() == 'duck' and entry1.get() != '':
        webbrowser.open('http://duckduckgo.com/?q='+entry1.get())

    elif btn2.get() == 'schedule' and entry1.get() != '':
        ScheduleTT(entry1.get())

    elif btn2.get() == 'youtube' and entry1.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())

    else:
        pass

def buttonClick():

    speak.Speak('Listening to you sir !')
    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

    with sr.Microphone() as source:

        try:

            audio = r.listen(source, timeout=5)
            message = str(r.recognize_google(audio))
            entry1.focus()
            entry1.delete(0, END)
            entry1.insert(0, message)

            if btn2.get() == 'google':
                webbrowser.open('http://google.com/search?q='+message)
        
            elif btn2.get() == 'duck':
                webbrowser.open('http://duckduckgo.com/?q='+message)

            elif btn2.get() == 'schedule':
                ScheduleTT(message)
                
            elif btn2.get() == 'youtube':
                webbrowser.open('https://www.youtube.com/results?search_query='+message)

            else:
                pass

        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')

        except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition Service')

        else:
            pass    

entry1.bind('<Return>', get)

MyButton1 = ttk.Button(root, text='Search', width=10, command=callback)
MyButton1.grid(row=0, column=6)

MyButton2 = ttk.Radiobutton(root, text='Google', value='google', variable=btn2)
MyButton2.grid(row=1, column=1, sticky=W)

MyButton3 = ttk.Radiobutton(root, text='Duck', value='duck', variable=btn2)
MyButton3.grid(row=1, column=2, sticky=W)

MyButton4 = ttk.Radiobutton(root, text='Schedule', value='schedule', variable=btn2)
MyButton4.grid(row=1, column=3)

MyButton5 = ttk.Radiobutton(root, text='YouTube', value='youtube', variable=btn2)
MyButton5.grid(row=1, column=4, sticky=E)

MyButton6 = Button(root, image=photo, command=buttonClick, bd=0, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
MyButton6.grid(row=0, column=5)

entry1.focus()
root.wm_attributes('-topmost', 1)
btn2.set('google')

current_time = datetime.datetime.now()
h = current_time.hour

if (int(h) >= 6 and int(h) < 12):
    speak.Speak('Good Morning')
elif (int(h) >= 12 and int(h) <= 16):
    speak.Speak('Good Afternoon')
elif(int(h) >= 16 and int(h) <= 23):
    speak.Speak('Good Evening')
else:
    speak.Speak('Good Night ')
            
speak.Speak('Q, at your service sir, What can I do for you ?')

root.mainloop()

