import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk() #tkinter module

apps = []

if os.path.isfile("save.txt"): #if save.txt exists in directory
    with open("save.txt", "r") as f: #open the file as read-only
        tempApps = f.read() #save read file as variable
        tempApps = tempApps.split(",") #split each entry with a ","
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                      filetypes=(("executables", "*.exe"), ("all files", "*.*"))) #filetypes, dropdown menu option. 1: executables for .exe files, 2: all files with or without .exe
    apps.append(filename)
    #print(filename)
    for app in apps:
        if app.endswith(".exe"):
            label = tk.Label(frame, text=os.path.basename(app), padx=15, pady=10, width=200)
            label.pack() #must pack() to show on screen

def runApps():
    for app in apps:
        try:
            os.startfile(app)  # loop over apps array and run each file
        except OSError:
            print("Invalid filename or extension")

canvas = tk.Canvas(root, height=500, width=700, bg="#303030") #style canvas / window
canvas.pack() #apply style from canvas variable

frame = tk.Frame(root, bg="#5e5e5e", padx=30, pady=30) #create frame inside tkinder canvas
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1) #set relative width/height of frame inside canvas, relx/rely leaves 0.1 on left/right and top/bottom of frame.. acts like css margin

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp) # -- adds button to root canvas, command=addApp means to execute addApp function when clicked
#openFile = tk.Button(frame, text="Open File", padx=10, pady=5, fg="white", bg="#263D42") -- adds button to frame
openFile.pack() #use .pack() to attach to root or frame

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps) # -- adds button to root canvas
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=os.path.basename(app), padx=15, pady=10, width=200)
    label.pack()

root.mainloop() # needed to create canvas window

with open("save.txt", "w") as f:
    for app in apps:
        if app.endswith(".exe"):
            f.write(app + ",")