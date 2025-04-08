import tkinter

class CreateRectangle:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.main_window, height=200, width=200)

        self.canvas.create_arc(10, 10, 180, 180, start=45, extent=30)

        self.canvas.pack()

        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = CreateRectangle()