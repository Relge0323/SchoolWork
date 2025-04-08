import tkinter


class ListboxExample:
    def __init__(self):
        self.main_window = tkinter.Tk()


        self.listbox = tkinter.Listbox(self.main_window)
        self.listbox.pack(padx=10, pady=10)

        self.listbox.insert(0, 'monday')
        self.listbox.insert(1, 'tuesday')
        self.listbox.insert(2, 'wednesday')
        self.listbox.insert(3, 'thursday')
        self.listbox.insert(4, 'friday')
        self.listbox.insert(5, 'saturday')
        self.listbox.insert(6, 'sunday')

        tkinter.mainloop()


if __name__ == '__main__':
    mygui = ListboxExample()