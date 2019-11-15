import tkinter as tk
#from "C:\Users\user\Anaconda3\Lib\site-packages\pytube import YouTube
import pytube

def downloadvid():
    global E1
    string = E1.get()
    yt = pytube.YouTube(str(string))
    
    videos = yt.streams.first()
    print(str(videos))
    
    dest = str(input("Enter dest: "))
    videos.download(dest)
    print("file is downloaded")

##the first arg widget needs is a root
root = tk.Tk()

w = tk.Label(root,text="Youtube_Down")
w.pack()

E1 = tk.Entry(root,bd = 5)
E1.pack(side = tk.TOP)

button = tk.Button(root,text="Down",fg="green",command = downloadvid)
button.pack(side = tk.BOTTOM)

root.mainloop()
