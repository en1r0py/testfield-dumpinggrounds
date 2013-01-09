import Tkinter
import os

class App:
    def __init__(self, master):
        frame = Tkinter.Frame(master, height=500,width=500)
        frame.pack()

        self.button = Tkinter.Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=Tkinter.LEFT)

        self.hi_there = Tkinter.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=Tkinter.LEFT)

        blah = 0

    def say_hi(self):
        print "Hi there, everyone"

if __name__ == '__main__':
    root = Tkinter.Tk()
    app = App(root)
    root.mainloop()
