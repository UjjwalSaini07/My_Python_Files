from tkinter import *
window = Tk()
window.title("USING PILLOW LIBRARY")
canvas = Canvas(window, width = 1366, heigh=768)
canvas.pack()
my_image = PhotoImage(file="C:\\Users\\Us\\Desktop\\tmkoc.png")
canvas.create_image(0, 0, anchor = NW, image=my_image)
