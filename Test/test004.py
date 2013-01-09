import Tkinter
import tkMessageBox

class App:
    def __init__(self, master):
        self.frame = Tkinter.Frame(master, width=400, height=400)
        self.frame.pack()
        self.create_menu(master, self.frame)
        master.title("This is a fuzzbug")

    def create_menu(self, master, frame):
        top = master.winfo_toplevel()
        self.menubar = Tkinter.Menu(top)
        top["menu"] = self.menubar


        self.filemenu = Tkinter.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.say_hi)
        self.filemenu.add_command(label="Save", command=self.say_hi)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit", command=master.quit)

        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.helpmenu = Tkinter.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.say_about)

        self.menubar.add_cascade(label="Help", menu=self.helpmenu)


    def say_hi(self):
        print "Hey world"

    def say_about(self):
        tkMessageBox.showinfo("About", "This is a test program")


if __name__ == '__main__':
    root = Tkinter.Tk()
    app = App(root)
    root.mainloop()

