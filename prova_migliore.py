import tkinter as tk
from tkinter import messagebox

def mostra_avviso():
    # Creazione di una finestra principale
    finestra = tk.Tk()
    finestra.withdraw()  # Nascondi la finestra principale

    # Mostra un messaggio di avviso
    messagebox.showwarning("Attenzione", "Questo è un avvertimento!")

    # Chiudi la finestra principale
    finestra.destroy()

# Esegui la funzione per mostrare l'avviso
mostra_avviso()
