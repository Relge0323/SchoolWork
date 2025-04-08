import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create two frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        # create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a distance in kilometers:')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)


        # pack the top frame widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')


        # create the button widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)


        # pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()
    
    
    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214

        tkinter.messagebox.showinfo('Results', str(kilo) + ' kilometers is equal to ' + str(miles) + ' miles.')


if __name__ == '__main__':
    kilo_conv = KiloConverterGUI()
