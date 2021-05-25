from tkinter import *
root = Tk()
root.title("ROUNDED BUTTON")
root.configure(bg="goldenrod")

root.geometry("980x600") #width x height

def thing():
   my_label.config(text="YOU CLICK THE BUTTON")

login_btn = PhotoImage(file="hotel.png")

img_label = Label(image=login_btn)

my_button = Button(root, image=login_btn , command=thing ,borderwidth=10)
my_button.pack(pady=20)

btn1=Button(root,text="EXIT",command=root.destroy)
btn1.pack()

my_label = Label(root,text="HELLO")
my_label.pack(pady=20)

mainloop()
