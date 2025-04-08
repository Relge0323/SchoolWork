import tkinter

class HorizontalScrollbarExample:
    def __init__(self):
        self.main_window = tkinter.Tk()


        self.listbox_frame = tkinter.Frame(self.main_window)
        self.listbox_frame.pack(padx=20, pady=20)


        self.listbox = tkinter.Listbox(self.listbox_frame, height=0, width=30)
        self.listbox.pack(side='top')


        self.scrollbar = tkinter.Scrollbar(self.listbox_frame, orient=tkinter.HORIZONTAL)
        self.scrollbar.pack(side='bottom', fill=tkinter.X)

        self.scrollbar.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=self.scrollbar.set)


        data = ['the burj khalifa building is 2717 feet tall',
                'the shanghai tower is 2073 feet tall',
                'the abraj al-bait clock tower is 1971 feet tall',
                'the ping an finance center is 1965 feet tall']
        
        for i in data:
            self.listbox.insert(tkinter.END, i)


        tkinter.mainloop()

if __name__ == '__main__':
    mygui = HorizontalScrollbarExample()