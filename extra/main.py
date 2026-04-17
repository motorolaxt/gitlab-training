import tkinter as tk
from tkinter import messagebox

def madness():
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("wina", "THIS")
    messagebox.showinfo("winb", "IS")
    messagebox.showinfo("winc", "SPAARTAA!!!")
    messagebox.showinfo("winc", ".... not yet")
    messagebox.showinfo("winc", "no, sorry")
    messagebox.showinfo("winc", "I said SPARTA!!!")
    root.destroy()

madness()