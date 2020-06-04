### Data stworzenia: 04.06.2020
### Połączenie wszystkich części kodu.
#============================================================#

import random

from tkinter import *
from tkinter import messagebox

from functools import partial # Więcej niż jeden argument dla "command".
from Pytanka import pytania_all # Zaimportowanie pytań z zewnętrznego pliku.
from Pytanka import odpowiedzi_all # Zaimportowanie odpowiedzi z zewnętrznego pliku.
from Pytanka import sprawdzenie_all # Zaimportowanie odpowiedzi z zewnętrznego pliku.
from PIL import Image, ImageTk # Dodawanie obrazków.
import tkinter.font as font # Czcionki.
import pygame # Dźwięk.
pygame.mixer.init()

#============================================================#

# EKRAN STARTOWY:
class AplikacjaGUI_1(Frame, object):
    def __init__(self, master):
        super(AplikacjaGUI_1, self).__init__(master)
        tworz_okno(master)
        self.stworz_przyciski(master)
        pygame.mixer.music.load("muzyczka_startowa.mp3")
        pygame.mixer.music.play() # Muzyka zaczyna grać.

    def stworz_przyciski(self, master):

        specjalna_czcionka = font.Font(family="Naula", size=15, weight="bold", slant="italic")

        nowa_gra = Button(self.master, text = "NOWA GRA", relief = RAISED,
                          fg = "#ffd750", bg = "#19133d", command = self.zacznij_gre)
        nowa_gra['font'] = specjalna_czcionka # Zapis z internetowego poradnika.
        nowa_gra.place(x = 350, y = 225, width=200, height=75)

        koniec = Button(self.master,text = "WYJŚCIE \nZ PROGRAMU", relief = RAISED,
                        fg = "#ffd750", bg = "#19133d", command = self.zamknij_program)
        koniec['font'] = specjalna_czcionka # Zapis z internetowego poradnika.
        koniec.place(x = 350, y = 310, width=200, height=75)

    def zacznij_gre(self):
        self.master.destroy() # Zamknięcie okna startowego.
        pygame.mixer.music.fadeout(2000) # Muzyka się wycisza (czas).
        Glowne_Okno = Tk()

#============================================================#

        # LOSOWANIE 12 PYTAŃ DO AKTUALNEJ ROZGRYWKI:

            #========================================#
            #                                        #
            #             by: Marysia                #
            #                                        #
            #========================================#

        rozgrywka_pytania = []
        rozgrywka_odpowiedzi = []
        rozgrywka_sprawdzenie = []
        wylosowane_pytania = []

        # 12, bo do gry potrzebujemy tylko 12 pytań (0-11).
        for i in range(12):
            # Losujemy z 40 pytań (0-39).
            numer_pytania = random.randint(0,39)
            # Nie może być 2 razy tego samego pytania.
            while numer_pytania in wylosowane_pytania:

                numer_pytania = random.randint(0,39)
            wylosowane_pytania.append(numer_pytania)
            rozgrywka_pytania.append(pytania_all[numer_pytania])
            rozgrywka_odpowiedzi.append(odpowiedzi_all[numer_pytania])
            rozgrywka_sprawdzenie.append(sprawdzenie_all[numer_pytania])

        # Tutaj przechodzimy do drugiej klasy (przrzucamy tam też wylosowane pytania itd.).
        ekran_2 = AplikacjaGUI_2(Glowne_Okno, rozgrywka_pytania, rozgrywka_odpowiedzi, rozgrywka_sprawdzenie)
        Glowne_Okno.mainloop()

    # Zakończenie gry z poziomu menu.
    def zamknij_program(self):
        self.master.destroy()

#============================================================#

# GŁÓWNE OKNO:
class AplikacjaGUI_2(Frame, object):

    #===========================================#
    #                                           #
    #               Konstruktor                 #
    #                                           #
    #===========================================#

    def __init__(self, master, pyt, odp, spr):
        super(AplikacjaGUI_2, self).__init__(master)
        tworz_okno(master)

        # Elementy wylosowane, przeniesione z poprzedniej klasy:
        self.pula_pytan = pyt
        self.pula_odpowiedzi = odp
        self.pula_sprawdzen = spr

        # Czcionki:
        self.specjalna_czcionka_2 = font.Font(family="Naula", size=10, weight="bold")
        self.specjalna_czcionka_3 = font.Font(family="Arial", size=10, weight="bold")

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

#============================================================#

            #========================================#
            #                                        #
            #               by: Damian               #
            #                                        #
            #========================================#


    def Prowadzacy(self, master):
        self.Hubert = Canvas(self.master)
        self.Hubert.place(x = 100, y = 0, width = 600, height = 350)
        self.zdj_Huberta = Image.open("Hubert.jpg")
        self.zdj_Huberta_Tk = ImageTk.PhotoImage(self.zdj_Huberta)
        self.Hubert.create_image(200, 200, image = self.zdj_Huberta_Tk)

    def Kola_Ratunkowe(self, master):

        self.publ_obraz = Image.open("1.png")
        self.publ_obraz = self.publ_obraz.resize((45, 45))
        self.publ_Tk = ImageTk.PhotoImage(self.publ_obraz)

        self.pol_na_pol_obraz = Image.open("2.png")
        self.pol_na_pol_obraz = self.pol_na_pol_obraz.resize((45, 45))
        self.pol_na_pol_Tk = ImageTk.PhotoImage(self.pol_na_pol_obraz)

        self.tel_obraz = Image.open("3.png")
        self.tel_obraz = self.tel_obraz.resize((45, 45))
        self.tel_Tk = ImageTk.PhotoImage(self.tel_obraz)

#============================================================#

            #========================================#
            #                                        #
            #              by: Jakub                 #
            #                                        #
            #========================================#

        self.przycisk_publ=Button(self.master, text = "publ", image = self.publ_Tk, relief = RAISED, state = DISABLED, fg = "white")
        self.przycisk_publ.place(x = 650 , y = 50, width=60, height=50)
        self.przycisk_5050=Button(self.master, text = "50/50", image = self.pol_na_pol_Tk, relief = RAISED, state = DISABLED, fg = "white")
        self.przycisk_5050.place(x = 720 , y = 50, width=60, height=50)
        self.przycisk_tel=Button(self.master, text = "tel", image = self.tel_Tk, relief = RAISED, state = DISABLED, fg = "white")
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
            relief = RAISED, state = DISABLED, font = self.specjalna_czcionka_2, bg = "#0F0A8C", fg = "white", disabledforeground="white"))
            if i == 0:
                self.guziki[i].configure(state = NORMAL)
            self.guziki[-1].place(x = 650, y = 562.5 - 40*i, width=200, height=37.5)

        # Strzałka:
        self.wskaznik_plotno = Canvas(self.master)
        self.wskaznik_plotno.place(x = 600, y = 562.5, width = 50, height = 37.5)
        self.wskaznik = Image.open("strzalka.png")
        self.wskaznik_Tk = ImageTk.PhotoImage(self.wskaznik)
        self.wskaznik_plotno.create_image(25, 20, image = self.wskaznik_Tk)

#============================================================#

    #===========================================#
    #          Koniec def. podstawowych         #
    #             elementów okna.               #
    #===========================================#

    # 1: poczatek_gry
    # -> wywołuje funckję czyszczącą pole z pytaniem i 4 odpowiedzi
    # -> zmienia kolor aktualnego pytania na złoty
    # -> wywołuje funkcję przydzielającą nowe pytanie
    # -> na każdy przycisk z $$$ można kliknąć tylko raz
    #    (stąd: DISABLED po jej wykonaniu)

    def poczatek_gry(self, nr_pytania):
        self.czyszczenie_pol()
        self.guziki[nr_pytania].configure(bg = "#600A51")
        self.komentarz_Huberta(nr_pytania)
        self.nowe_pytanie(nr_pytania)
        self.guziki[nr_pytania].configure(state = DISABLED)
        self.wlacz_kola(nr_pytania)

#============================================================#

            #========================================#
            #                                        #
            #               by: Damian               #
            #                                        #
            #========================================#

    def komentarz_Huberta(self, nr_pytania):
        komentarze = ["Pierwsze pytanie:", "Prawidłowo. Oto kolejne pytanie:",
        "Prawidłowo. Oto kolejne pytanie:",
        "Zgadza się. Następne pytanie:",
        "Całkiem nieźle sobie radzisz! Przejdźmy do następnego pytania:",
        "I to jest poprawna odpowiedź! Następne pytanie:",
        "Wygląda na to, że połowa juz za nami. A oto kolejne pytanie:",
        "Zgadza się. Następne pytanie:",
        "I to jest poprawna odpowiedź! Następne pytanie:",
        "Prawidłowo. Oto kolejne pytanie:",
        "To pytanie nie należało do najłatwiejszych, gratuluję. Tak brzmi kolejne pytanie:"
        "To wielka chwila, od miliona dzieli Cię ostatnie pytanie. Gotów? Brzmi ono tak:",
        "Gratulacje! Właśnie grasz o milion polskich złotych!"]

        komentarz = Label(self.master, text = komentarze[nr_pytania], bg='gold')
        komentarz.place(x=50, y=345, width=475, height=55)
#============================================================#

    # 2: czyszczenie_pol
    # -> czysci pole z pytaniem i 4 pola z odpowiedziami

    def czyszczenie_pol(self):
        for i in range(4):
            self.odpowiedzi[i].configure(bg="#0F0A8C", text = "")

    # 3: nowe_pytanie
    # -> wywołuje bazę pytań
    # -> wywołuję bazę odpowiedzi

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
        # Zrobione poza pętlą, żeby "lambda" odpowiednio działała

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
    # -> zmienia tło zdobytych $$$ na złoty kolor

    def info_dobra_odpowiedz(self, nr_pytania):
        pygame.mixer.music.load("aplauz.wav")
        pygame.mixer.music.play()
        messagebox.showinfo("GRATULACJE", "Poprawna odpowiedź!")
        if not (nr_pytania == 1 or nr_pytania == 6):
            self.guziki[nr_pytania].configure(bg = "lightblue", disabledforeground="darkblue")
        elif nr_pytania == 1:
            self.guziki[nr_pytania].configure(text = "Gwarantowany 1000 zł", bg = "gold", font = self.specjalna_czcionka_3, disabledforeground="darkblue")
        elif nr_pytania == 6:
            self.guziki[nr_pytania].configure(text = "Gwarantowane 40 000 zł", bg = "gold", font = self.specjalna_czcionka_3, disabledforeground="darkblue")
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
            self.wskaznik_plotno.destroy() # Usunięcie strzałki.

            # Nowa strzałka:
            self.wskaznik_plotno = Canvas(self.master)
            wartosc_przesuniecia = 522.5 - 40 * int(nr_pytania)
            self.wskaznik_plotno.place(x = 600, y = wartosc_przesuniecia, width = 50, height = 37.5)
            self.wskaznik_plotno.create_image(25, 20, image = self.wskaznik_Tk)

            self.zwolnij_guzik(nr_pytania + 1)

        else:
            messagebox.showinfo("Koniec gry", "Wygrana: " + str(kwoty[nr_pytania]))
            self.master.destroy()
            ekran_startowy()

    # 10: zwolnij_guzik
    # -> zwalnia guzik odpowiadający kolejnemu pytaniu

    def zwolnij_guzik(self, nr_do_zwolnienia):
        self.guziki[nr_do_zwolnienia].configure(state = NORMAL)

    # 11: jestes_milionerem
    # -> informuje o byciu milionerem
    # -> aplauz

    def jestes_milionerem(self):
        pygame.mixer.music.load("aplauz.wav")
        pygame.mixer.music.play()
        messagebox.showinfo("GRATULACJE", "Wygrałeś milion złotych!")
        self.master.destroy()
        ekran_startowy()

    # 12: przegrana
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

    # 13: informacja_o_wygranej
    # -> podaje wygraną kwotę;
    # -> bierze pod uwagę sumy gwarantowane

    def informacja_o_wygranej(self, nr_pytania):
        if nr_pytania < 2:
            messagebox.showinfo("WYGRANA", "Twoja wygrana: 0 zł")
        elif (nr_pytania >= 2 and nr_pytania < 8):
            messagebox.showinfo("WYGRANA", "Twoja wygrana: gwarantowany 1 000 zł")
        else:
            messagebox.showinfo("WYGRANA", "Twoja wygrana: gwarantowane 40 000 zł")
        self.master.destroy()
        ekran_startowy()
#============================================================#

# Poza klasami: funkcja wywołująca pierwszą klasę,
# funkcja umieszczająca okna na środku ekranu.

def ekran_startowy():
    Okno_Startowe = Tk()
    ekran_1 = AplikacjaGUI_1(Okno_Startowe)
    Okno_Startowe.mainloop()

# Tworzenie 2 okien, na środku ekranu:
def tworz_okno(master):
        master.title("Milionerzy.")
        master.resizable(width = False, height = False)
        szerokosc_ekranu = master.winfo_screenwidth()
        wysokosc_ekranu = master.winfo_screenheight()
        wspolrzedna_x = int((szerokosc_ekranu/2) - (900/2))
        wspolrzedna_y = int((wysokosc_ekranu/2) - (650/2))
        master.geometry("{}x{}+{}+{}".format(900, 650, wspolrzedna_x, wspolrzedna_y))
        # Powyższy zapis pozwala wyśrodkować okno na ekranie użytkownika.
        # Współrzędna "x" punktu zaczepienia: szerokość ekranu / 2 - szerokość okna /2.
        # Współrzędna "y" punktu zaczepienia: wysokość ekranu / 2 - wysokość okna /2.
        # Ostatnia linijka pozwala "wstawić" wartości w odpowiednie miejsca zapisu "szerokośćxdługość+x+y".

#============================================================#

# Uruchomienie programu:
ekran_startowy()
