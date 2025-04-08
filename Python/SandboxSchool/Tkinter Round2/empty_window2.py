# this program displays an empty window.

import tkinter

class MyGUI:
    def __init__(self):
        # create the main window widget
        self.main_window = tkinter.Tk()

        # enter the tkinter main loop
        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()