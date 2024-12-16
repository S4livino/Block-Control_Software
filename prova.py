import pyautogui #Libreria per muovere il cursore
import time #Libreria per gestire il tempo in secondi
import tkinter as tk #Libreria per gestire banner di avvertimento
from tkinter import messagebox

def mostra_avviso():
    # Creazione di una finestra principale
    finestra = tk.Tk()
    finestra.withdraw()  # Nascondi la finestra principale

    # Mostra un messaggio di avviso
    messagebox.showwarning("Attenzione", "Tempo di utilizzo di Netflix superato. Lasciare Mouse e Tastiera!")

    # Chiudi la finestra principale
    finestra.destroy()




def controllo_netflix_aperto():
    # Controlla se l'immagine è presente sullo schermo
    time.sleep(1)
    try:
        immagine_presente = pyautogui.locateOnScreen('icona_netflix_barra_applicazioni.png', confidence= 0.7)
    
        if immagine_presente:
            print("Immagine trovata!")
            return True
        else:
            
            print("Immagine non trovata.")
            return False
        
    except pyautogui.ImageNotFoundException:
        print("Immagine non trovata ")
        return False

    





def chiudi_applicazione(immagine_presente):
    
    #Controllo se la funzione controllo_netflix_aperto non ha trovato l'immagine
    if (immagine_presente == False):
        print("Si è verificato un problema. Immagine non trovata")
        return False
    
    centro = pyautogui.locateCenterOnScreen('icona_netflix_barra_applicazioni.png', confidence=0.8)
    pyautogui.moveTo(centro, duration=0.5)  # Spostati in 0.2 secondi
    print(f"Spostato al centro: {centro}")

    # Clicca sull'app nella parte barra delle applicazioni e cerca di chiudere l'applicazione richiesta
    pyautogui.click(button='right',duration=0.2)
    print("Clic destro eseguito.")
    nuova_posizione = (centro[0], centro[1] - 50)
    pyautogui.moveTo(nuova_posizione, duration=0.4)
    print(f"Spostato a nuova posizione: {nuova_posizione}")
    pyautogui.click(button='left',duration=0.2)

    # Controllo se chiuso con successo
    time.sleep(1)
    centro = pyautogui.locateCenterOnScreen('icona_netflix_barra_applicazioni.png',confidence=0.7)
    if centro:
        print("Immagine trovata. Si è verificato un errore")
        return False
        
    else:
        print("Applicazione chiusa con successo")
    return True

def main():
    while True:
        time.sleep(2)
        if(controllo_netflix_aperto()):
            time.sleep(2)
            mostra_avviso()
            time.sleep(2)
            chiudi_applicazione()
            return 0


# MODIFICHE DA FARE: SI PIANTAAAA Aggiungere controllo nel main se non viene chiusa con successo  l'applicazione + Altro sicuramente

main()