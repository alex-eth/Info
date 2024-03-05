import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import *


window = tk.Tk()
window.title("Simple Text Editor")

window.geometry("1000x800")


text_area = tk.Text(window, height=24, width=80)
text_area.pack(expand=True, fill=tk.BOTH)


def open_file():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, "r") as file2:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.INSERT, file2.read())
            window.title(f"Simple Text Editor - {file}")


def save_file():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with (open(file, "w") as file2):
            file2.write(text_area.get(1.0, tk.END))
            window.title(f"Simple Text Editor - {file}")


menu_bar = tk.Menu(window)
window.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)


file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

bouton_quit = Button(window,text = " Quit ",bg = 'red',command = window.destroy)
bouton_quit.configure(height=2, width=10)
bouton_quit.place(x=900,y=750)


window.mainloop()
