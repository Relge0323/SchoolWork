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
        for i in self.words.keys():
            self.english_listbox.insert(tkinter.END, i)

        # populate portuguese listbox
        for i in self.words.values():
            self.portuguese_listbox.insert(tkinter.END, i)


        # bind the selection event
        self.english_listbox.bind("<<ListboxSelect>>", self.target_portuguese)
        self.portuguese_listbox.bind("<<ListboxSelect>>", self.target_english)



        tkinter.mainloop()


    def target_portuguese(self, event):
        index = self.english_listbox.curselection()

        if index:
            english_word = self.english_listbox.get(index)
            portuguese_translation = self.words[english_word]

            portuguese_index = list(self.words.values()).index(portuguese_translation)

            self.portuguese_listbox.selection_clear(0, tkinter.END)
            self.portuguese_listbox.selection_set(portuguese_index)
            self.portuguese_listbox.activate(portuguese_index)

    def target_english(self, event):
        index = self.portuguese_listbox.curselection()

        if index:
            portuguese_word = self.portuguese_listbox.get(index)

            for english, portuguese in self.words.items():
                if portuguese_word == portuguese:
                    english_word = english
                    break
            
            english_index = list(self.words.keys()).index(english_word)

            self.english_listbox.selection_clear(0, tkinter.END)
            self.english_listbox.selection_set(english_index)
            self.english_listbox.activate(english_index)

if __name__ == '__main__':
    mygui = EnglishToPortuguese()