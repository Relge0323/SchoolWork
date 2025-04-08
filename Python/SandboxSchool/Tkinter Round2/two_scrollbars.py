import tkinter

class ScrollbarExample:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.outer_frame = tkinter.Frame(self.main_window)
        self.outer_frame.pack(padx=20, pady=20)

        self.inner_frame = tkinter.Frame(self.outer_frame)
        self.inner_frame.pack()


        self.listbox = tkinter.Listbox(self.inner_frame, height=5, width=30)
        self.listbox.pack(side='left')

        self.v_scrollbar = tkinter.Scrollbar(self.inner_frame, orient=tkinter.VERTICAL)
        self.v_scrollbar.pack(side='right', fill=tkinter.Y)


        self.h_scrollbar = tkinter.Scrollbar(self.outer_frame, orient=tkinter.HORIZONTAL)
        self.h_scrollbar.pack(side='bottom', fill=tkinter.X)


        self.v_scrollbar.config(command=self.listbox.yview)
        self.h_scrollbar.config(command=self.listbox.xview)
        self.listbox.config(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)


        data = ['the burj khalifa building is 2717 feet tall',
                'the shanghai tower is 2073 feet tall',
                'the abraj al-bait clock tower is 1971 feet tall',
                'the ping an finance center is 1965 feet tall',
                'the rain in spain',
                'falls mainly on the plain',
                'stop, its hammer time']
        

        for element in data:
            self.listbox.insert(tkinter.END, element)
        
        tkinter.mainloop()

if __name__ == '__main__':
    mygui = ScrollbarExample()