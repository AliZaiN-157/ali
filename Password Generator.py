import random
from tkinter import *
import string


def generate_password():
	password=[]
	for i in range(5):
		alpha=ramdom.choice(string.ascii_letters)
		symbol=ramdom.choice(string.punctuation)
		numbers=ramdom.choice(string.digits)
		password.append(alpha)
		password.append(symbol)
		password.append(numbers)

	y="".join(str(x)for x in password)
	lbl.config(text=y)	


root=Tk()
root.geometry("250x500")
btn=Button(root,text="generate password",commad=generate_password
btn.grid(row=2,column=2)
lbl=Label(root,font=("times",15,"bold"))
lbl.grid(row=4,column=2)
root.mainloop()