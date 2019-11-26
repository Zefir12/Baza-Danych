import os.path
from os import path
import sys

slownik_wegle = {}
slownik_bialka = {}
slownik_tluszcze = {}
slownik_dzien = {}
slownik_miesiac = {}
slownik_rok = {}
slownik_nazwa = {}

generator_produktow = ['Jabłko', 'Banan', 'Kiełbasa', 'Masło', 'Kurczak', 'Wołowina', 'Jogurt', 'Majonez',
                       'Ser', 'Płatki', 'Dżem', 'Śliwka', 'Ananas', 'Parówki', 'Kalafior', 'Pizza', 'Chrzan', 'Olej']
lista = []

class Jedzenie():
    def __init__(self,nazwa,dzien,miesiac,rok,wegle,tluszcze,bialka,indeks):
        self.węglowodany=wegle
        self.bialka=bialka
        self.tluszcze=tluszcze
        self.nazwa=nazwa
        self.indeks=indeks
        self.dzien=dzien
        self.miesiac=miesiac
        self.rok = rok
        self.sortowanie=0


def wpisywanie_do_listy(zmiennaindeks):
    for b in lista:
        if zmiennaindeks == b.indeks:
            slownik_wegle[zmiennaindeks] = b.węglowodany
        if zmiennaindeks == b.indeks:
            slownik_tluszcze[zmiennaindeks] = b.tluszcze
        if zmiennaindeks == b.indeks:
            slownik_bialka[zmiennaindeks] = b.bialka
        if zmiennaindeks == b.indeks:
            slownik_nazwa[zmiennaindeks] = b.nazwa
        if zmiennaindeks == b.indeks:
            slownik_dzien[zmiennaindeks] = b.dzien
        if zmiennaindeks == b.indeks:
            slownik_miesiac[zmiennaindeks] = b.miesiac
        if zmiennaindeks == b.indeks:
            slownik_rok[zmiennaindeks] = b.rok

def pasekladowania(procenty):
    if procenty < 5:
        print(' [#                   ] '+str(procenty)+'%')
    elif procenty < 10:
        print(' [##                  ] '+str(procenty)+'%')
    elif procenty < 15:
        print(' [###                 ] '+str(procenty)+'%')
    elif procenty < 20:
        print(' [####                ] '+str(procenty)+'%')
    elif procenty < 25:
        print(' [#####               ] '+str(procenty)+'%')
    elif procenty < 30:
        print(' [######              ] '+str(procenty)+'%')
    elif procenty < 35:
        print(' [#######             ] '+str(procenty)+'%')
    elif procenty < 40:
        print(' [########            ] '+str(procenty)+'%')
    elif procenty < 45:
        print(' [#########           ] '+str(procenty)+'%')
    elif procenty < 50:
        print(' [##########          ] '+str(procenty)+'%')
    elif procenty < 55:
        print(' [###########         ] '+str(procenty)+'%')
    elif procenty < 60:
        print(' [############        ] '+str(procenty)+'%')
    elif procenty < 65:
        print(' [#############       ] '+str(procenty)+'%')
    elif procenty < 70:
        print(' [##############      ] '+str(procenty)+'%')
    elif procenty < 75:
        print(' [###############     ] '+str(procenty)+'%')
    elif procenty < 80:
        print(' [################    ] '+str(procenty)+'%')
    elif procenty < 85:
        print(' [#################   ] '+str(procenty)+'%')
    elif procenty < 90:
        print(' [##################  ] '+str(procenty)+'%')
    elif procenty < 95:
        print(' [################### ] '+str(procenty)+'%')
    else:
        print(' [####################] '+str(procenty)+'%')



def zapisywanie_do_pliku():
    file = open('Dane/nazwa.txt', 'w')
    for b in slownik_nazwa:
        file.writelines(slownik_nazwa[b])
        file.write('\n')
    file.close()
    file = open('Dane/wegle.txt', 'w')
    for b in slownik_wegle:
        file.writelines(slownik_wegle[b])
        file.write('\n')
    file.close()
    file = open('Dane/dzien.txt', 'w')
    for b in slownik_dzien:
        file.writelines(slownik_dzien[b])
        file.write('\n')
    file.close()
    file = open('Dane/miesiac.txt', 'w')
    for b in slownik_miesiac:
        file.writelines(slownik_miesiac[b])
        file.write('\n')
    file.close()
    file = open('Dane/rok.txt', 'w')
    for b in slownik_rok:
        file.writelines(slownik_rok[b])
        file.write('\n')
    file.close()
    file = open('Dane/tluszcze.txt', 'w')
    for b in slownik_tluszcze:
        file.writelines(slownik_tluszcze[b])
        file.write('\n')
    file.close()
    file = open('Dane/bialka.txt', 'w')
    for b in slownik_bialka:
        file.writelines(slownik_bialka[b])
        file.write('\n')
    file.close()
    indeksfile = open('Dane/indeksy.txt', 'w')
    indekszmiennaxdnachwile = str(len(lista))
    indeksfile.write(indekszmiennaxdnachwile)
    indeksfile.close()


def czyszczeniepliku(nazwapliku):
    file = open(nazwapliku, 'w')
    file.close()

def wyszukiwanie(poczym):
    iloscobiektow = 0
    if poczym == 1:
        a = str(input('Podaj nazwe: \n'))
        for b in lista:
            if a == b.nazwa:
                print('\nIndeks: ' + str(b.indeks))
                print('Nazwa: ' + b.nazwa, '\nBiałka: ' + b.bialka, '\nTłuszcze: ' + b.tluszcze,
                      '\nWęglowodany: ' + b.węglowodany, '\nData: ' + b.dzien + '-' + b.miesiac + '-' + b.rok, '\n')
                iloscobiektow += 1
    if poczym ==2:
        a = str(input('Podaj dzien: \n'))
        d = str(input('Podaj miesiac: \n'))
        c = str(input('Podaj rok: \n'))
        for b in lista:
            if a == b.dzien:
                if d == b.miesiac:
                    if c == b.rok:
                        print('\nIndeks: ' + str(b.indeks))
                        print('Nazwa: ' + b.nazwa, '\nBiałka: ' + b.bialka, '\nTłuszcze: ' + b.tluszcze,
                              '\nWęglowodany: ' + b.węglowodany, '\nData: ' + b.dzien + '-' + b.miesiac + '-' + b.rok, '\n')
                        iloscobiektow += 1
    if poczym ==3:
        a = str(input('Podaj Węglowodany: \n'))
        for b in lista:
            if a == b.węglowodany:
                print('\nIndeks: ' + str(b.indeks))
                print('Nazwa: ' + b.nazwa, '\nBiałka: ' + b.bialka, '\nTłuszcze: ' + b.tluszcze,
                      '\nWęglowodany: ' + b.węglowodany, '\nData: ' + b.dzien + '-' + b.miesiac + '-' + b.rok, '\n')
                iloscobiektow += 1
    if poczym ==4:
        a = str(input('Podaj tłuszcze: \n'))
        for b in lista:
            if a == b.tluszcze:
                print('\nIndeks: ' + str(b.indeks))
                print('Nazwa: ' + b.nazwa, '\nBiałka: ' + b.bialka, '\nTłuszcze: ' + b.tluszcze,
                      '\nWęglowodany: ' + b.węglowodany, '\nData: ' + b.dzien + '-' + b.miesiac + '-' + b.rok, '\n')
                iloscobiektow += 1
    if poczym ==5:
        a = str(input('Podaj białka: \n'))
        for b in lista:
            if a == b.bialka:
                print('\nIndeks: ' + str(b.indeks))
                print('Nazwa: ' + b.nazwa, '\nBiałka: ' + b.bialka, '\nTłuszcze: ' + b.tluszcze,
                      '\nWęglowodany: ' + b.węglowodany, '\nData: ' + b.dzien + '-' + b.miesiac + '-' + b.rok, '\n')
                iloscobiektow += 1
    if poczym ==6:
        a = int(input('Podaj indeks: \n'))
        for b in lista:
            if a == b.indeks:
                print('\nIndeks: ' + str(b.indeks))
                print('Nazwa: ' + b.nazwa, '\nBiałka: ' + b.bialka, '\nTłuszcze: ' + b.tluszcze,
                      '\nWęglowodany: ' + b.węglowodany, '\nData: ' + b.dzien + '-' + b.miesiac + '-' + b.rok, '\n')
                iloscobiektow += 1
    return iloscobiektow


def sortowanie(poczym):
    listazmienna=[]
    zmienna = 0
    i=0
    ii=0
    if poczym =='wegle':
        for b in lista:
            if zmienna < int(b.węglowodany) and b.sortowanie==0:
                zmienna = int(b.węglowodany)
                listazmienna=[b]
            elif zmienna == int(b.węglowodany)and b.sortowanie==0:
                listazmienna.append(b)
            if i == len(lista)-1:
                for bb in listazmienna:
                    for bbb in lista:
                        if bbb.indeks == bb.indeks:
                            bbb.sortowanie=1
                            print('\nIndeks: ' + str(bbb.indeks),'\nNazwa: ' + bbb.nazwa, '\nBiałka: ' + bbb.bialka, '\nTłuszcze: ' + bbb.tluszcze,
                                  '\nWęglowodany: --> ' + bbb.węglowodany,'<--',
                                  '\nData: ' + bbb.dzien + '-' + bbb.miesiac + '-' + bbb.rok, '\n')
            i+=1
        for b in lista:
            if b.sortowanie == 0:
                ii=1
        if ii>0:
            sortowanie('wegle')


    if poczym =='tluszcze':
        for b in lista:
            if zmienna < int(b.tluszcze) and b.sortowanie==0:
                zmienna = int(b.tluszcze)
                listazmienna=[b]
            elif zmienna == int(b.tluszcze)and b.sortowanie==0:
                listazmienna.append(b)
            if i == len(lista)-1:
                for bb in listazmienna:
                    for bbb in lista:
                        if bbb.indeks == bb.indeks:
                            bbb.sortowanie=1
                            print('\nIndeks: ' + str(bbb.indeks),'\nNazwa: ' + bbb.nazwa, '\nBiałka: ' + bbb.bialka, '\nTłuszcze: --> ' + bbb.tluszcze,'<--',
                                  '\nWęglowodany: ' + bbb.węglowodany,
                                  '\nData: ' + bbb.dzien + '-' + bbb.miesiac + '-' + bbb.rok, '\n')
            i+=1
        for b in lista:
            if b.sortowanie == 0:
                ii=1
        if ii>0:
            sortowanie('tluszcze')

    if poczym =='bialka':
        for b in lista:
            if zmienna < int(b.bialka) and b.sortowanie==0:
                zmienna = int(b.bialka)
                listazmienna=[b]
            elif zmienna == int(b.bialka)and b.sortowanie==0:
                listazmienna.append(b)
            if i == len(lista)-1:
                for bb in listazmienna:
                    for bbb in lista:
                        if bbb.indeks == bb.indeks:
                            bbb.sortowanie=1
                            print('\nIndeks: ' + str(bbb.indeks),'\nNazwa: ' + bbb.nazwa, '\nBiałka: --> ' + bbb.bialka,'<--', '\nTłuszcze: ' + bbb.tluszcze,
                                  '\nWęglowodany: ' + bbb.węglowodany,
                                  '\nData: ' + bbb.dzien + '-' + bbb.miesiac + '-' + bbb.rok, '\n')
            i+=1
        for b in lista:
            if b.sortowanie == 0:
                ii=1
        if ii>0:
            sortowanie('bialka')

    if poczym =='weglerosnaco':
        zmienna=10000
        for b in lista:
            if zmienna > int(b.węglowodany) and b.sortowanie==0:
                zmienna = int(b.węglowodany)
                listazmienna=[b]
            elif zmienna == int(b.węglowodany)and b.sortowanie==0:
                listazmienna.append(b)
            if i == len(lista)-1:
                for bb in listazmienna:
                    for bbb in lista:
                        if bbb.indeks == bb.indeks:
                            bbb.sortowanie=1
                            print('\nIndeks: ' + str(bbb.indeks),'\nNazwa: ' + bbb.nazwa, '\nBiałka: ' + bbb.bialka, '\nTłuszcze: ' + bbb.tluszcze,
                                  '\nWęglowodany: --> ' + bbb.węglowodany,'<--',
                                  '\nData: ' + bbb.dzien + '-' + bbb.miesiac + '-' + bbb.rok, '\n')
            i+=1
        for b in lista:
            if b.sortowanie == 0:
                ii=1
        if ii>0:
            sortowanie('weglerosnaco')


    if poczym =='tluszczerosnaco':
        zmienna = 10000
        for b in lista:
            if zmienna > int(b.tluszcze) and b.sortowanie==0:
                zmienna = int(b.tluszcze)
                listazmienna=[b]
            elif zmienna == int(b.tluszcze)and b.sortowanie==0:
                listazmienna.append(b)
            if i == len(lista)-1:
                for bb in listazmienna:
                    for bbb in lista:
                        if bbb.indeks == bb.indeks:
                            bbb.sortowanie=1
                            print('\nIndeks: ' + str(bbb.indeks),'\nNazwa: ' + bbb.nazwa, '\nBiałka: ' + bbb.bialka, '\nTłuszcze: --> ' + bbb.tluszcze,'<--',
                                  '\nWęglowodany: ' + bbb.węglowodany,
                                  '\nData: ' + bbb.dzien + '-' + bbb.miesiac + '-' + bbb.rok, '\n')
            i+=1
        for b in lista:
            if b.sortowanie == 0:
                ii=1
        if ii>0:
            sortowanie('tluszczerosnaco')

    if poczym =='bialkarosnaco':
        zmienna = 10000
        for b in lista:
            if zmienna > int(b.bialka) and b.sortowanie==0:
                zmienna = int(b.bialka)
                listazmienna=[b]
            elif zmienna == int(b.bialka)and b.sortowanie==0:
                listazmienna.append(b)
            if i == len(lista)-1:
                for bb in listazmienna:
                    for bbb in lista:
                        if bbb.indeks == bb.indeks:
                            bbb.sortowanie=1
                            print('\nIndeks: ' + str(bbb.indeks),'\nNazwa: ' + bbb.nazwa, '\nBiałka: --> ' + bbb.bialka,'<--', '\nTłuszcze: ' + bbb.tluszcze,
                                  '\nWęglowodany: ' + bbb.węglowodany,
                                  '\nData: ' + bbb.dzien + '-' + bbb.miesiac + '-' + bbb.rok, '\n')
            i+=1
        for b in lista:
            if b.sortowanie == 0:
                ii=1
        if ii>0:
            sortowanie('bialkarosnaco')





