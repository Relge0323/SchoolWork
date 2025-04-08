import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window, borderwidth=1, relief='solid')
        self.bottom_frame = tkinter.Frame(self.main_window, borderwidth=3, relief='flat')

        # create 3 label widgets for the top frame
        self.label1 = tkinter.Label(self.top_frame, text='Mike')
        self.label2 = tkinter.Label(self.top_frame, text='Cobi')
        self.label3 = tkinter.Label(self.top_frame, text='Lovers', borderwidth=1, relief='solid')

        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='right', pady=(0, 20))


        self.label4 = tkinter.Label(self.bottom_frame, text='Scott')
        self.label5 = tkinter.Label(self.bottom_frame, text='Keith')
        self.label6 = tkinter.Label(self.bottom_frame, text='Brothers')

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop()


if __name__ == '__main__':
    my_gui = MyGUI()