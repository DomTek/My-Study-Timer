from tkinter import *
from datetime import datetime

root = Tk()
root.geometry("300x450")

# list to safe the start and finish time to process later
time_save = []
time_records = []


# Function for the start button to retrieve, display and store start time
def startClick():
    current_time = retriev_time()
    time_lable = Label(root, text="Study start time is : " + current_time)
    time_lable.grid(row=1, column=2)
    startButton["state"] = "disabled"
    stopButton["state"] = "normal"
    time_save.insert(0, current_time)

# Function for the stop button to retrieve, display and store stop time
def stopClick():
    current_time2 = retriev_time()
    stop_time_lable = Label(root, text="Study stop time is : " + current_time2)
    time_save.append(current_time2)

    datetime_object = datetime.strptime(current_time2, '%H:%M:%S')
    datetime_object2 = datetime.strptime(time_save[0], '%H:%M:%S')
    timeSpent = datetime_object - datetime_object2
    result_lable = Label(root, text="Your Study Time was: " + str(timeSpent), bg="#41E5FF")
    stop_time_lable.grid(row=2, column=2)
    result_lable.grid(row=3, column=2)

    #records time to be used for list or later processing
    #time_records.append(timeSpent)


    # function to enable and disable the buttons as they are used
    startButton["state"] = "normal"
    stopButton["state"] = "disabled"

    # adding the time spent studying to a list to be used later to display and save
    time_records.append(str(timeSpent))

    text_area.insert(END, str(timeSpent) + '\n')


# function used to retrieve the current time
def retriev_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


# Creating GUI buttons and labels
title = Label(root, text="Study Timer", font=(12), width=30)
startButton = Button(root, text="Start Timer", command=startClick)
stopButton = Button(root, text="Stop timer", comman=stopClick)
text_area = Text(root, height=20, width=35)

# Place Gui buttons and labels
title.grid(row=0, column=0, columnspan=3)
startButton.grid(row=1, column=0, sticky='w', pady=5, padx=5)
stopButton.grid(row=2, column=0, sticky='w', pady=5, padx=5)
text_area.grid(row=4, columnspan=3)

root.mainloop()

