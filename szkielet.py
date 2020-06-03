### Data stworzenia: 03.06.2020

import random

from tkinter import *
from tkinter import messagebox
from functools import partial
from Pytanka import pytania_all # zaimportowanie pytań z zewnętrznego pliku
from Pytanka import odpowiedzi_all # zaimportowanie odpowiedzi z zewnętrznego pliku
from Pytanka import sprawdzenie_all # zaimportowanie odpowiedzi z zewnętrznego pliku
from PIL import Image, ImageTk # dodawanie obrazków
import tkinter.font as font # czcionki
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
        pygame.mixer.music.load("muzyczka_startowa.mp3")
        pygame.mixer.music.play()

    def stworzWidgety(self, master):

        czcionka_1 = font.Font(family="Naula", size=15, weight="bold", slant="italic")

        nowa_gra = Button(self.master, text = "NOWA GRA", relief = RAISED,
                          fg = "#ffd750", bg = "#19133d", command = self.zacznij_gre)
        nowa_gra['font'] = czcionka_1
        nowa_gra.place(x = 350, y = 225, width=200, height=75)

        koniec = Button(self.master,text = "WYJŚCIE \nZ PROGRAMU", relief = RAISED,
                        fg = "#ffd750", bg = "#19133d", command = self.zamknij_program)
        koniec['font'] = czcionka_1
        koniec.place(x = 350, y = 310, width=200, height=75)

    def zacznij_gre(self):
        self.master.destroy()
        pygame.mixer.music.fadeout(2000)
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
    ############################################################################

    def Kola_Ratunkowe(self, master):
    #=====#
        self.publ_obraz = Image.open("1.png")
        self.publ_obraz = self.publ_obraz.resize((60, 50))
        self.publ_Tk = ImageTk.PhotoImage(self.publ_obraz)

        self.pol_na_pol_obraz = Image.open("2.png")
        self.pol_na_pol_obraz = self.pol_na_pol_obraz.resize((60, 50))
        self.pol_na_pol_Tk = ImageTk.PhotoImage(self.pol_na_pol_obraz)

        self.tel_obraz = Image.open("3.png")
        self.tel_obraz = self.tel_obraz.resize((60, 50))
        self.tel_Tk = ImageTk.PhotoImage(self.tel_obraz)
    #=====#

        self.przycisk_publ=Button(self.master, text = "publ", image = self.publ_Tk, relief = RAISED, state = DISABLED, bg = "#0F0A8C", fg = "white")
        self.przycisk_publ.place(x = 650 , y = 50, width=60, height=50)
        self.przycisk_5050=Button(self.master, text = "50/50", image = self.pol_na_pol_Tk, relief = RAISED, state = DISABLED, bg = "#0F0A8C", fg = "white")
        self.przycisk_5050.place(x = 720 , y = 50, width=60, height=50)
        self.przycisk_tel=Button(self.master, text = "tel", image = self.tel_Tk, relief = RAISED, state = DISABLED, bg = "#0F0A8C", fg = "white")
        self.przycisk_tel.place(x = 790 , y = 50, width=60, height=50)
        self.czy_wykorzystano_publ = False
        self.czy_wykorzystano_pol = False
        self.czy_wykorzystano_tel = False


    def wylacz_kola(self):
        self.przycisk_publ.configure(state = DISABLED)
        self.przycisk_5050.configure(state = DISABLED)
        self.przycisk_tel.configure(state = DISABLED)

    def wlacz_kola(self, nr_pytania):
        if self.czy_wykorzystano_publ == False:
            self.przycisk_publ.configure(state = NORMAL, command = partial(self.pytanie_do_publicznosci, nr_pytania))
        if self.czy_wykorzystano_pol == False:
            self.przycisk_5050.configure(state = NORMAL, command = partial(self.pol_na_pol, nr_pytania))
        if self.czy_wykorzystano_tel == False:
            self.przycisk_tel.configure(state = NORMAL, command = partial(self.telefon_do_przyjaciela, nr_pytania))

    def pytanie_do_publicznosci(self, nr_pytania):
        pytania = [0,1,2,3]
        for i in range(4):
            if self.pula_sprawdzen[nr_pytania][i] == "tak":
                prawidlowa = self.pula_odpowiedzi[nr_pytania][i]
                pytania.remove(i)
        losowa_bledna = random.randint(0,2)
        bledna = self.pula_odpowiedzi[nr_pytania][pytania[losowa_bledna]]
        szansa = 100 - (nr_pytania*3)
        losowa_ze_stu = random.randint(1,100)
        if losowa_ze_stu > szansa:
            odpowiedz = bledna
        else:
            odpowiedz = prawidlowa

        messagebox.showinfo("Pytanie do publicznosci", "Publiczność sądzi, ze odpowiedź to: "+odpowiedz)
        self.czy_wykorzystano_publ = True
        self.przycisk_publ.configure(state = DISABLED)

    def pol_na_pol(self, nr_pytania):
        pytania = [0,1,2,3]
        for i in range(4):
            if self.pula_sprawdzen[nr_pytania][i] == "tak":
                prawidlowa = self.pula_odpowiedzi[nr_pytania][i]
                pytania.remove(i)
        losowa_bledna = random.randint(0,2)
        bledna = self.pula_odpowiedzi[nr_pytania][pytania[losowa_bledna]]
        messagebox.showinfo("Pol na pol", "Odpowiedź to "+ prawidlowa+"lub "+ bledna)
        self.czy_wykorzystano_pol = True
        self.przycisk_5050.configure(state = DISABLED)

    def telefon_do_przyjaciela(self, nr_pytania):
        pytania = [0,1,2,3]
        for i in range(4):
            if self.pula_sprawdzen[nr_pytania][i] == "tak":
                prawidlowa = self.pula_odpowiedzi[nr_pytania][i]
                pytania.remove(i)
        losowa_bledna = random.randint(0,2)
        bledna = self.pula_odpowiedzi[nr_pytania][pytania[losowa_bledna]]
        szansa = 100 - (nr_pytania*4)
        losowa_ze_stu = random.randint(1,100)
        if losowa_ze_stu > szansa:
            odpowiedz = bledna
        else:
            odpowiedz = prawidlowa
        messagebox.showinfo("Telefon do przyjaciela", "Przyjaciel uważa, że prawdidłowa odpowiedź to: "+odpowiedz)
        self.czy_wykorzystano_tel = True
        self.przycisk_tel.configure(state = DISABLED)
        #######
        #dodalem jeszcze linijke do funkcji poczatek_gry()
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
        self.wlacz_kola(nr_pytania)

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
        # for i in range(4):
        #     self.odpowiedzi[i].configure(text = self.pula_odpowiedzi[nr_pytania][i])

        self.master.after(1000, lambda: self.odpowiedzi[0].configure(text = self.pula_odpowiedzi[nr_pytania][0]))
        self.master.after(2000, lambda: self.odpowiedzi[1].configure(text = self.pula_odpowiedzi[nr_pytania][1]))
        self.master.after(3000, lambda: self.odpowiedzi[2].configure(text = self.pula_odpowiedzi[nr_pytania][2]))
        self.master.after(4000, lambda: self.odpowiedzi[3].configure(text = self.pula_odpowiedzi[nr_pytania][3]))

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
                    self.przegrana(nr_pytania)

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
            self.czy_chcesz_grac_dalej(nr_pytania)
        else:
            self.jestes_milionerem()

    # 9: zwolnij_guzik
    # -> dobra odpowiedź umożliwia kliknięcie na kolejną kwotę,
    #    a tym samym: zaczęcie nowej rundy

    def czy_chcesz_grac_dalej(self, nr_pytania):
        kwoty = ["500 zł", "1000 zł", "2000 zł", "5000 zł", "10 000 zł", "20 000 zł",
        "40 000 zł", "75 000 zł", "125 000 zł", "250 000 zł", "500 000 zł", "1 000 000 zł"]

        graj_dalej = messagebox.askquestion("Uwaga!", "Obecnie masz w garści: " + str(kwoty[nr_pytania])
                                           + "\nCzy chcesz kontynuować grę?")
        if graj_dalej == "yes":
            self.zwolnij_guzik(nr_pytania + 1)
        else:
            messagebox.showinfo("Koniec gry", "Wygrana: " + str(kwoty[nr_pytania]))
            self.master.destroy()
            ekran_startowy()

    def zwolnij_guzik(self, nr_do_zwolnienia):
        self.guziki[nr_do_zwolnienia].configure(state = NORMAL)

    def jestes_milionerem(self):
        pygame.mixer.music.load("aplauz.wav")
        pygame.mixer.music.play()
        messagebox.showinfo("GRATULACJE", "Wygrałeś milion złotych!")
        self.master.destroy()
        ekran_startowy()

    # 10: przegrana
    # -> okienko z informacją o przegranej
    # -> zamyka główne okno

    def przegrana(self, nr_pytania):
        poprawna_odpowiedz = 0
        for i in range(4):
            if self.pula_sprawdzen[nr_pytania][i] == "tak":
                poprawna_odpowiedz = self.pula_odpowiedzi[nr_pytania][i]

        pygame.mixer.music.load("przegrana.mp3")
        pygame.mixer.music.play()
        messagebox.showinfo("PORAŻKA", "Przegrałeś :( Poprawna odpowiedź: " + str(poprawna_odpowiedz))
        self.informacja_o_wygranej(nr_pytania)

    def informacja_o_wygranej(self, nr_pytania):
        if nr_pytania < 2:
            messagebox.showinfo("WYGRANA", "Twoja wygrana: 0 zł")
        elif (nr_pytania >= 2 and nr_pytania < 8):
            messagebox.showinfo("WYGRANA", "Twoja wygrana: gwarantowany 1 000 zł")
        else:
            messagebox.showinfo("WYGRANA", "Twoja wygrana: gwarantowane 40 000 zł")
        self.master.destroy()
        ekran_startowy()
#==========================================================#

# Poza klasą: funkcja tworząca okienko i wywołująca klasę.

def ekran_startowy():
    Okno_Startowe = Tk()
    ekran_1 = AplikacjaGUI_1(Okno_Startowe)
    Okno_Startowe.mainloop()

ekran_startowy()
