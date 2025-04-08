import tkinter

class MyGUI:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("My First GUI")
        self.main_window.minsize(280, 280)

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #create a label to put on my window
        self.lbl = tkinter.Label(self.top_frame, text='Michael Egler', bg='black', fg='white', borderwidth=2, relief='solid')
        self.job = tkinter.Label(self.bottom_frame, text="Software Engineer", bg='green', fg='black', borderwidth=8, relief='raised')
        self.hobby = tkinter.Label(self.main_window, text="Sandbox Designs", bg='grey', fg='pink', borderwidth=6, relief='groove')

        # place label and make it visible on the window
        self.lbl.pack(side='left', ipadx=5, ipady=5, padx=20, pady=20)
        self.job.pack(side='left', ipadx=20, ipady=20, padx=20, pady=20)
        self.hobby.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        #start the gui
        tkinter.mainloop()



def main():
    my_Gui = MyGUI()


if __name__ == '__main__':
    main()
