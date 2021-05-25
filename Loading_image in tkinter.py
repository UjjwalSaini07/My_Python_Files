from tkinter import *

# FUNCTION TO LOAD IMAGE

def clickcode():
    my_image = PhotoImage(file="C:\\Users\\Us\\Desktop\\Project window\\\hotel.png")
    canvas.create_image(0,0,anchor=NW,image=my_image)
    canvas.my_image = my_image

window = Tk()
window.title("HOTEL IMAGE")
window.configure(bg="tomato2")

# CANVAS IS NOT VISIBLE
canvas = Canvas(window,width=879,height=461)
canvas.pack()

# CODE FOR BUTTON NOT VISIBLE
btn = Button(window,text = "CLICK MY PICTURE",bg="black",fg="white",command= clickcode)
btn.pack()
btn_for_quit = Button(window,text="QUIET",bg="black",fg="white",command = window.destroy)
btn_for_quit.pack()
