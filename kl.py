import openai
import tkinter as tk
from tkinter import *

openai.api_key = "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"

window = tk.Tk()
window.title("OpenAI Chatbot")
bg=PhotoImage(file="D:\\harshitha\\ct.png")
lb=Label(window,image=bg)
lb.place(x=0,y=0)
chatlog = tk.Text(window, height=20, width=50,bg="black")
inputfield = tk.Entry(window, width=50,bg="pink")

def get_response(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response.choices[0].text.strip()

def send_message():
    message = inputfield.get()
    inputfield.delete(0, tk.END)
    chatlog.insert(tk.END, "You: " + message + "\n")
    response = get_response(message)
    chatlog.insert(tk.END, "Chat Bot: " + response + "\n")


sendbutton = tk.Button(window, text="Send", command=send_message,fg='white',bg='green')
chatlog.pack()
inputfield.pack()
sendbutton.pack()

window.mainloop()
