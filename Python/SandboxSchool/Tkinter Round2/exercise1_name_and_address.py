import tkinter

class NameAndAddress:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()

        # create StringVar objects to display name, street, and city-state-zip
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()

        # create two frames
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # create the label widgets, associated with the StringVar objects
        self.name_label = tkinter.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame, textvariable=self.street_value)
        self.csz_label = tkinter.Label(self.info_frame, textvariable=self.csz_value)

        # pack the labels
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

        # create the button widgets
        self.show_info_button = tkinter.Button(self.button_frame, text='Show Info', command=self.show)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        # pack the buttons
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        # pack the frames
        self.info_frame.pack()
        self.button_frame.pack()


        tkinter.mainloop()
    

    def show(self):
        self.name_value.set('Mike Egler')
        self.street_value.set('418 Lake David Drive')
        self.csz_value.set('Picayune, MS 39466')

if __name__ == '__main__':
    mygui = NameAndAddress()