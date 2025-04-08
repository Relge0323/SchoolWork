import tkinter
import tkinter.messagebox


class TestAveragesGUI:
    def __init__(self):
        # main window
        self.main_window = tkinter.Tk()

        # creating 5 frames, 3 test, 1 avg, 1 button frame
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        #test1 label
        self.test1_label = tkinter.Label(self.test1_frame, text='Enter the score for test 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame, width=10)

        #test2 label
        self.test2_label = tkinter.Label(self.test2_frame, text='Enter the score for test 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame, width=10)

        #test3 label
        self.test3_label = tkinter.Label(self.test3_frame, text='Enter the score for test 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame, width=10)

        #average label
        self.avg_label = tkinter.Label(self.avg_frame, text='Average')
        self.avg = tkinter.StringVar()    # setting StringVar to self.value to use with textvariable
        self.avg_output_label = tkinter.Label(self.avg_frame, textvariable=self.avg)

        #average and quit buttons
        self.avg_button = tkinter.Button(self.button_frame, text='Average', command=self.calc_average)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        #pack test1 label and test1 entry
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # pack test2 label and test2 entry
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        #pack test3 label and entry
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        # pack avg labels
        self.avg_label.pack(side='left')
        self.avg_output_label.pack(side='left')

        # pack buttons
        self.avg_button.pack(side='left')
        self.quit_button.pack(side='left')

        # packing all 5 frames
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()
    
    def calc_average(self):
        # store 3 test scores into variables
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())

        # calc avg
        self.average = (self.test1 + self.test2 + self.test3) / 3.0

        #update avg_label widget
        self.avg.set(self.average)



if __name__ == '__main__':
    mygui = TestAveragesGUI()