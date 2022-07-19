import threading
import time
import tkinter as tk


class countdown:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry("380x230")
        self.master.configure(bg="gainsboro")
        self.master.title("Countdown Timer")
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.full_seconds = 0
        self.label1 = tk.Label(self.master,font=15,text="Enter the Time",bg="gainsboro",fg="black")
        self.label1.place(x=110,y=10)

        self.text = tk.Entry(self.master,font=30)
        self.text.place(x=75,y=38)

        self.start = tk.Button(self.master,font=45,text="START",command=self.start_thread, activebackground="lightgreen",fg="black")
        self.start.place(x=100,y=75)

        self.stop = tk.Button(self.master, font=45, text="RESET",command=self.reset, activebackground="coral",fg="black")
        self.place = self.stop.place(x=200, y=75)

        self.pause = tk.Button(self.master, font=35, text="PAUSE",command=self.pause, activebackground="yellow",fg="black")
        self.pause.place(x=100, y=125)

        self.reset = tk.Button(self.master, font=35, text="RESUME",command=self.resume, activebackground="cyan",fg="black")
        self.reset.place(x=200, y=125)

        self.label2 = tk.Label(self.master,font=("Ariel",15),bg="gainsboro",text="Time: 00:00:00 ")
        self.label2.place(x=120,y=180)
        self.master.mainloop()

    def start_thread(self):
        t = threading.Thread(target=self.start_time)
        t.start()

    def start_time(self):

        self.stop_loop = False
        time_split = self.text.get().split(":")
        if len(time_split) == 3:
            self.hours = int(time_split[0])
            self.minutes = int(time_split[1])
            self.seconds = int(time_split[2])
        elif len(time_split) == 2:
            self.minutes = int(time_split[0])
            self.seconds = int(time_split[1])
        elif len(time_split) == 1:
            self.seconds = int(time_split[0])
        else:
            print("invalid time format")
            return
        self.full_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        while self.full_seconds > 0 and not self.stop_loop:
            self.full_seconds = self.full_seconds - 1
            self.minutes, self.seconds = divmod(self.full_seconds, 60)
            self.hours, self.minutes = divmod(self.minutes, 60)
            self.label2.config(text=f"Time: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
            self.master.update()
            time.sleep(1)

        self.master.update()
        #self.timeup.config(text="TIME IS UP!")

    def pause(self):
        self.pause = True
        self.stop_loop = True
        self.hours = self.hours
        self.minutes = self.minutes
        self.seconds = self.seconds
        self.label2.config(text=f"Time: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
        self.label2.update()

    def resume(self):
        self.pause = False
        self.stop_loop = False
        while self.full_seconds > 0 and not self.stop_loop:
            self.full_seconds = self.full_seconds - 1
            self.minutes, self.seconds = divmod(self.full_seconds, 60)
            self.hours, self.minutes = divmod(self.minutes, 60)
            self.label2.config(text=f"Time: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
            self.master.update()
            time.sleep(1)

    def reset(self):
        self.stop_loop = True
        self.label2.config(text="Time: 00:00:00 ")
        self.master.update()


countdown()