### Data stworzenia: 03.06.2020
### Dodałam okno startowe.

import random

from tkinter import *
from tkinter import messagebox
from functools import partial
from Pytanka import pytania_all # zaimportowanie pytań z zewnętrznego pliku
from Pytanka import odpowiedzi_all # zaimportowanie odpowiedzi z zewnętrznego pliku
from Pytanka import sprawdzenie_all # zaimportowanie odpowiedzi z zewnętrznego pliku
from PIL import Image, ImageTk # dodawanie obrazków
import pygame # do dźwięku
pygame.mixer.init()

# EKRAN STARTOWY:
class AplikacjaGUI_1(Frame, object):
    def __init__(self, master):
        super(AplikacjaGUI_1, self).__init__(master)
        self.master.title("Milionerzy.")
        self.master.geometry("900x650")
        self.master.resizable(width = False, height = False)
        self.stworzWidgety(master)

    def stworzWidgety(self, master):
        nowa_gra = Button(self.master, text = "NOWA GRA", relief = RAISED,
                          bg = "lightblue", fg = "black", command = self.zacznij_gre)
        nowa_gra.place(x = 350, y = 225, width=200, height=75)
        koniec = Button(self.master,text = "WYJŚCIE Z PROGRAMU", relief = RAISED,
                        bg = "lightblue", fg = "black", command = self.zamknij_program)
        koniec.place(x = 350, y = 300, width=200, height=75)

    def zacznij_gre(self):
        self.master.destroy()
        Glowne_Okno = Tk()

        rozgrywka_pytania = []
        rozgrywka_odpowiedzi = []
        rozgrywka_sprawdzenie = []
        wylosowane_pytania = []

        for i in range(12): # do gry potrzebujemy tylko 12 pytań
            numer_pytania = random.randint(0,39)
            while numer_pytania in wylosowane_pytania: # nie może wylosować 2 razy tego samego pytania
                numer_pytania = random.randint(0,39)
            wylosowane_pytania.append(numer_pytania)
            rozgrywka_pytania.append(pytania_all[numer_pytania])
            rozgrywka_odpowiedzi.append(odpowiedzi_all[numer_pytania])
            rozgrywka_sprawdzenie.append(sprawdzenie_all[numer_pytania])

        ekran_2 = AplikacjaGUI_2(Glowne_Okno, rozgrywka_pytania, rozgrywka_odpowiedzi, rozgrywka_sprawdzenie) # wywołanie klasy
        Glowne_Okno.mainloop()

    def zamknij_program(self):
        self.master.destroy()


# GŁÓWNE OKNO:
class AplikacjaGUI_2(Frame, object):

    #===========================================#
    #                                           #
    #               Konstruktor                 #
    #                                           #
    #===========================================#

    def __init__(self, master, pyt, odp, spr):
        super(AplikacjaGUI_2, self).__init__(master)
        self.master.title("Milionerzy.") # "Nazwa okna, w którym wyświetla się program".
        self.master.geometry("900x650") # "szerokośćxwysokość"
        self.master.resizable(width = False, height = False) # Okno ma stały rozmiar.

        # Główne obszary okna:
        # Prowadzący Aktualne_Pytanie, Warianty_Odpowiedzi,
        # Guziki_z_Wygranymi i Kola_Ratunkowe.

        self.pula_pytan = pyt
        self.pula_odpowiedzi = odp
        self.pula_sprawdzen = spr


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
    #           command = "###" (trzeba uzupełnić nazwę poleceń)
    #

        self.kolo1_obraz = Image.open("1.png")
        self.kolo1_obraz = self.kolo1_obraz.resize((60, 50))
        self.kolo1_Tk = ImageTk.PhotoImage(self.kolo1_obraz)

        self.kolo2_obraz = Image.open("2.png")
        self.kolo2_obraz = self.kolo2_obraz.resize((60, 50))
        self.kolo2_Tk = ImageTk.PhotoImage(self.kolo2_obraz)

        self.kolo3_obraz = Image.open("3.png")
        self.kolo3_obraz = self.kolo3_obraz.resize((60, 50))
        self.kolo3_Tk = ImageTk.PhotoImage(self.kolo3_obraz)

        self.pierwsze_kolo = Button(self.master, text = "", image = self.kolo1_Tk, bg = "#0F0A8C", fg = "white", command = "###")
        self.pierwsze_kolo.place(x = 650, y = 50, width = 60, height = 50)

        self.drugie_kolo = Button(self.master, text = "", image = self.kolo2_Tk, bg = "#0F0A8C", fg = "white", command = "###")
        self.drugie_kolo.place(x = 720, y = 50, width = 60, height = 50)

        self.trzecie_kolo = Button(self.master, text = "", image = self.kolo3_Tk, bg = "#0F0A8C", fg = "white", command = "###")
        self.trzecie_kolo.place(x = 790, y = 50, width = 60, height = 50)
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
        self.pytanie.configure(text = self.pula_pytan[nr_pytania])

    # 5: baza_odpowiedzi
    # -> wyświetla warianty odpowiedzi (ABCD)
    # -> wywołuje funkcję determinującą zachowanie przycisków (ABCD) w danej rundzie

    def baza_odpowiedzi(self, nr_pytania):
        for i in range(4):
            self.odpowiedzi[i].configure(text = self.pula_odpowiedzi[nr_pytania][i])
        self.sprawdz_odpowiedz(nr_pytania)

    # 6: sprawdz_odpowiedz
    # -> przypisje przyciskom odpowiednie dla danej rundy polecenie (command)
    #    inaczej mówiąc: określa na jaki kolor ma się zmienić odpowiedź po jej kliknięciu

    def sprawdz_odpowiedz(self, nr_pytania):
        for i in range(4):
            if self.pula_sprawdzen[nr_pytania][i] == "tak":
                self.odpowiedzi[i].configure(command = partial(self.reakcja_odpowiedz, i, "prawidłowa", nr_pytania))
            else:
                self.odpowiedzi[i].configure(command = partial(self.reakcja_odpowiedz, i, "nieprawidłowa", nr_pytania))
    # 7: reakcja_odpowiedz
    # -> zmienia kolor naciśniętej odpowiedzi
    #    na zielono, jeśli odpowiedź jest dobra
    #    na czerwono, jeśli jest zła
    # -> wywołuje funkcję wyświetlającą okienko z informacją o dobrej/złej odpowiedzi

    def reakcja_odpowiedz(self, ktora_odpowiedz, czy_dobra, nr_pytania):
        for i in range(4):
            if i != ktora_odpowiedz:
                self.odpowiedzi[i].configure(text = "")
        for i in range(4):
            if i == ktora_odpowiedz:
                if czy_dobra == "prawidłowa":
                    self.odpowiedzi[i].configure(bg = "green", command = "")
                    self.info_dobra_odpowiedz(nr_pytania)
                elif czy_dobra == "nieprawidłowa":
                    self.odpowiedzi[i].configure(bg = "red", command = "")
                    self.przegrana()

    # 8: info_dobra_odpowiedz
    # -> okienko z informacją o poprawnej odpowiedzi
    # (o tym może informować Hubert, ale wstępnie jest)
    # -> zmienia tło zdobytych $$$ na złoty kolor.

    def info_dobra_odpowiedz(self, nr_pytania):
        pygame.mixer.music.load("aplauz.wav")
        pygame.mixer.music.play()
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
        pygame.mixer.music.load("przegrana.mp3")
        pygame.mixer.music.play()
        messagebox.showinfo("PORAŻKA", "Przegrałeś :(")
        self.master.destroy()
        ekran_startowy()
#==========================================================#

# Poza klasą: funkcja tworząca okienko i wywołująca klasę.

def ekran_startowy():
    Okno_Startowe = Tk()
    ekran_1 = AplikacjaGUI_1(Okno_Startowe)
    Okno_Startowe.mainloop()

ekran_startowy()
