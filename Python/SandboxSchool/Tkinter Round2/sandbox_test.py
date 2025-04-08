# a simple countdown timer

import tkinter
import tkinter.messagebox


class My_GUI:
    def __init__(self):
        # create the root window
        self.main_window = tkinter.Tk()

        # create a frame for the countdown
        self.countdown_frame = tkinter.Frame(self.main_window, borderwidth=1, relief='solid')

        # create a frame for the start and stop buttons
        self.buttons_frame = tkinter.Frame(self.main_window, borderwidth=5, relief='solid')

        # create countdown label and entry label for countdown
        self.countdown_label = tkinter.Label(self.countdown_frame, text='Countdown Time:')
        self.entry_label = tkinter.Entry(self.countdown_frame, width=10)

        # packing the 2 labels
        self.countdown_label.pack(side='left')
        self.entry_label.pack(side='left')



        # create a label to display the countdown time
        self.timer_label = tkinter.Label(self.countdown_frame, text="00:00")
        self.timer_label.pack(side='left')




        # create a button to start countdown
        self.start_button = tkinter.Button(self.buttons_frame, text='START', command=self.start_countdown)

        # create a button to stop or reset the countdown
        self.stop_button = tkinter.Button(self.buttons_frame, text='STOP', command=self.stop_countdown)

        # pack the frames
        self.countdown_frame.pack(padx=5, pady=5)
        self.buttons_frame.pack(padx=5, pady=5)

        # pack the start and stop buttons
        self.stop_button.pack(side='bottom')
        self.start_button.pack(side='bottom')

        self.countdown_time = 0 # time in seconds
        self.running = False    # to keep track if countdown is running



        tkinter.mainloop()
    
    # method to start the countdown when button is clicked, a callback function
    def start_countdown(self):
        try:
            self.countdown_time = int(self.entry_label.get())   # get time from use input
            self.update_timer()
            self.running = True
        except ValueError:
            tkinter.messagebox.showinfo('Input Error', 'Please enter a valid number')
    
    # method to update the timer every second
    def update_timer(self):
        if self.countdown_time > 0 and self.running:
            minutes, seconds = divmod(self.countdown_time, 60)
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")  # update display
            self.countdown_time -= 1
            self.main_window.after(1000, self.update_timer)
        elif self.countdown_time == 0:
            tkinter.messagebox.showinfo('Countdown', 'Time\'s up!')
            self.stop_countdown()

    # method to stop the countdown when the button is clicked
    def stop_countdown(self):
        self.running = False
        self.countdown_time = 0
        self.timer_label.config(text="00:00")
        tkinter.messagebox.showinfo('Countdown', 'Countdown Stopped')


if __name__ == '__main__':
    my_gui = My_GUI()