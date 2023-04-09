from tkinter import *
import time
from PIL import ImageTk
from tkinter import ttk, messagebox
from playsound import playsound
import multiprocessing
from datetime import datetime
from threading import *


hours_list = ['00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24']

minutes_list = ['00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59']

ringtones_list = ['nice_wake_up', 
'twirling_intime', 'wakeup_alarm_tone']

ringtones_path = {
    'nice_wake_up': 'D:\\harshitha\\alaram\\nice_wake_up.mp3',
    'twirling_intime': 'D:\\harshitha\\alaram\\twirling_intime.mp3',
    'wakeup_alarm_tone': 'D:\\harshitha\\alaram\\wakeup_alarm_tone.mp3'
}

class Alarm_Clock:
    def __init__(self, root):
        self.window = root
        self.window.geometry("680x420+0+0")
        self.window.title("Alaram Clock")
        

        
        self.bg_image = ImageTk.PhotoImage(file="C:\\Users\\ejapu\\OneDrive\\Pictures\\Saved Pictures\\image.jpg")
        self.background = Label(self.window, image=self.bg_image)
        self.background.place(x=0,y=0,relwidth=1,relheight=1)

        self.display = Label(self.window, font=('Helvetica', 34), 
        bg = 'black', fg = 'lightblue')
        self.display.place(x=100,y=150)

        
        self.show_time()

        
        set_button = Button(self.window, text="Set Alarm", 
        font=('Helvetica',15), bg="red", fg="white", 
        command=self.another_window)
        set_button.place(x=270, y=220)

   
    def show_time(self):
        current_time = time.strftime('%H:%M:%S %p, %A')
       
        self.display.config(text = current_time)
        self.display.after(100, self.show_time)

   
    def another_window(self):
        self.window_2 = Tk()
        self.window_2.title("Set Alarm")
        self.window_2.geometry("680x420+200+200")
        self.window_2.configure(bg="orange")
        
        
        hours_label = Label(self.window_2, text="Hours", 
        font=("times new roman",20))
        hours_label.place(x=150, y=50)

       
        minute_label = Label(self.window_2, text="Minutes", 
        font=("times new roman",20))
        minute_label.place(x=450, y=50)

        
        self.hours = StringVar()
        self.hours_combobox = ttk.Combobox(self.window_2, 
        width=10, height=10, textvariable=self.hours, 
        font=("times new roman",15))
        self.hours_combobox['values'] = hours_list
        self.hours_combobox.current(0)
        self.hours_combobox.place(x=150,y=90)

       
        self.minutes = StringVar()
        self.minutes_combobox = ttk.Combobox(self.window_2, 
        width=10, height=10, textvariable=self.minutes, 
        font=("times new roman",15))
        self.minutes_combobox['values'] = minutes_list
        self.minutes_combobox.current(0)
        self.minutes_combobox.place(x=450,y=90)

        
        ringtone_label = Label(self.window_2, text="Ringtones", 
        font=("times new roman",20))
        ringtone_label.place(x=150, y=130)

       
        self.ringtones = StringVar()
        self.ringtones_combobox = ttk.Combobox(self.window_2, 
        width=15, height=10, textvariable=self.ringtones, 
        font=("times new roman",15))
        self.ringtones_combobox['values'] = ringtones_list
        self.ringtones_combobox.current(0)
        self.ringtones_combobox.place(x=150,y=170)

       
        message_label = Label(self.window_2, text="Message", 
        font=("times new roman",20))
        message_label.place(x=150, y=210)

        
        self.message = StringVar()
        self.message_entry = Entry(self.window_2, 
        textvariable=self.message, font=("times new roman",14), width=30)
        self.message_entry.insert(0, 'Wake Up')
        self.message_entry.place(x=150, y=250)

        
        test_button = Button(self.window_2, text='Test', 
        font=('Helvetica',15), bg="lightblue", fg="black", command=self.test_window)
        test_button.place(x=150, y=300)

        
        cancel_button = Button(self.window_2, 
        text='Stop', font=('Helvetica',15), bg="red", 
        fg="black", command=self.window_2.destroy)
        cancel_button.place(x=390, y=300)

        
        start_button = Button(self.window_2, text='Start',
        font=('Helvetica',15), bg="red", fg="black", command=self.Threading_1)
        start_button.place(x=490, y=300)


        self.window_2.mainloop()


    def test_window(self):
        self.bg=PhotoImage(file="D:\\harshitha\\mrng.png")
        self.lb=Label(root,image=self.bg)
        self.lb.place(x=0,y=0)
        process = multiprocessing.Process(target=playsound, 
        args=(ringtones_path[self.ringtones_combobox.get()],))
        process.start()
        messagebox.showinfo('Playing...', 'press ENTER to stop playing')
        process.terminate()    
    def Threading_1(self):
        self.bg=PhotoImage(file="D:\\harshitha\\mrng.png")
        self.lb=Label(root,image=self.bg)
        self.lb.place(x=0,y=0)
        x = Thread(target=self.set_alarm_time)
        x.start()
    def set_alarm_time(self):
        alarm_time = f"{self.hours_combobox.get()}:{self.minutes_combobox.get()}"
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        try:
            while True: 
                current_time = datetime.now()
                current_time_format = current_time.strftime("%H:%M")
                if current_time_format == alarm_time:
                    process = multiprocessing.Process(target=playsound, 
                    args=(ringtones_path[self.ringtones_combobox.get()],))
                    process.start()
                    messagebox.showinfo("Alarm",f"{self.message_entry.get()}, It's {alarm_time}")
                    process.terminate()
                    break
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")
if __name__ == "__main__":
    root = Tk()
    obj = Alarm_Clock(root)
    root.mainloop()