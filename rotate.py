from tkinter import *


window = Tk()

window.title("Image Loader")
window.geometry("600x600")
window.config(background="gray9")


button_open = Button(window,text="Open Image")

button_open.place(relx=0.5,rely=0.2,anchor=CENTER)

label_loaded = Label(window)

label_loaded.place(relx=0.5,rely=0.5,anchor=CENTER)

button_rotate = Button(window,text="Rotate Image")

button_rotate.place(relx=0.5,rely=0.7,anchor=CENTER)

window.mainloop()