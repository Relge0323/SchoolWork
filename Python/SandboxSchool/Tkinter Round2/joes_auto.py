import tkinter

class JoesAutomotive:
    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive")
        self.main_window.geometry("300x300")

        # dictionary of services
        self.maintenance_services = {'oil change': 30.00,
                                     'lube job': 20.00,
                                     'radiator flush': 40.00,
                                     'transmission flush': 100.00,
                                     'inspection': 35.00,
                                     'muffler replacement': 200.00,
                                     'tire rotation': 20.00}
        
        # dictionary to store IntVar variables for each checkbox
        self.cb_vars = {}



        # create 3 frames, title_frame, checkboxes_frame, total_cost_frame
        self.title_frame = tkinter.Frame(self.main_window)
        self.title_frame.pack()

        self.checkbox_frame = tkinter.Frame(self.main_window)
        self.checkbox_frame.pack()

        self.total_cost_frame = tkinter.Frame(self.main_window)
        self.total_cost_frame.pack()


        # create title label
        self.title_label = tkinter.Label(self.title_frame, text='Joe\'s Automotive')
        self.title_label.pack(ipadx=8, ipady=15, padx=15)

        # create checkboxes using for loop
        for key, value, in self.maintenance_services.items():
            var = tkinter.IntVar()
            self.cb_vars[key] = var
            self.cb_service = tkinter.Checkbutton(self.checkbox_frame,
                                                  text=f'{key} - ${value}',
                                                    variable=var,
                                                    command=self.calc_total)
            self.cb_service.pack()
        

        self.total_cost_label = tkinter.Label(self.total_cost_frame, text='Total: $0.00')
        self.total_cost_label.pack()
        



        tkinter.mainloop()
    
    def calc_total(self):
        total_sum  = 0
        
        for key in self.maintenance_services:
            if self.cb_vars[key].get() == 1:
                total_sum += self.maintenance_services[key]
        
        self.total_cost_label.config(text=f'Total: ${total_sum}')

if __name__ == '__main__':
    mygui = JoesAutomotive()

