import tkinter

class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.test_label = tkinter.Label(self.main_window, text='Hello World')
        
        self.test_label.pack()



        tkinter.mainloop()


if __name__ == '__main__':
    my_gui = MyGUI()