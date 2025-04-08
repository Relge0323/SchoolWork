import tkinter

class ListboxExample:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()


        # crate a listbox widget
        self.listbox = tkinter.Listbox(self.main_window, height=0, width=0)
        self.listbox.pack(padx=10, pady=10)


        # create a list with the days of the week.
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        # populate the listbox with the data using a loop
        for i in days:
            self.listbox.insert(tkinter.END, i)


        tkinter.mainloop()



if __name__ == '__main__':
    listbox_example = ListboxExample()