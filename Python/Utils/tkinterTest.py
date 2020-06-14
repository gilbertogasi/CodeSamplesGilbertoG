import tkinter
from tkinter import messagebox

def helloCallBack():
   textvalue = X.get()
   msg = messagebox.showinfo( "Mensaje", "Hello World, {}".format(textvalue))

def exitForm():
   top.quit()

top = tkinter.Tk()
top.geometry("300x100")
top.title("Saludos")
top.maxsize(width = 300, height = 100)

label = tkinter.Label(top, text = "Nombre:")
label.place(x = 20, y = 20)

X = tkinter.Entry(top, bd = 2)
X.pack(side = "right")
X.place(x = 75,y = 25)
X.focus()

B1 = tkinter.Button(top, text = "Hello", command = helloCallBack)
B1.place(x = 75,y = 50)

B2 = tkinter.Button(top, text = "Exit", command = exitForm)
B2.place(x = 125,y = 50)

top.mainloop()