from tkinter import * #graphical user interface – GUI
from tkinter import filedialog #to create file/directory selection windows
import pygame #import pygame
import os #работа с операционной системой

root = Tk()
root.title("Aisu's favourite musics")
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)
    
    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global pause
    pygame.mixer.music.pause()
    paused = True

def sled_music():
    global current_song, paused
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def pred_music():
    global current_song, paused

    try:
       songlist.selection_clear(0, END)
       songlist.selection_set(songs.index(current_song) - 1)
       current_song = songs[songlist.curselection()[0]]
       play_music()
    except:
        pass

organise_menu = Menu(menubar, tearoff = False)
organise_menu.add_command(label = 'Select Folder', command = load_music)
menubar.add_cascade(label = 'Organise', menu = organise_menu)

songlist = Listbox(root, bg = "PapayaWhip", fg = "Black", width = 100, height = 15)
songlist.pack()

play_btn_image = PhotoImage(file='C:/Users/aisul/Documents/PP2/TSIS7/music/play.png').subsample(5)
pause_btn_image = PhotoImage(file='C:/Users/aisul/Documents/PP2/TSIS7/music/pause.png').subsample(5)
sled_btn_image = PhotoImage(file='C:/Users/aisul/Documents/PP2/TSIS7/music/sled.png').subsample(5)
pred_btn_image = PhotoImage(file='C:/Users/aisul/Documents/PP2/TSIS7/music/pred.png').subsample(5)

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image = play_btn_image, borderwidth = 0, command = play_music)
pause_btn = Button(control_frame, image = pause_btn_image, borderwidth = 0, command = pause_music)
sled_btn = Button(control_frame, image = sled_btn_image, borderwidth = 0, command = sled_music)
pred_btn = Button(control_frame, image = pred_btn_image, borderwidth = 0, command = pred_music)

play_btn.grid(row = 0, column = 1, padx = 7, pady = 10)
pause_btn.grid(row = 0, column = 2, padx = 7, pady = 10)
sled_btn.grid(row = 0, column = 3, padx = 7, pady = 10)
pred_btn.grid(row = 0, column = 0, padx = 7, pady = 10)

root.mainloop()