# this program demonstrates the Button widget.
# when the user clicks the Button, an info dialog box is displayed

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # create a main window
        self.main_window = tkinter.Tk()

        # create a button widget. The text 'Click Me!' should appear on the face of the Button.
        # the do_someting method sould be executed when the user clicks the button.
        self.my_button = tkinter.Button(self.main_window, text='Click Me!', command=self.do_something)


        # create a quit button
        self.quit_button = tkinter.Button(self.main_window, text='QUIT', command=self.main_window.destroy)

        self.my_button.pack()
        self.quit_button.pack(pady=20)

        tkinter.mainloop()


    # The do_something method is a callback function for the Button widget
    def do_something(self):
        # display an info dialog box
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button.')

if __name__ == '__main__':
    my_gui = MyGUI()