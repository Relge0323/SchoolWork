import tkinter

class TimeZone:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Time Zones')

        self.__build_prompt_label()
        self.__build_listbox()
        self.__build_output_frame()
        self.__build_quit_button()

        tkinter.mainloop()




    # this method creates the prompt label widget
    def __build_prompt_label(self):
        self.prompt_label = tkinter.Label(self.main_window, text='Select a City')
        self.prompt_label.pack(padx=5, pady=5)





    # this method creates and populates the city listbox widget
    def __build_listbox(self):
        self.__cities = ['Denver', 'Honolulu', 'Minneapolis', 'New York', 'San Francisco']

        self.city_listbox = tkinter.Listbox(self.main_window, height=0, width=0)
        self.city_listbox.pack(padx=5, pady=5)

        # bind a callback function to the listbox
        self.city_listbox.bind('<<ListboxSelect>>', self.__display_time_zone)

        for i in self.__cities:
            self.city_listbox.insert(tkinter.END, i)






    # this method creates the output frame and its contents
    def __build_output_frame(self):
        #create the frame
        self.output_frame = tkinter.Frame(self.main_window)
        self.output_frame.pack(padx=5)

        # create label that reads "time zone"
        self.output_description_label = tkinter.Label(self.output_frame, text='Time Zone:')
        self.output_description_label.pack(side='left', padx=(5, 1), pady=5)

        # create a StringVar variable to hold the time zone name
        self.__timezone = tkinter.StringVar()

        # create the Label that displays teh time zone name
        self.output_label = tkinter.Label(self.output_frame, borderwidth=1, relief='solid', width=15, textvariable=self.__timezone)
        self.output_label.pack(side='right', padx=(1, 5), pady=5)

    




    # this method creates the quit button
    def __build_quit_button(self):
        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)
        self.quit_button.pack(padx=5, pady=5)






    # callback function for the city_listbox widget
    def __display_time_zone(self, event):
        # get the current selections
        index = self.city_listbox.curselection()

        # get the city
        city = self.city_listbox.get(index[0])

        # determine the time zone
        if city == 'Denver':
            self.__timezone.set('Mountain')
        elif city == 'Honolulu':
            self.__timezone.set('Hawaii-Aleutian')
        elif city == 'Minneapolis':
            self.__timezone.set('Central')
        elif city == 'New York':
            self.__timezone.set('Eastern')
        elif city == 'San Francisco':
            self.__timezone.set('Pacific')



            
if __name__ == '__main__':
    mygui = TimeZone()