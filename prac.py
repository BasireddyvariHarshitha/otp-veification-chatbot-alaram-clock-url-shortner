import pyperclip
import pyshorteners
from tkinter import *
from PIL import Image,ImageTk


root=Tk()
root.geometry("500x300")
root.title("URL Shortener")
#root.configure(bg="lightblue")
bg=PhotoImage(file="D:\\harshitha\\hras.png")
lb=Label(root,image=bg)
lb.place(x=0,y=0)
url=StringVar()
url_addrerss=StringVar()

def urlshort():
    urladd=url.get()
    url_shrt=pyshorteners.Shortener().tinyurl.short(urladd)
    url_addrerss.set(url_shrt)
def copyurl():
    url_shrt=url_addrerss.get()
    pyperclip.copy(url_shrt)
Label(root,text="HARSHITHA REDDY",font="poppins",bg="pink").pack(pady=20)
Label(root,text="ENTER URL Link",font="poppins",bg="orange").pack(pady=20)
Entry(root,textvariable=url).pack(pady=7)
Button(root,text="Generate short URL",command=urlshort).pack(pady=20)
Entry(root,textvariable=url_addrerss).pack(pady=7)
Button(root,text="You can Copy URL",command=copyurl,bg="green").pack(pady=20)
root.mainloop()