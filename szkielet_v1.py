import time
import random
from tkinter import *
from tkinter import messagebox
from functools import partial

# Numery pytania: od 0 do 11.
def poczatek_gry(nr_pytania):
    czyszczenie()
    guziki[nr_pytania].configure(bg = "gold")
    nowe_pytanie(nr_pytania)
    guziki[nr_pytania].configure(state = DISABLED)

def czyszczenie():
    for i in range(4):
        odpowiedzi[i].configure(bg="#0F0A8C")

def zwolnij_guzik(nr_do_zwolnienia):
    guziki[nr_do_zwolnienia].configure(state = NORMAL)

def nowe_pytanie(nr_pytania):
    baza_pytan(nr_pytania)
    baza_odpowiedzi(nr_pytania)

def baza_pytan(nr_pytania):
    lista_pytan = ["pytanie1", "pytanie2", "pytanie3", "pytanie4", "pytanie5",
    "pytanie6", "pytanie7", "pytanie8", "pytanie9", "pytanie10", "pytanie11", "pytanie12"]
    pytanie.configure(text = lista_pytan[nr_pytania])

def baza_odpowiedzi(nr_pytania):
    lista_odpowiedzi = [
        ["POPRAWNA", "1 odp. B ", "1 odp. C", "1 odp. D"],
        ["2 odp. A", "POPRAWNA", "2 odp. C", "2 odp. D"],
        ["3 odp. A", "3 odp. B", "POPRAWNA", "3 odp. D"],
        ["4 odp. A", "4 odp. B", "4 odp. C", "POPRAWNA"],
        ["POPRAWNA", "5 odp. B", "5 odp. C", "5 odp. D"],
        ["6 odp. A", "POPRAWNA", "6 odp. C", "6 odp. D"],
        ["7 odp. A", "7 odp. B", "POPRAWNA", "7 odp. D"],
        ["8 odp. A", "8 odp. B", "8 odp. C", "POPRAWNA"],
        ["POPRAWNA", "9 odp. B", "9 odp. C", "9 odp. D"],
        ["10 odp. A", "POPRAWNA", "10 odp. C", "10 odp. D"],
        ["11 odp. A", "11 odp. B", "POPRAWNA", "11 odp. D"],
        ["12 odp. A", "12 odp. B", "12 odp. C", "POPRAWNA"],]

    for i in range(4):
        odpowiedzi[i].configure(text = lista_odpowiedzi[nr_pytania][i])

    sprawdz_odpowiedz(nr_pytania)

def sprawdz_odpowiedz(nr_pytania):
    for i in range(4):
        odpowiedzi[i].configure(command = partial(reakcja_odpowiedz, i, "nie", nr_pytania))

        if nr_pytania == 0 or nr_pytania == 4 or nr_pytania == 8:
            odpowiedzi[0].configure(command = partial(reakcja_odpowiedz, 0, "tak", nr_pytania))
        elif nr_pytania == 1 or nr_pytania == 5 or nr_pytania == 9:
             odpowiedzi[1].configure(command = partial(reakcja_odpowiedz, 1, "tak", nr_pytania))
        elif nr_pytania == 2 or nr_pytania == 6 or nr_pytania == 10:
            odpowiedzi[2].configure(command = partial(reakcja_odpowiedz, 2, "tak", nr_pytania))
        elif nr_pytania == 3 or nr_pytania == 7 or nr_pytania == 11:
             odpowiedzi[3].configure(command = partial(reakcja_odpowiedz, 3, "tak", nr_pytania))

def reakcja_odpowiedz(ktora_odpowiedz, czy_dobra, nr_pytania):

    for i in range(4):
        if i == ktora_odpowiedz:
            if czy_dobra == "tak":
                odpowiedzi[i].configure(bg = "green", command = "")
            else:
                odpowiedzi[i].configure(bg = "red", command = "")
        else:
            odpowiedzi[i].configure(text = "", command = "")

    if czy_dobra == "tak":
        info_dobra_odpowiedz(nr_pytania)
    if czy_dobra == "nie":
        przegrana()

def info_dobra_odpowiedz(nr_pytania):
    messagebox.showinfo("GRATULACJE", "Poprawna odpowiedź!")
    if nr_pytania != 11:
        zwolnij_guzik(nr_pytania + 1)

def przegrana():
    messagebox.showinfo("PORAŻKA", "Przegrałeś :(")
    Glowne_Okno.destroy()

###==========###

Glowne_Okno = Tk()
Glowne_Okno.geometry("900x650")
Glowne_Okno.resizable(width = False, height = False)

# Hubert:
Hubert = Frame(Glowne_Okno, bg = "white")
Hubert.place(x = 0, y = 0, width = 600, height = 350)

# Aktualne pytanie i odpowiedzi:
pytanie = Button(Glowne_Okno, text = "", relief = RAISED, bg = "#0F0A8C", fg = "white")
pytanie.place(x = 50, y = 400, width = 475, height=50)

odpowiedzi = []
for i in range(4):
    odpowiedzi.append(Button(Glowne_Okno, text = "", relief = RAISED, bg = "#0F0A8C", fg = "white"))
    if i == 0:
        odpowiedzi[-1].place(x = 50, y = 475, width = 225, height=50)
    elif i == 1:
        odpowiedzi[-1].place(x = 300, y = 475, width = 225, height=50)
    elif i == 2:
        odpowiedzi[-1].place(x = 50, y = 550, width = 225, height=50)
    else:
        odpowiedzi[-1].place(x = 300, y = 550, width = 225, height=50)

# Wygrane po prawej:
guziki = []
sumy = ["500 zł", "1000 zł", "2000 zł", "5000 zł", "10 000 zł", "20 000 zł",
"40 000 zł", "75 000 zł", "125 000 zł", "250 000 zł", "500 000 zł", "1 000 000 zł"]
for i in range(12):
    guziki.append(Button(Glowne_Okno, text = sumy[i], command = partial(poczatek_gry, i),
    relief = RAISED, state = DISABLED, bg = "#0F0A8C", fg = "white"))
    if i == 0:
        guziki[i].configure(state = NORMAL)
    guziki[-1].place(x = 650, y = 562.5 - 40*i, width=200, height=37.5)

# Koła ratunkowe (orientacyjna pozycja, nic nie robią):
kola = []
tekst_kola = ["*publ.", "50:50", "tel."]
for i in range(3):
    kola.append(Button(Glowne_Okno, text = tekst_kola[i], relief = RAISED, bg = "#0F0A8C", fg = "white"))
    kola[-1].place(x = 650 + 70*i, y = 50, width=60, height=50)

Glowne_Okno.mainloop()
