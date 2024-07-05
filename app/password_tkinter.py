import customtkinter as ctk
import string
import random
from CTkMessagebox import CTkMessagebox


def pass_tkinter():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("315x196+700+300")
    root.resizable(False, False)
    root.title("Генератор паролей")
    root.grid_columnconfigure((0, 1, 2), weight=1)
    root.grid_rowconfigure((0, 1, 2), weight=1)

    def password(chars, number=1, letter=1, symbol=1):
        if not number and not letter and not symbol:
            return CTkMessagebox(title="ошибка", message='должен быть хотя бы один из: цифр, букв, знаков')
        number = string.digits if number else ''
        letter = string.ascii_letters if letter else ''
        symbol = string.punctuation if symbol else ''
        s = number + letter + symbol
        return ''.join(random.choices(s, k=chars))

    def generate():
        gen_password = password(int(myCombobox.get()), numbers_value.get(), letters_value.get(), symbols_value.get())
        if isinstance(gen_password, str):
            myEntry.delete(0, 'end')
            myEntry.insert(0, gen_password)

    myLabel = ctk.CTkLabel(root, text="Генератор паролей", font=("Arial", 20))
    myLabel.grid(row=0, column=0, pady=10, columnspan=3)

    myEntry = ctk.CTkEntry(root, placeholder_text="генерируйте ваш пароль", width=230, font=("Arial", 14))
    myEntry.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="w")

    myCombobox = ctk.CTkComboBox(root,
                                 values=["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", ],
                                 state="readonly", width=76, font=("Arial", 14))
    myCombobox.grid(row=1, column=2, pady=10, sticky="w")
    myCombobox.set("8")

    numbers_value = ctk.IntVar(value=1)
    numbersCheckBox = ctk.CTkCheckBox(root, text="Цифры", variable=numbers_value, onvalue=1, offvalue=0,
                                      font=("Arial", 14))
    numbersCheckBox.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    letters_value = ctk.IntVar(value=1)
    lettersCheckBox = ctk.CTkCheckBox(root, text="Буквы", variable=letters_value, onvalue=1, offvalue=0,
                                      font=("Arial", 14))
    lettersCheckBox.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    symbols_value = ctk.IntVar(value=1)
    symbolsCheckBox = ctk.CTkCheckBox(root, text="Знаки", variable=symbols_value, onvalue=1, offvalue=0,
                                      font=("Arial", 14))
    symbolsCheckBox.grid(row=2, column=2, pady=10, sticky="w")

    runButton = ctk.CTkButton(root, text="Генерировать", command=generate, width=300, height=35, font=("Arial", 14))
    runButton.grid(row=3, column=0, padx=10, pady=10, sticky="w", columnspan=3)

    root.mainloop()


if __name__ == '__main__':
    pass_tkinter()
