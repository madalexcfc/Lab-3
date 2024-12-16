import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_key():
    input_text = entry_input.get()
    
    if not (input_text.isdigit() and len(input_text) == 6):
        messagebox.showerror("Ошибка", "Введите шестизначное число!")
        return

    digits = list(input_text)

    block1 = digits[3] + digits[4] + digits[5] + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
    block2 = digits[0] + digits[1] + digits[2] + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)

    sum1 = int("".join(digits[3:6]))  
    sum2 = int("".join(digits[0:3]))  
    block3 = str(sum1 + sum2).zfill(4)  

    key = f"{block1}-{block2}-{block3}"

    entry_key.delete(0, tk.END)
    entry_key.insert(0, key)

root = tk.Tk()
root.title("Генератор ключа")
root.geometry("600x400")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(fill="both", expand=True)

try:
    background_image = tk.PhotoImage(file="C:/Users/PC/Desktop/test/Lab-3/background.png")  # Укажите путь к картинке
    canvas.create_image(0, 0, image=background_image, anchor="nw")
except tk.TclError:
    messagebox.showerror("Ошибка", "Фоновое изображение background.png не найдено!")

label_input = tk.Label(root, text="Введите шестизначное число (DEC):", font=("Arial", 12), bg="lightblue")
canvas.create_window(300, 50, window=label_input)

entry_input = tk.Entry(root, font=("Arial", 14))
canvas.create_window(300, 100, window=entry_input)

button_generate = tk.Button(root, text="Сгенерировать ключ", font=("Arial", 14), command=generate_key, bg="green", fg="white")
canvas.create_window(300, 150, window=button_generate)

label_key = tk.Label(root, text="Сгенерированный ключ:", font=("Arial", 12), bg="lightblue")
canvas.create_window(300, 200, window=label_key)

entry_key = tk.Entry(root, font=("Arial", 14), justify="center")
canvas.create_window(300, 250, window=entry_key)

root.mainloop()
