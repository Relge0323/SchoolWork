import tkinter


class VerticalScrollbarExample:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.title('Scrollbar')

        self.listbox_frame = tkinter.Frame(self.main_window)
        self.listbox_frame.pack(padx=20, pady=20)


        self.listbox = tkinter.Listbox(self.listbox_frame, height=6, width=0)
        self.listbox.pack(side='left')


        self.scrollbar = tkinter.Scrollbar(self.listbox_frame, orient=tkinter.VERTICAL)
        self.scrollbar.pack(side='right', fill=tkinter.Y)


        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)


        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        for month in months:
            self.listbox.insert(tkinter.END, month)

        
        tkinter.mainloop()

if __name__ == '__main__':
    mygui = VerticalScrollbarExample()