import tkinter

class EnglishToPortuguese:
    def __init__(self):

        self.words = {'Hello': 'Ola',
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

        # create output frame for translation
        self.output_frame = tkinter.Frame(self.main_window, padx=20, pady=20)
        self.output_frame.pack()



        # create english_label
        self.english_label = tkinter.Label(self.english_words_frame, text='English')
        self.english_label.pack()

        # create portuguese label
        self.portuguese_label = tkinter.Label(self.portuguese_words_frame, text='Portuguese')
        self.portuguese_label.pack()

        # create output label
        self.output_var = tkinter.StringVar()
        self.output_label = tkinter.Label(self.output_frame, textvariable=self.output_var)
        self.output_label.pack()




        # create english listbox
        self.english_listbox = tkinter.Listbox(self.english_words_frame, height=0, width=0)
        self.english_listbox.pack(side='bottom', padx=5, pady=5)

        # create portuguese listbox
        self.portuguese_listbox = tkinter.Listbox(self.portuguese_words_frame, height=0, width=0)
        self.portuguese_listbox.pack(side='bottom', padx=5, pady=5)




        # populate the english listbox
        for i in self.words.keys():
            self.english_listbox.insert(tkinter.END, i)

        # populate portuguese listbox
        for i in self.words.values():
            self.portuguese_listbox.insert(tkinter.END, i)


        # i kept running into what i can only imagine is an infinite loop when i tried making
        # the curselection() target the other listbox,  i could get it to work once on either side
        # but it would freeze on the second attempt, so my workaround was to create a label and use
        # StringVar() to show the relation. I realize this isn't what you wanted, but at least I can
        # get this one to run and function properly
        
        # bind english word for selection
        self.english_listbox.bind('<<ListboxSelect>>', self.display_portuguese)
        self.portuguese_listbox.bind('<<ListboxSelect>>', self.display_english)


        tkinter.mainloop()


    

    def display_portuguese(self, event):
        index = self.english_listbox.curselection()

        if index:
            english_word = self.english_listbox.get(index[0])
            port_word = self.words[english_word]
            self.output_var.set(f'{english_word} == {port_word}')


    def display_english(self, event):
        index = self.portuguese_listbox.curselection()

        if index:
            port_word = self.portuguese_listbox.get(index[0])
            
            # for loop to find value of port_word
            for key, value in self.words.items():
                if value == port_word:
                    eng_word = key
                    break
            
            # i like the output of keeping the eng word on the left side
            self.output_var.set(f'{eng_word} == {port_word}')











if __name__ == '__main__':
    mygui = EnglishToPortuguese()