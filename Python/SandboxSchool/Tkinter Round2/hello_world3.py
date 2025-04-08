# using arguments in the pack method to move labels

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()


        # create a label
        self.label1 = tkinter.Label(self.main_window, text='Look ma, no hands...', borderwidth=1, relief='groove')
        self.label2 = tkinter.Label(self.main_window, text='sacrifices must be made for the greater good', borderwidth=5, relief='sunken')
        self.label3 = tkinter.Label(self.main_window, text='trying out relief', borderwidth=10, relief='ridge')
        
        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='bottom')




        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()