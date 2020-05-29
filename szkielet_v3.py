### POPRAWIONA WERSJA PORAWIONEJ WERSJI ##
### Data stworzenia: 28.05.2020.

import time
import random

from tkinter import *
from tkinter import messagebox
from functools import partial

# Na tę chwilę nasz program składa się z jednego okna.
# Poniższy zapis umożliwia względnie sprawne dołączenie ewentualnych dodatkowych
# okien, np. okna z widokiem menu początkowego czy okna z widokiem po zakończeniu gry.
# Jeśli ktoś z Was czuje, że ma niewystarczająco do zrobienia, to może się nimi zająć.

# Wykorzystałam formę zapisu z prezentacji nr 24 (opcja: za pomocą klas).

class AplikacjaGUI(Frame, object):

    #===========================================#
    #                                           #
    #               Konstruktor                 #
    #                                           #
    #===========================================#

    def __init__(self, master):
        super(AplikacjaGUI, self).__init__(master)

        self.master.title("Milionerzy.") # "Nazwa okna, w którym wyświetla się program".
        self.master.geometry("900x650") # "szerokośćxwysokość"
        self.master.resizable(width = False, height = False) # Okno ma stały rozmiar.

        # Główne obszary okna:
        # Prowadzący Aktualne_Pytanie, Warianty_Odpowiedzi,
        # Guziki_z_Wygranymi i Kola_Ratunkowe.

        self.Prowadzacy(master)
        self.Aktualne_Pytanie(master)
        self.Warianty_Odpowiedzi(master)
        self.Guziki_z_Wygranymi(master)
        self.Kola_Ratunkowe(master)


    #===========================================#
    #                                           #
    #            Koniec konstruktora            #
    #                                           #
    #===========================================#

    #===========================================#
    #     def podstawowych elementów okna       #
    #     programu, tzn. ich położenie          #
    #              kolor tła itd.               #
    #===========================================#


    def Prowadzacy(self, master):
        self.Hubert = Frame(self.master, bg = "white")
        self.Hubert.place(x = 0, y = 0, width = 600, height = 350)


        # Tło: wstępnie ustawione jako białe; oczywiście można zupełnie to zmienić.
        # Pozostawiam decyzję osobie zajmującej się Hubertem.

    #
    #
    #            Hubert
    #
    #

    def Kola_Ratunkowe(self, master):


    #
    #           KOŁA
    #
    #
    #

        #### TEN FRAGMENT MA CHARAKTER ORIENTACYJNY.###
        ### (później się go wyrzuci).
        ### Decyzja o tym, jak będą wyglądały koła,
        ### zależy od osoby, która zajmuje się ich robieniem.
        self.kola = []
        self.tekst_kola = ["*publ.", "50:50", "tel."]
        for i in range(3):
            self.kola.append(Button(self.master, text = self.tekst_kola[i], relief = RAISED, bg = "#0F0A8C", fg = "white"))
            self.kola[-1].place(x = 650 + 70*i, y = 50, width=60, height=50)
        ##########################

    #============================================================#

    def Aktualne_Pytanie(self, master):
        self.pytanie = Button(self.master, text = "", relief = RAISED, bg = "#0F0A8C", fg = "white")
        self.pytanie.place(x = 50, y = 400, width = 475, height=50)

    def Warianty_Odpowiedzi(self, master):
        self.odpowiedzi = []
        for i in range(4):
            self.odpowiedzi.append(Button(self.master, text = "", relief = RAISED, bg = "#0F0A8C", fg = "white"))
            if i == 0:
                self.odpowiedzi[-1].place(x = 50, y = 475, width = 225, height=50)
            elif i == 1:
                self.odpowiedzi[-1].place(x = 300, y = 475, width = 225, height=50)
            elif i == 2:
                self.odpowiedzi[-1].place(x = 50, y = 550, width = 225, height=50)
            else:
                self.odpowiedzi[-1].place(x = 300, y = 550, width = 225, height=50)

    def Guziki_z_Wygranymi(self, master):
        self.guziki = []
        sumy = ["500 zł", "1000 zł", "2000 zł", "5000 zł", "10 000 zł", "20 000 zł",
        "40 000 zł", "75 000 zł", "125 000 zł", "250 000 zł", "500 000 zł", "1 000 000 zł"]
        for i in range(12):
            self.guziki.append(Button(self.master, text = sumy[i], command = partial(self.poczatek_gry, i),
            relief = RAISED, state = DISABLED, bg = "#0F0A8C", fg = "white"))
            if i == 0:
                self.guziki[i].configure(state = NORMAL)
            self.guziki[-1].place(x = 650, y = 562.5 - 40*i, width=200, height=37.5)

    #============================================================#

    #===========================================#
    #          Koniec def podstawowych          #
    #             elementów okna.               #
    #===========================================#

    #===========================================#
    #          Poniżej: funkcje związane        #
    #  z działaniem gry (część dynamiczna).     #
    #===========================================#

    # 1: poczatek_gry
    # -> wywołuje funckję czyszczącą pole z pytaniem i 4 odpowiedzi
    # -> zmienia kolor aktualnego pytania na złoty
    # -> wywołuje funkcję przydzielającą nowe pytanie
    # -> na każdy przycisk z $$$ można kliknąć tylko raz
    #    (stąd: DISABLED po jej wykonaniu)

    def poczatek_gry(self, nr_pytania):
        self.czyszczenie_pol()
        self.guziki[nr_pytania].configure(bg = "#852EBA")
        self.nowe_pytanie(nr_pytania)
        self.guziki[nr_pytania].configure(state = DISABLED)

    # 2: czyszczenie_pol
    # -> czysci pole z pytaniem i 4 pola z odpowiedziami

    def czyszczenie_pol(self):
        for i in range(4):
            self.odpowiedzi[i].configure(bg="#0F0A8C", text = "")

    # 3: nowe_pytanie
    # -> wywołuje bazę pytań
    # -> wywołuję bazę odpowiedzi
    # na razie nie mamy jeszcze pytań i odpowiedzi
    # więc dałam przykładowe pytania

    def nowe_pytanie(self, nr_pytania):
        self.baza_pytan(nr_pytania)
        self.baza_odpowiedzi(nr_pytania)

    # 4: baza_pytan
    # -> wyświetla nowe pytanie

    def baza_pytan(self, nr_pytania):
        lista_pytan = ["pytanie1", "pytanie2", "pytanie3", "pytanie4", "pytanie5",
        "pytanie6", "pytanie7", "pytanie8", "pytanie9", "pytanie10", "pytanie11", "pytanie12"]
        self.pytanie.configure(text = lista_pytan[nr_pytania])

    # 5: baza_odpowiedzi
    # -> wyświetla warianty odpowiedzi (ABCD)
    # -> wywołuje funkcję determinującą zachowanie przycisków (ABCD) w danej rundzie

    def baza_odpowiedzi(self, nr_pytania):
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
            self.odpowiedzi[i].configure(text = lista_odpowiedzi[nr_pytania][i])

        self.sprawdz_odpowiedz(nr_pytania)

    # 6: sprawdz_odpowiedz
    # -> przypisje przyciskom odpowiednie dla danej rundy polecenie (command)
    #    inaczej mówiąc: określa na jaki kolor ma się zmienić odpowiedź po jej kliknięciu

    def sprawdz_odpowiedz(self, nr_pytania):
        lista_sprawdzajaca = [["tak","nie","nie","nie"], ["nie","tak","nie","nie"],
            ["nie","nie","tak","nie"], ["nie","nie","nie","tak"], ["tak","nie","nie","nie"],
            ["nie","tak","nie","nie"], ["nie","nie","tak","nie"], ["nie","nie","nie","tak"],
            ["tak","nie","nie","nie"], ["nie","tak","nie","nie"], ["nie","nie","tak","nie"],
            ["nie","nie","nie","tak"]]

    ### Na razie jest to zrobione w ten sposób, ale lepiej byłoby wprowadzić tu element losowości.
    ### Wiecie, żeby nie było tak, że np. zawsze odpowiedzią na trzecie pytanie jest C.

        for i in range(4):
            if lista_sprawdzajaca[nr_pytania][i] == "tak":
                self.odpowiedzi[i].configure(command = partial(self.reakcja_odpowiedz, i, "prawidłowa", nr_pytania))
            else:
                self.odpowiedzi[i].configure(command = partial(self.reakcja_odpowiedz, i, "zła", nr_pytania))

    # 7: reakcja_odpowiedz
    # -> zmienia kolor naciśniętej odpowiedzi
    #    na zielono, jeśli odpowiedź jest dobra
    #    na czerwono, jeśli jest zła
    # -> wywołuje funkcję wyświetlającą okienko z informacją o dobrej/złej odpowiedzi


    def reakcja_odpowiedz(self, ktora_odpowiedz, czy_dobra, nr_pytania):

        for i in range(4):
            if i == ktora_odpowiedz:
                if czy_dobra == "prawidłowa":
                    self.odpowiedzi[i].configure(bg = "green", command = "")
                    self.info_dobra_odpowiedz(nr_pytania)
                else:
                    self.odpowiedzi[i].configure(bg = "red", command = "")
                    self.przegrana()
            else:
                self.odpowiedzi[i].configure(text = "", command = "")

    # 8: info_dobra_odpowiedz
    # -> okienko z informacją o poprawnej odpowiedzi
    # (o tym może informować Hubert, ale wstępnie jest)
    # -> zmienia tło zdobytych $$$ na złoty kolor.

    def info_dobra_odpowiedz(self, nr_pytania):
        messagebox.showinfo("GRATULACJE", "Poprawna odpowiedź!")
        self.guziki[nr_pytania].configure(bg = "gold")
        if nr_pytania != 11: # Dla ostatniego pytania nie ma czego zwolnić.
            self.zwolnij_guzik(nr_pytania + 1)

    # 9: zwolnij_guzik
    # -> dobra odpowiedź umożliwia kliknięcie na kolejną kwotę,
    #    a tym samym: zaczęcie nowej rundy

    def zwolnij_guzik(self, nr_do_zwolnienia):
        self.guziki[nr_do_zwolnienia].configure(state = NORMAL)

    # 10: przegrana
    # -> okienko z informacją o przegranej
    # -> zamyka główne okno

    def przegrana(self):
        messagebox.showinfo("PORAŻKA", "Przegrałeś :(")
        self.master.destroy()

#==========================================================#

# Poza klasą: funkcja tworząca okienko i wywołująca klasę.

def main():
    Glowne_Okno = Tk()
    app = AplikacjaGUI(Glowne_Okno) # wywołanie klasy
    Glowne_Okno.mainloop()

main() # Wywołanie funkcji "main".


### Uffff... koniec.
