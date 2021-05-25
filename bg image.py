from tkinter import *
import tkinter.ttk as ttk

root=Tk()
root.title("Background image")
root.geometry("330x430")

framehome=Frame(root,bg="red")
framehome.pack(fill=BOTH,expand=True)

imagehome=PhotoImage(file="pic1.png")
label1=ttk.Label(framehome,image=imagehome)
label1.pack(fill=BOTH,expand=True)

labela=Label(label1,text="UJJWAL IMAGE",fg="black",font=("calibri",30,"bold"))
labela.pack()

root.mainloop()
