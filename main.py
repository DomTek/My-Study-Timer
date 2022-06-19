from tkinter import *
from datetime import datetime

root = Tk()
root.geometry("300x150")

# list to safe the start and finish time to process later
time_save = []

# Function for the start button to retrieve, display and store start time
def startClick():
    current_time = retriev_time()
    time_lable = Label(root, text="Study start time is : " + current_time)
    time_lable.grid(row=1, column=2)
    time_save.insert(0, current_time)

# Function for the stop button to retrieve, display and store stop time
def stopClick():

    current_time2 = retriev_time()
    timeLable2 = Label(root, text="Study stop time is : " + current_time2)
    datetime_object = datetime.strptime(current_time2, '%H:%M:%S')
    datetime_object2 = datetime.strptime(time_save[0], '%H:%M:%S')
    timeSpent = datetime_object - datetime_object2
    timeLable3 = Label(root, text="Your Study Time was: " + str(timeSpent),bg="#41E5FF")
    timeLable2.grid(row=2, column=2)
    timeLable3.grid(row=3, column=2)

# function used to retrieve the current time
def retriev_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

# Creating GUI buttons and labels
title = Label(root, text="Study Timer", font=(12), width=30)
startButton = Button(root, text="Start Timer", command=startClick)
stopButton = Button(root, text="Stop timer", comman=stopClick)


# Place Gui buttons and labels
title.grid(row=0, column=0, columnspan=3)
startButton.grid(row=1, column=0, sticky='w', pady=5, padx=5)
stopButton.grid(row=2,column=0, sticky='w', pady=5, padx=5)


root.mainloop()

