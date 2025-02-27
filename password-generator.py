from tkinter import *
from random import randint

root = Tk()
root.title('Strong Password Generator')
root.geometry("500x300")

def new_rand():
    pwd_entry.delete(0, END)
    pwd_length = int(my_entry.get())
    my_passwor = ""
    for x in range(pwd_length):
        my_passwor += chr(randint(33,126))
    pwd_entry.insert(0, my_passwor)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pwd_entry.get())

#Label Frame
lf = LabelFrame(root, text="How many characters?")
lf.pack(pady=20)

my_entry =  Entry(lf,font=("Helvetica", 24))
my_entry.pack(padx=20, pady=20) 

pwd_entry =  Entry(root, text='',font=("Helvetica", 24))
pwd_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text='Generate Strong Password', command = new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text='Copy to Clipboard', command=clipper)
clip_button.grid(row=0, column=1, padx=10)


root.mainloop()