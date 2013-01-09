from Tkinter import *
import tkFileDialog

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.create_wgts()

    def create_wgts(self):
        self.MainMenu=Menu(self.master)

        self.wgt_confirm = Button(text='Confirm', command=self.traceback).pack(side=RIGHT)

        self.wgt_entry = Entry()
        self.wgt_entry.pack(side=RIGHT, fill=X, expand=1, ipadx=200)
        self.wgt_entry.bind('<Key-Return>', self.hit_enter)

        self.casMenu_File = Menu(self.MainMenu)
        self.casMenu_File.add_command(label="Open File", command=self.file_select)
        self.casMenu_File.add_command(label="Write to File", command=self.file_write)
        self.casMenu_File.add_separator()
        self.casMenu_File.add_command(label="Exit", command=self.traceback)

        self.MainMenu.add_cascade(label='File', menu=self.casMenu_File)
        self.master.config(menu=self.MainMenu)

    def traceback(self):
        print "traceback called"


    def hit_enter(self, event):
        print "Hit ENTER"


    def file_select(self):
        print "File>Open called"


    def file_write(self):
        print "File>Write File called"


root = Tk()
app = Application(master=root)
app.mainloop()

