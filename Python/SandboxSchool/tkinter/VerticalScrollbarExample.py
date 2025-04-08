# this program demonstrates a listbox with a vertical scrollbar.
import tkinter

class VerticalScrollbarExample:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()

        #create a frame for the listbox and vertical scrollbar
        self.listbox_frame = tkinter.Frame(self.main_window)
        self.listbox_frame.pack(padx=20, pady=20)

        #create a listbox widget in the listbox_frame
        self.listbox = tkinter.Listbox(self.listbox_frame, height=6, width=0)
        self.listbox.pack(side='left')

        # create a vertical scrollbar in the listbox_frame
        self.scrollbar = tkinter.Scrollbar(self.listbox_frame, orient=tkinter.VERTICAL)
        self.scrollbar.pack(side='right', fill=tkinter.Y)

        # configure the scrollbar and listbox to work together
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # create a list with the names of the months
        months = ['january', 'febuary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

        for i in months:
            self.listbox.insert(tkinter.END, i)

        
        tkinter.mainloop()

if __name__ == '__main__':
    scrollbar_example = VerticalScrollbarExample()

