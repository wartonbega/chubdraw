import image
import tkinter as tk

def change_background():
    canvas.config(bg=background.get())

a=0
def evento(event):
    global a
    size=int(spinsize.get())
    color=spincolor.get()
    if a == 1:
        print(a)
        canvas.create_rectangle(event.x, event.y, event.x-size, event.y-size, outline=color, fill=color)


def clicked(event):
    global a
    a = 1
def realeased(event):
    global a
    a = 0
        
def cleared():
    canvas.delete('all')

window = tk.Tk()
canvas = tk.Canvas(window)
canvas.pack()

canvas.bind('<Button-1>',clicked)
canvas.bind('<Motion>', evento)
canvas.bind('<ButtonRelease-1>',realeased)

clear = tk.Button(window,text='clear',command = cleared)
clear.pack()

spincolor = tk.Spinbox(window ,values=('blue','yellow','black','red','darkblue','grey','lightgrey','darkgrey','white','green'))
spincolor.pack()

spinsize = tk.Spinbox(window, from_=0, to=20)
spinsize.pack()

background = tk.Spinbox(window, values=('white','blue','yellow','black','red','darkblue','grey','lightgrey','darkgrey','green'),command=change_background)
background.pack()

canvas.config(bg=background.get())

window.mainloop()