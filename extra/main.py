import tkinter as tk
from tkinter import messagebox

def madness():
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Okno 1", "THIS")
    messagebox.showinfo("Okno 2", "IS")
    messagebox.showinfo("Okno 3", "SPAARTAA!!!")

    root.destroy()

madness()