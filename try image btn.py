from tkinter import *
root = Tk()
root.title("ROUNDED BUTTON")
#root.iconbitmap("HELLO")
root.geometry("380x570") #width x height
def thing():
   my_label.config(text="YOU CLICK THE BUTTON")

login_btn = PhotoImage(file="pic1.png")

img_label = Label(image=login_btn)

my_button = Button(root, image=login_btn , command=thing ,borderwidth=10)
my_button.pack(pady=20)

my_label = Label(root,text="")
my_label.pack(pady=20)

mainloop()
