# this program demonstrates the Canvas widget
import tkinter


class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()


        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        self.canvas.create_line(10,10, 189,10, 100,189, 10,10)

        self.canvas.pack()

        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = myGUI()