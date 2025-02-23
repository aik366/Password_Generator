import customtkinter as ctk
from string import digits, ascii_letters, punctuation
import random
from CTkMessagebox import CTkMessagebox


def pass_tkinter():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("315x200+700+300")
    root.resizable(False, False)
    root.title("Генератор паролей")
    root.grid_columnconfigure((0, 1, 2), weight=1, uniform='a')
    root.grid_rowconfigure((0, 1, 2), weight=1, uniform='a')

    def generate_password():
        try:
            gen_password = ""
            if numbers_value.get():
                gen_password += digits
            if letters_value.get():
                gen_password += ascii_letters
            if symbols_value.get():
                gen_password += punctuation
            gen_password = ''.join(random.choices(gen_password, k=int(slider.get())))
            myEntry.delete(0, 'end')
            myEntry.insert(0, gen_password)
        except Exception as e:
            CTkMessagebox(title=f"ошибка: {e}", message='должен быть хотя бы один из: цифр, букв, знаков')

    def copy_to_clipboard():
        if myEntry.get():
            myEntry.clipboard_clear()
            myEntry.clipboard_append(myEntry.get())
            CTkMessagebox(title="Скопировано", message=f"Пароль: {myEntry.get()}\nскопирован в буфер обмена")
        else:
            CTkMessagebox(title="Ошибка", message="Генерируйте пароль")

    myLabel = ctk.CTkLabel(root, text="Генератор паролей", font=("Arial", 20))
    myLabel.grid(row=0, column=0, pady=5, columnspan=3)

    myEntry = ctk.CTkEntry(root, placeholder_text="генерируйте ваш пароль", width=300, font=("Arial", 14))
    myEntry.grid(row=1, column=0, padx=10, pady=5, columnspan=3, sticky="wn")

    numbers_value = ctk.IntVar(value=1)
    numbersCheckBox = ctk.CTkCheckBox(root, text="Цифры", variable=numbers_value, onvalue=1, offvalue=0,
                                      font=("Arial", 14))
    numbersCheckBox.grid(row=2, column=0, padx=(10, 20), pady=5, sticky="we")

    letters_value = ctk.IntVar(value=1)
    lettersCheckBox = ctk.CTkCheckBox(root, text="Буквы", variable=letters_value, onvalue=1, offvalue=0,
                                      font=("Arial", 14))
    lettersCheckBox.grid(row=2, column=1, padx=(10, 20), pady=5, sticky="we")

    symbols_value = ctk.IntVar(value=1)
    symbolsCheckBox = ctk.CTkCheckBox(root, text="Знаки", variable=symbols_value, onvalue=1, offvalue=0,
                                      font=("Arial", 14))
    symbolsCheckBox.grid(row=2, column=2, padx=(20, 10), pady=5, sticky="we")

    run_button = ctk.CTkButton(root, text="Генерировать", command=generate_password, height=35, font=("Arial", 14))
    run_button.grid(row=4, column=0, padx=(10, 5), pady=5, sticky="we", columnspan=2)

    copy_button = ctk.CTkButton(root, text="Copy", command=copy_to_clipboard, height=35, font=("Arial", 14))
    copy_button.grid(row=4, column=2, padx=(5, 10), pady=5, sticky="we")

    def slider_event(value):
        slider_Label.configure(text=f"Длина: {int(value)}")

    slider = ctk.CTkSlider(root, from_=6, to=24, command=slider_event)
    slider.grid(row=3, column=0, padx=(5, 0), pady=5, columnspan=2, sticky="we")
    slider.set(12)

    slider_Label = ctk.CTkLabel(root, text=f"Длина: {int(slider.get())}", font=("Arial", 16))
    slider_Label.grid(row=3, column=2, pady=5, sticky="we")

    root.mainloop()


if __name__ == '__main__':
    pass_tkinter()
