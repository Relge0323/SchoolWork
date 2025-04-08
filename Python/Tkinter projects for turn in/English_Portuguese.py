import tkinter

class EnglishToPortuguese:
    def __init__(self):

        words = {'Hello': 'Ola',
                 'Car': 'Carro',
                 'University': 'Universidade',
                 'College': 'Colegio',
                 'River': 'Rio',
                 'Pearl': 'Perola',
                 'Exam': 'Prova',
                 'Computer': 'Computador',
                 'City': 'Cidade',
                 'Food': 'Comida',
                 'Restroom': 'Banheiro',
                 'Programming': 'Programacao',
                 'Science': 'Ciencia',
                 'Understanding': 'Entendimento',
                 'Patience': 'Paciencia',
                 'Box': 'Caixa',
                 'Menu': 'Cardapio',
                 'Paper': 'Papel',
                 'Coding': 'Codificacao',
                 'Search': 'Procurar'}
        

        # create main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Translator")



        # create english words frame, pack to left side
        self.english_words_frame = tkinter.Frame(self.main_window, padx=20, pady=20)
        self.english_words_frame.pack(side='left')

        # create portuguese words frame, pack to right side
        self.portuguese_words_frame = tkinter.Frame(self.main_window, padx=20, pady=20)
        self.portuguese_words_frame.pack(side='right')



        # create english_label
        self.english_label = tkinter.Label(self.english_words_frame, text='English')
        self.english_label.pack()

        # create portuguese label
        self.portuguese_label = tkinter.Label(self.portuguese_words_frame, text='Portuguese')
        self.portuguese_label.pack()



        # create english listbox
        self.english_listbox = tkinter.Listbox(self.english_words_frame, height=0, width=0)
        self.english_listbox.pack(padx=5, pady=5)

        # create portuguese listbox
        self.portuguese_listbox = tkinter.Listbox(self.portuguese_words_frame, height=0, width=0)
        self.portuguese_listbox.pack(padx=5, pady=5)




        # populate the english listbox
        for i in words.keys():
            self.english_listbox.insert(tkinter.END, i)

        # populate portuguese listbox
        for i in words.values():
            self.portuguese_listbox.insert(tkinter.END, i)


        # TRACK WHEN WE'RE UPDATING TO AVOID INFINITE LOOP*********************************************************
        self.updating = False



        # bind the selection event
        self.english_listbox.bind("<<ListboxSelect>>", self.__target_portuguese)
        self.portuguese_listbox.bind("<<ListboxSelect>>", self.__target_english)



        tkinter.mainloop()


    def __target_portuguese(self, event):
        if self.updating:
            return  # prevent infinite loop
        
        index = self.english_listbox.curselection()

        if index:
            self.updating = True # disable event triggering temporarily
            self.portuguese_listbox.selection_clear(0, tkinter.END)
            self.portuguese_listbox.selection_set(index[0])
            self.portuguese_listbox.activate(index[0])

            self.main_window.after(10, self.reset_updating)

    def __target_english(self, event):
        if self.updating:
            return  # prevent infinite loop
        
        index = self.portuguese_listbox.curselection()

        if index:
            self.updating = True
            self.english_listbox.selection_clear(0, tkinter.END)
            self.english_listbox.selection_set(index[0])
            self.english_listbox.activate(index[0])
            self.main_window.after(10, self.reset_updating)

    # delay the reset of updating the flag to prevent event loop
    def reset_updating(self):
        self.updating = False


if __name__ == '__main__':
    mygui = EnglishToPortuguese()