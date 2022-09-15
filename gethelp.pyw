#IMPORTS
from tkinter import *
from pygame import mixer
import pygame
import time
import os
import random

music = os.listdir('./songs')
random.shuffle(music)

""" for i in range(len(music)):
    music[i] = "./songs/"+music[i] """


#listing music:
""" music = [
    "./songs/Anywhen You Say - Cheel.mp3",
    "./songs/Cartoon - Howling (Ft. Asena) [NCS Release].mp3"
    ] """ #legacy test

import sounddevice as sd
print(sd.query_devices(device=None, kind=None))

#WINDOW SETTINGS
window = Tk()
window.title("Streaming Music Player by OTAKU")
window.geometry("900x50")
#window.wm_iconbitmap('media_logo.ico')

topFrame = Frame(window)
topFrame.pack()

bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)
window.resizable(width=True, height=False)

window["bg"] = "black"

music_number = int(0)
music_number2 = (music_number)
next_music = (music[music_number + 1])
current_music = (music[music_number])

paused = True

#DEFINITIONS BELOW:

def quitprogram():
    time.sleep(0.25)
    window.destroy()
    time.sleep(0.25)
    quit()

def nextsong():
    global songLABEL
    global music_number
    global current_music
    global music
    global music_number2
    global next_music
    mixer.music.stop()
    music_number = int(music_number2 + 1)
    music_number2 = (music_number)
    print (music_number)
    current_music = (music[music_number])
    mixer.music.load("./songs/"+current_music)

    songLABEL.forget()
    time.sleep(0.5)
    songLABEL = Label(text=current_music, fg="white")
    songLABEL.pack(side=TOP)
    songLABEL["bg"] = "black"

    time.sleep(0.5)
    mixer.music.play()

    next_music = (music[music_number + 1])
    pygame.mixer.music.queue(next_music)
    print ("NEXT: ", next_music)


def lastsong():
    global songLABEL
    global music_number
    global current_music
    global music
    global music_number2
    global next_music
    mixer.music.stop()
    music_number = int(music_number2 - 1)
    music_number2 = (music_number)
    print (music_number)
    current_music = (music[music_number])
    mixer.music.load("./songs/"+current_music)

    songLABEL.forget()
    time.sleep(0.5)
    songLABEL = Label(text=current_music, fg="white")
    songLABEL.pack(side=TOP)
    songLABEL["bg"] = "black"

    time.sleep(0.5)
    mixer.music.play()

    next_music = (music[music_number + 1])
    pygame.mixer.music.queue(next_music)
    print ("NEXT: ", next_music)


def playpause():
    global songLABEL
    global current_music
    global next_music
    print(music_number)
    current_music = (music[music_number])
    global paused

    if mixer.get_init():
        if paused is False:
            mixer.music.pause()
            paused = True
        else:
            mixer.music.unpause()
            paused = False
    else:
        mixer.init()
        mixer.music.load("./songs/"+current_music)
        pygame.mixer.music.set_volume(0.1) #initial volume
        mixer.music.play()
        paused = False

    songLABEL.forget()
    songLABEL = Label(text=current_music, fg="white")
    songLABEL.pack(side=TOP)
    songLABEL["bg"] = "black"

    next_music = (music[music_number + 1])
    pygame.mixer.music.queue(next_music)
    print ("NEXT: ", next_music)

def rewindsong():
    pygame.mixer.music.rewind()


def volumedown():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)


def volumeup():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)



playBUTTON = Button(text="PLAY-PAUSE", fg="white")
playBUTTON.pack(side=LEFT)
playBUTTON.configure(command=playpause)
playBUTTON["bg"] = "black"

nextBUTTON = Button(text="NEXT▶", fg="white")
nextBUTTON.pack(side=LEFT, padx=10)
nextBUTTON.configure(command=nextsong)
nextBUTTON["bg"] = "black"

lastBUTTON = Button(text="◀PREVIOUS", fg="white")
lastBUTTON.pack(side=LEFT, padx=10)
lastBUTTON.configure(command=lastsong)
lastBUTTON["bg"] = "black"

rewindBUTTON = Button(text="↻REPLAY", fg="white")
rewindBUTTON.pack(side=LEFT, padx=10)
rewindBUTTON.configure(command=rewindsong)
rewindBUTTON["bg"] = "black"

volumedownBUTTON = Button(text="🔉VOL -", fg="white")
volumedownBUTTON.pack(side=LEFT, padx=10)
volumedownBUTTON.configure(command=volumedown)
volumedownBUTTON["bg"] = "black"

volumeupBUTTON = Button(text="🔊VOL +", fg="white")
volumeupBUTTON.pack(side=LEFT, padx=10)
volumeupBUTTON.configure(command=volumeup)
volumeupBUTTON["bg"] = "black"

songLABEL = Label(text="music provided by NoCopyrightSounds", fg="white")
songLABEL.pack(side=TOP)
songLABEL["bg"] = "black"

window.protocol('WM_DELETE_WINDOW', quitprogram)

#THE WINDOW BEING KEPT OPEN
window.mainloop()