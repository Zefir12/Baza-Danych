from Funkcje_i_zmienne import *
import os

print('----------------------Wczytywanie kopi zapasowej danych---------------------')
file = open('KopiaDanych/nazwakopia.txt', 'r').read()
file1 = open('KopiaDanych/dzienkopia.txt', 'r').read()
file5 = open('KopiaDanych/miesiackopia.txt', 'r').read()
file6 = open('KopiaDanych/rokkopia.txt', 'r').read()
file2 = open('KopiaDanych/weglekopia.txt', 'r').read()
file3 = open('KopiaDanych/tluszczekopia.txt', 'r').read()
file4 = open('KopiaDanych/bialkakopia.txt', 'r').read()

indeksfile = open('KopiaDanych/indeksykopia.txt', 'r')
strefeddf = int(indeksfile.readline())
indekskopia = open('Dane/indeksy.txt', 'w')
indekskopia.write(str(strefeddf))
indekskopia.close()

file = file.split('\n')
file1 = file1.split('\n')
file2 = file2.split('\n')
file3 = file3.split('\n')
file4 = file4.split('\n')
file5 = file5.split('\n')
file6 = file6.split('\n')
if len(file) > 1:
    filekopia = open('Dane/nazwa.txt', 'w')
    file1kopia = open('Dane/dzien.txt', 'w')
    file5kopia = open('Dane/miesiac.txt', 'w')
    file6kopia = open('Dane/rok.txt', 'w')
    file2kopia = open('Dane/wegle.txt', 'w')
    file3kopia = open('Dane/tluszcze.txt', 'w')
    file4kopia = open('Dane/bialka.txt', 'w')

    for line in file:
        filekopia.write(line)
        filekopia.write('\n')
    for line in file1:
        file1kopia.write(line)
        file1kopia.write('\n')
    for line in file2:
        file2kopia.write(line)
        file2kopia.write('\n')
    for line in file3:
        file3kopia.write(line)
        file3kopia.write('\n')
    for line in file5:
        file5kopia.write(line)
        file5kopia.write('\n')
    for line in file6:
        file6kopia.write(line)
        file6kopia.write('\n')
    x = len(file4) - 1
    for line in file4:
        xd = (1 - (x / (len(file4) - 1))) * 100
        xd = round(xd, 2)
        os.system("cls")
        pasekladowania(xd)
        x -= 1
        file4kopia.write(line)
        file4kopia.write('\n')
    filekopia.close()
    file1kopia.close()
    file2kopia.close()
    file3kopia.close()
    file4kopia.close()
    file5kopia.close()
    file6kopia.close()
else:
    print('Baza danych jest pusta, nie ma co kopiować\n')