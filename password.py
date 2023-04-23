import customtkinter
import tkinter
import random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

chars = 'abcdefghijklmnopqrstuvwxyz'
symbols = '[]{}()*&_-!@?0123456789'

chars = list(chars + chars.upper() + symbols)

def generate():
    len_passwords = int(entry_len.get())
    count_passwords = int(entry_count.get())
    for i in range(count_passwords):
        password = ''
        for j in range(len_passwords):
            password += random.choice(chars)
        text_field.insert(tkinter.END, password + '\n')



def clear():
    text_field.delete(0.0, tkinter.END)


window = customtkinter.CTk()
window.title('Generator password')
window.geometry('600*600')

customtkinter.CTkLabel(window, text='number of passwords: ').place(x = 10, y = 30)
entry_count = customtkinter.CTkEntry(window, width=50)
entry_count.place(x = 140, y = 30)

customtkinter.CTkLabel(window, text='password length: ').place(x = 10, y = 60)
entry_len = customtkinter.CTkEntry(window, width=50)
entry_len.place(x = 140, y = 60)

btn_clear = customtkinter.CTkButton(window, text='Clear', command=clear)
btn_clear.place(x = 30, y = 100)

btn_generate = customtkinter.CTkButton(window, text='Generate', command=generate)
btn_generate.place(x = 30, y = 150)

text_field = customtkinter.CTkTextbox(window, width=560, height=400)
text_field.place(x = 20, y = 200)

window.mainloop()