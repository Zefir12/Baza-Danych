import random
import os
import os.path
from Funkcje_i_zmienne import *
import sys


def main():
    if not path.exists('Dane'):
        os.system("md Dane")
    if not path.exists('KopiaDanych'):
        os.system("md KopiaDanych")

    if path.exists('Dane/nazwa.txt') and path.exists('Dane/dzien.txt') and path.exists('Dane/miesiac.txt') and path.exists('Dane/rok.txt') and path.exists('Dane/wegle.txt') and path.exists('Dane/tluszcze.txt') and path.exists('Dane/bialka.txt'):
        indeksfile = open('Dane/indeksy.txt', 'r')
        bgryh=int(indeksfile.readline())
        file = open('Dane/nazwa.txt', 'r').read()
        file1 = open('Dane/dzien.txt', 'r').read()
        file5 = open('Dane/miesiac.txt', 'r').read()
        file6 = open('Dane/rok.txt', 'r').read()
        file2 = open('Dane/wegle.txt', 'r').read()
        file3 = open('Dane/tluszcze.txt', 'r').read()
        file4 = open('Dane/bialka.txt', 'r').read()

        file = file.split('\n')
        file1 = file1.split('\n')
        file2 = file2.split('\n')
        file3 = file3.split('\n')
        file4 = file4.split('\n')
        file5 = file5.split('\n')
        file6 = file6.split('\n')

        listaa=[]
        listab=[]
        listac=[]
        listad=[]
        listae=[]
        listaf=[]
        listag=[]

        for line in file:
            listaa.append(line)
        for line in file1:
            listab.append(line)
        for line in file2:
            listac.append(line)
        for line in file3:
            listad.append(line)
        for line in file4:
            listae.append(line)
        for line in file5:
            listaf.append(line)
        for line in file6:
            listag.append(line)

        i = 0
        while i < bgryh:
            lista.append(Jedzenie(listaa[i],listab[i],listaf[i],listag[i],listac[i],listad[i],listae[i],i))
            i += 1


        i = 0
        for b in lista:
            if i == b.indeks:
                slownik_wegle[i] = b.węglowodany
                slownik_tluszcze[i] = b.tluszcze
                slownik_bialka[i] = b.bialka
                slownik_nazwa[i] = b.nazwa
                slownik_dzien[i] = b.dzien
                slownik_miesiac[i] = b.miesiac
                slownik_rok[i] = b.rok
                i += 1
    else:
        czyszczeniepliku('Dane/nazwa.txt')
        czyszczeniepliku('Dane/dzien.txt')
        czyszczeniepliku('Dane/miesiac.txt')
        czyszczeniepliku('Dane/rok.txt')
        czyszczeniepliku('Dane/wegle.txt')
        czyszczeniepliku('Dane/tluszcze.txt')
        czyszczeniepliku('Dane/bialka.txt')
        f = open('Dane/indeksy.txt','w')
        f.write('0')
        f.close()
        czyszczeniepliku('KopiaDanych/nazwakopia.txt')
        czyszczeniepliku('KopiaDanych/dzienkopia.txt')
        czyszczeniepliku('KopiaDanych/miesiackopia.txt')
        czyszczeniepliku('KopiaDanych/rokkopia.txt')
        czyszczeniepliku('KopiaDanych/weglekopia.txt')
        czyszczeniepliku('KopiaDanych/tluszczekopia.txt')
        czyszczeniepliku('KopiaDanych/bialkakopia.txt')
        f = open('KopiaDanych/indeksykopia.txt','w')
        f.write('0')
        f.close()

    print('Witaj w bazie danych')

    while True:
        print('Wybierz opcje: \n1.Zapisz dane w bazie \n2.Szukaj danych w bazie \n3.Generownie sztucznych wpisów w bazie danych \n4.Wyświetlanie całej bazy dnych \n5.Czyszczenie bazy danych i reset programu \n6.Tworzenie kopii zapasowej \n7.Przywracanie kopii zapasowej i reset programu \n8.Moduł sortowania \n9.Wyjście ')
        menuopcje = input()
        os.system("cls")
        if menuopcje=='1':
            print('--------------------Moduł Zapisywania-------------------')
            zmiennaindeks=len(lista)
            lista.append(Jedzenie(input('Podaj nazwe: '),input('Podaj dzien: '),input('Podaj miesiac: '),input('Podaj rok: '),input('Podaj wegle: '),input('Podaj tluszcze: '),input('Podaj bialka: '),zmiennaindeks))
            wpisywanie_do_listy(zmiennaindeks)
            zapisywanie_do_pliku()
            os.system("cls")

        elif menuopcje=='2':
            print('----------------------Moduł Szukania---------------------')
            a=int(input('Podaj po czym chcesz wyszukiwać: \n1.Nazwa\n2.Data\n3.Węglowodany\n4.Tłuszcze\n5.Białka\n6.Indeks\n'))
            if a !=6:
                print('\nIlość obiektów z tą nazwą wynosi: '+str(wyszukiwanie(a))+'\n')
            else:
                a = int(input('Podaj indeks: \n'))
                for b in lista:
                    if a == b.indeks:
                        print('Nazwa: ' + b.nazwa, '\nBiałka: ' + b.bialka, '\nTłuszcze: ' + b.tluszcze,'\nWęglowodany: ' + b.węglowodany, '\nData: ' + b.dzien + '-' + b.miesiac + '-' + b.rok, '\n')
            zapisywanie_do_pliku()
            print(input('\nPress Enter to go back '))
            os.system("cls")

        elif menuopcje=='8':
            for b in lista:
                b.sortowanie=0
            print('----------------------Moduł Sortowania---------------------')
            a = str(input('Wybierz rodzaj sortowania: \n1.Największa wartość\n2.Najmniejsza wartość\n3.Wartości z dnia/miesiąca/roku'))
            os.system('cls')

            if a == '1':
                aa=str(input('Wybierz po jakiej wartosci chcesz sortować: \n1.Białka\n2.Tłuszcze\n3.Węglowodany\n'))
                if aa == '1':
                    sortowanie('bialkarosnaco')
                    print(input('\nPress Enter to go back '))
                    os.system("cls")
                if aa == '2':
                    sortowanie('tluszczerosnaco')
                    print(input('\nPress Enter to go back '))
                    os.system("cls")
                if aa == '3':
                    sortowanie('weglerosnaco')
                    print(input('\nPress Enter to go back '))
                    os.system("cls")

            if a == '2':
                aa=str(input('Wybierz po jakiej wartosci chcesz sortować: \n1.Białka\n2.Tłuszcze\n3.Węglowodany\n'))
                if aa == '1':
                    sortowanie('bialka')
                    print(input('\nPress Enter to go back '))
                    os.system("cls")
                if aa == '2':
                    sortowanie('tluszcze')
                    print(input('\nPress Enter to go back '))
                    os.system("cls")
                if aa == '3':
                    sortowanie('wegle')
                    print(input('\nPress Enter to go back '))
                    os.system("cls")

            if a == '3':
                a=str(input('Wybierz opcje: \n1.Wypisz wszystkie produkty z podanej daty\n2.Podaj sumy i średnie poszczególnych wartości z podanej daty \n'))
                b = str(input('Podaj rok: '))
                c = str(input('\nPodaj miesiac: '))
                d = str(input('\nPodaj dzień: \n'))
                if a =='1':
                    os.system('cls')
                    zmiennailosc=0
                    for bb in lista:
                        if b == bb.rok or b=='0':
                            if c==bb.miesiac or c=='0':
                                if d==bb.dzien or d=='0':
                                    print('Indeks: ' + str(bb.indeks))
                                    print('Nazwa: ' + bb.nazwa, '\nBiałka: ' + bb.bialka, '\nTłuszcze: ' + bb.tluszcze,
                                          '\nWęglowodany: ' + bb.węglowodany,
                                          '\nData: ' + bb.dzien + '-' + bb.miesiac + '-' + bb.rok, '\n')
                                    zmiennailosc+=1
                    print('\nIlosc produktów z podanej daty wynosi: '+str(zmiennailosc)+'\n')
                    print(input('\nPress Enter to go back '))
                    os.system("cls")

                if a == '2':
                    zmiennailosc = 0
                    sumawegli = 0
                    sumatluszczy = 0
                    sumabialek = 0
                    os.system('cls')
                    for bb in lista:
                        if b == bb.rok or b == '0':
                            if c == bb.miesiac or c == '0':
                                if d == bb.dzien or d == '0':
                                    zmiennailosc += 1
                                    sumawegli += int(bb.węglowodany)
                                    sumatluszczy += int(bb.tluszcze)
                                    sumabialek += int(bb.bialka)
                    print('Ilość produktów: '+str(zmiennailosc)+'\nSuma białek: '+str(sumabialek)+'\nSuma tłuszczy: '+str(sumatluszczy)+'\nSuma węglowodanów: '+str(sumawegli)+'\n')
                    sredniewegle=sumawegli/zmiennailosc
                    srednietluszcze=sumatluszczy/zmiennailosc
                    sredniebialka=sumabialek/zmiennailosc
                    print('\nŚrednia ilość białek: '+str(sredniebialka)+'\nŚrednia ilość tłuszczy: '+str(srednietluszcze)+'\nŚrednia ilość węglowodanów: '+str(sredniewegle)+'\n')
                    print(input('\nPress Enter to go back '))
                    os.system("cls")


        elif menuopcje=='3':
            a=int(input('Podaj ile chcesz wygenerować sztuczych wpisów w bazie danych: '))
            i=0
            while i < a:
                procentygeneracji=(i/a)*100
                procentygeneracji=round(procentygeneracji,2)
                os.system("cls")
                pasekladowania(procentygeneracji)
                zmiennaindeks = len(lista)
                lista.append(Jedzenie(generator_produktow[random.randint(0,len(generator_produktow)-1)],str(random.randint(1,31)),str(random.randint(1,12)),str(random.randint(2000,2019)),str(random.randint(1,200)),str(random.randint(1,200)),str(random.randint(1,200)), zmiennaindeks))
                wpisywanie_do_listy(zmiennaindeks)
                zapisywanie_do_pliku()
                i+=1
            zapisywanie_do_pliku()
            print(input('\nGenerowanie zakonczone sukcesem\nWciśnij enter aby powrocic '))
            os.system("cls")


        elif menuopcje=='4':
            print('---------------------Moduł Szukania po indeksach----------------------')
            for b in lista:
                print('Indeks: '+str(b.indeks))
                print('Nazwa: '+b.nazwa,'\nBiałka: '+b.bialka,'\nTłuszcze: '+b.tluszcze,'\nWęglowodany: '+b.węglowodany,'\nData: '+b.dzien+'-' +b.miesiac+'-' +b.rok,'\n')
            print(input('\nPress Enter to go back '))
            os.system("cls")



        elif menuopcje == '5':
            print('----------------------Czyszczenie bazy danych-------------------------')
            czyszczeniepliku('Dane/nazwa.txt')
            czyszczeniepliku('Dane/dzien.txt')
            czyszczeniepliku('Dane/miesiac.txt')
            czyszczeniepliku('Dane/rok.txt')
            czyszczeniepliku('Dane/wegle.txt')
            czyszczeniepliku('Dane/tluszcze.txt')
            czyszczeniepliku('Dane/bialka.txt')
            file = open('Dane/indeksy.txt', 'w')
            file.write('0')
            file.close()
            break


        elif menuopcje == '6':
            os.system("Moduł_tworzenia_kopizapasowej.py")

        elif menuopcje == '9':
            break

        elif menuopcje == '7':
            os.system('Moduł_wczytywania_kopizapasowej.py')
            break

        else:
            print('Błędna Opcja\n')







