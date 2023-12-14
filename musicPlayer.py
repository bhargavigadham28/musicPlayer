from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
def addsongs():
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    for s in temp_song:
        s=s.replace("C:/Users/chari/OneDrive/Desktop/bhagi project/mp3 player using python/Music/","")
        songs_list.insert(END,s)
        
            
def deletesong():
    current_song=songs_list.curselection()
    songs_list.delete(current_song[0])
    
    
def Play():
    song=songs_list.get(ACTIVE)
    song=f'C:/Users/chari/OneDrive/Desktop/bhagi project/mp3 player using python/Music/{song}'
    mixer.music.load(song)
    mixer.music.play()
def Pause():
    mixer.music.pause()
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

def Resume():
    mixer.music.unpause()

#Function to navigate from the current song
def Previous():
    prev_song=songs_list.curselection()
    prev_song=prev_song[0]-1
    temp2=songs_list.get(prev_song)
    temp2=f'C:/Users/chari/OneDrive/Desktop/bhagi project/mp3 player using python/Music/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(prev_song)
    songs_list.selection_set(prev_song)

def Next():
    next_song=songs_list.curselection()
    next_song=next_song[0]+1
    temp=songs_list.get(next_song)
    temp=f'C:/Users/chari/OneDrive/Desktop/bhagi project/mp3 player using python/Music/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(next_song)
    songs_list.selection_set(next_song)
#creating the root window 
root=Tk()
root.title('Music player using python')
root.resizable(0,0)
mixer.init()

#create the listbox to contain songs
songs_list=Listbox(root,selectmode=SINGLE,bg="aqua",fg="black",font=('arial',15),height=12,width=47,selectbackground="deeppink3",selectforeground="aqua")
songs_list.grid(columnspan=9)

#font is defined which is to be used for the button font 
defined_font = font.Font(family='Helvetica')

#play button
play_button=Button(root,text="Play",width =7,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)

#pause button 
pause_button=Button(root,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

#stop button
stop_button=Button(root,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)

#resume button
Resume_button=Button(root,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)

#previous button
previous_button=Button(root,text="Previous",width =7,command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)

#nextbutton
next_button=Button(root,text="Next",width =7,command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)

#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Open Folder",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)


root.mainloop()