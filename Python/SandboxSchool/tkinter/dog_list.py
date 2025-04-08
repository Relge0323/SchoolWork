import tkinter
import tkinter.messagebox

class ListBoxSelection:
    def __init__(self):
        self.main_window = tkinter.Tk()


        # create a lsitbox widget
        self.dog_listbox = tkinter.Listbox(self.main_window, width=0, height=0)
        self.dog_listbox.pack(padx=10, pady=5)

        # create a list with the names of dog breeds.
        dogs = ['labrador', 'poodle', 'great dane', 'terrier']

        # populate the listbox with the list contents
        for dog in dogs:
            self.dog_listbox.insert(tkinter.END, dog)

        
        # create a button to get the selected item
        self.get_button = tkinter.Button(self.main_window, text='Get Item', command=self.__retrieve_dog)
        self.get_button.pack(padx=10, pady=5)

        # start main loop
        tkinter.mainloop()
    
    def __retrieve_dog(self):
        # get the index of the selected item
        indexes = self.dog_listbox.curselection()

        # if an item is selected, display it
        if (len(indexes) > 0):
            tkinter.messagebox.showinfo(message=self.dog_listbox.get(indexes[0]))
        else:
            tkinter.messagebox.showinfo(message='No item selected.')


if __name__ == '__main__':
    listbox_selection = ListBoxSelection()