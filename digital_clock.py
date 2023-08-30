from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("500x500")
app_window.resizable(1, 1)

text_font = ("Boulder", 68, 'bold')
background = "#f2e750"
foreground = "blue"  
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)


creator_label = Label(app_window, text="Made by ISHA TOPNO", font=("Helvetica", 14))
creator_label.grid(row=1, column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
