from tkinter import *

window = Tk()
window.title("Button")
window.geometry("450x200+20+10")

btn1 = Button(window, text="Color", bg="blue", fg="red")
btn1.pack()
btn1.place(x=100, y=150)

def demoColorChange():
 btn1.configure(bg="yellow", fg="red")

btn2 = Button(window, text = "<--- Click to change the color of the button", command= demoColorChange)
btn2.pack()
btn2.place(x=150,y=150)

window.mainloop()