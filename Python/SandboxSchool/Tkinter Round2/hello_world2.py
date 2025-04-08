import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label1 = tkinter.Label(self.main_window, text='Mike loves Cobi')
        self.label2 = tkinter.Label(self.main_window, text='label 2 testing')

        self.label1.pack()
        self.label2.pack()


        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()