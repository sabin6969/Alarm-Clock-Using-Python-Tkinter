import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import pygame
class Alarm:
    def __init__(self):
        root=tk.Tk()
        root.title("Alarm Clock")
        root.geometry('400x400')
        #----heading-----#
        title=tk.Label(root,text="Alarm Clock",font=('sans serif',12),fg='blue')
        title.place(x=165,y=20)
        #-----icon------#
        root.iconbitmap('clock icon.ico')
        #-----time entry-----#
        time_entry_label=tk.Label(root,text="Select Time (HH:MM)")
        time_entry_label.place(x=230,y=50)
        time_entry=ttk.Entry(root,font=('sans serif',12))
        time_entry.place(x=230,y=70,width=150,height=30)
        #---photo image---#
        photo_image=tk.PhotoImage(file='clock image.png')
        photo_label=ttk.Label(image=photo_image)
        photo_label.place(x=5,y=50,height=200,width=200)
        pygame.mixer.init()
        #---call back function---#
        def set_alarm():
            alarm_time=time_entry.get()
            if len(alarm_time)==0:
                messagebox.showerror("Time Not Selected","Please Select Time")
                text_message.delete(0,tk.END)
            else:
                if ":" in alarm_time:
                    lst=[]
                    lst=alarm_time.split(":")
                    try:
                        hour_integer=int(lst[1])
                        minute_integer=int(lst[2])
                        messagebox.showinfo("Sucess","Alarm Set Sucess")
                        current_time=time.strftime("%H:%M")
                        while alarm_time !=current_time:
                            current_time=time.strftime("%H:%M")
                        if alarm_time==current_time:
                            pygame.mixer.music.load('audio.mp3')
                            pygame.mixer.music.play()
                    except:
                        messagebox.showerror("Incorrect Format","Please Enter the Valid Format")
                        text_message.delete(0,tk.END)
                        time_entry.delete(0,tk.END)
                else:
                    messagebox.showwarning("Incorrect Format","Please Enter the Valid Format")
                    text_message.delete(0,tk.END)
                    time_entry.delete(0,tk.END)
        #---message----#
        message_label=tk.Label(root,text="Message")
        message_label.place(x=230,y=100)
        text_message=ttk.Entry(root)
        text_message.place(x=230,y=120,width=150,height=30)
        #-----set alarm button---#
        set_alarm_button=ttk.Button(root,text="Set Alarm",command=set_alarm)
        set_alarm_button.place(x=230,y=170,width=150)
        root.resizable(False,False)
        root.mainloop()
if __name__=="__main__":
    a = Alarm()