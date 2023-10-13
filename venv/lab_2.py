#Zadanie 1- obliczanie wartości wyrażenia

a= 512-282
b= 47*48 + 5
rownanie = a/b
print(rownanie)

#lub
rownanie1=(512-282)/ (47 * 48 + 5)
print(rownanie1)

"""
Autor: Michalina Sobkiewicz
Program oblicza i wyświetla wynik równania
"""


def zad1():
    rownanie=(512-282) / (47 * 48 + 5)
    print(rownanie)


# Napisz program, który pobiera od użytkownika wartość,
# a następnie przypisuje ją do zmiennej x. Następnie program wypisuje ciąg
# x, 2x, 3x, 4x, 5x oddzielony trzema myślnikami.
def zad2():
    LiczbaCalkowita = int(input('Wprowadź liczbę calkowitą: '))

    print(str(LiczbaCalkowita) + '---' + str(LiczbaCalkowita * 2) + '---' + str(LiczbaCalkowita*3)+
          '---'+ str(LiczbaCalkowita*4) + '---' + str(LiczbaCalkowita*5))


#Napisz program, który pobiera od użytkownika dwie liczby
# zmiennoprzecinkowe i mnoży je przez siebie. Wynik wyświetl na ekranie.
def zad3():
    pierwsza_liczba=float(input('Wprowadź pierwszą liczbę zmiennoprzecinkową: '))
    druga_liczba=float(input('Wprowadź drugą liczbę zmiennoprzecinkową: '))

    print(pierwsza_liczba * druga_liczba)



#Napisz program, który poprosi użytkownika o wpisanie wagi w kilogramach
# #i przekonwertuje podaną wartość na funty (kilogram ma około 2,2 funta).
def zad4():
    kg=float(input('Wprowadź wagę w kilogramach: '))
    print('jest to około ' + str(kg * 2.2) + ' funtów.')




#Napisz program, który wypisuje sumę pierwszych dziesięciu liczb całkowitych dodatnich
def zad5():

    suma = 0

    for liczba in range(1, 11):
        suma += liczba

    print("Suma pierwszych dziesięciu liczb całkowitych dodatnich wynosi:", suma)

# Napisz program, który drukuje iloczyn pierwszych dziesięciu liczb całkowitych dodatnich
def zad6():

    suma = 1

    for liczba in range(1, 11):
        suma *= liczba

    print("Iloczyn pierwszych dziesięciu liczb całkowitych dodatnich wynosi:", suma)


#Napisz program, który wypisuje sumę dni pierwszych trzech miesięcy dowolnego roku przestępnego.
def zad7():
    styczeń=31
    luty=29
    marzec=31

    suma= styczeń + luty + marzec
    print("Suma dni w pierwszych trzech miesiącach roku przestępnego wynosi: ", suma)


#Załóżmy, że żyjemy i zarabiamy 20 lat temu... Pozostawiamy pieniądze na lokacie.
# Kapitał początkowy wynosi 1000 zł, oprocentowanie wynosi 6%,
# a liczba kapitalizacji w ciągu roku k=1. Napisz program, który obliczy kapitalizację odsetek po pierwszym,
# po drugim i po trzecim roku na lokacie.
def zad8():
    kap_pocz=1000
    oprocentowanie=0.06
    l_kapitalizacji=1

    pierwszy_rok= kap_pocz * (1+oprocentowanie)
    drugi_rok=pierwszy_rok * (1+oprocentowanie)
    trzeci_rok=drugi_rok * (1+oprocentowanie)

    print(pierwszy_rok)
    print(drugi_rok)
    print(trzeci_rok)



def main():
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6()
    zad7()
    zad8()

main()

























