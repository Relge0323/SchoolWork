import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label1 = tkinter.Label(self.main_window, text='Testing out internal padding', borderwidth=1, relief='solid')
        self.label2 = tkinter.Label(self.main_window, text='For comparison', borderwidth=1, relief='solid')
        self.label3 = tkinter.Label(self.main_window, text='Bottom compare', borderwidth=1, relief='solid')

        self.label1.pack(side='left', ipadx=10, ipady=10)
        self.label2.pack(side='left', padx=15, pady=30)
        self.label3.pack(side='left', padx=(30,10), pady=(30,10))

        tkinter.mainloop()



if __name__ == '__main__':
    my_gui = MyGUI()