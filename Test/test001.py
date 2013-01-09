import Tkinter
import os

root = Tkinter.Tk()

frame = Tkinter.Frame(root, height=250, width=250)
button = Tkinter.Button(root, text="Hey world")
button.pack(side=Tkinter.TOP)
button = Tkinter.Button(root, text="Quit", command=frame.quit)
button.pack(side=Tkinter.BOTTOM)


root.mainloop()

