#instrukcje warunkowe
#lab4

import math
def zad1():
    liczba = float(input("Podaj liczbę zmiennoprzecinkową: "))

    if liczba < 0:
        liczba = -liczba

    print("Wartość bezwzględna tej liczby to:", liczba)


def zad2(liczba):
    if liczba > 0:
        return 1
    elif liczba < 0:
        return -1
    else:
        return 0


def zad3():
    liczba1 = float(input("Podaj pierwszą liczbę zmiennoprzecinkową: "))
    liczba2 = float(input("Podaj drugą liczbę zmiennoprzecinkową: "))

    if liczba2 != 0:
        wynik = liczba1 / liczba2
        print(f"Wynik dzielenia {liczba1} przez {liczba2} to {wynik}")
    else:
        print("Nie można dzielić przez zero")


def zad4():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))

    if a != 0:
        x = -b/a
        print(f"Pierwiastek tego równania to {x}")
    else:
        print("Brak wartości odpowiadającej za współczynnik kierunkowy")



#zmodyfikowa tak żeby wyrzucało też najmniejszą wartość
def zad5():
    liczba1 = float(input("Podaj pierwszą liczbę zmiennoprzecinkową: "))
    liczba2 = float(input("Podaj drugą liczbę zmiennoprzecinkową: "))
    liczba3 = float(input("Podaj trzecią liczbę zmiennoprzecinkową: "))

    temp=0
    if liczba1>liczba2:
        temp=liczba1
    elif liczba2>liczba1:
        temp=liczba2
    elif liczba3>temp:
        temp=liczba3

    print(temp)


#zmodyfikować tak, żeby zwracało też najmniejszą wartość
def max3(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z
def zad6():
    liczba1 = float(input("Podaj pierwszą liczbę zmiennoprzecinkową: "))
    liczba2 = float(input("Podaj drugą liczbę zmiennoprzecinkową: "))
    liczba3 = float(input("Podaj trzecią liczbę zmiennoprzecinkową: "))

    najwieksza = max3(liczba1, liczba2, liczba3)

    print("Największa liczba to:", najwieksza)





def zad7():
    bok1 = float(input("Podaj pierwszy bok trójkąta: "))
    bok2 = float(input("Podaj drugi bok trójkąta: "))
    bok3 = float(input("Podaj trzeci bok trójkąta: "))

    if bok1 + bok2 > bok3 and bok2 + bok3 > bok1 and bok1 + bok3 > bok2:
        obwod = bok1 + bok2 + bok3
        p = obwod / 2
        pole = math.sqrt(p * (p - bok1) * (p - bok2) * (p - bok3))
        print(f"Pole tego trójkąta wynosi {pole}, a obwód {obwod}")
    else:
        print("To nie są boki trójkąta! Kończę program.")




def zad8():

    # Funkcja do sprawdzania, czy podane boki mogą tworzyć trójkąt
    def poprawne_boki(a, b, c):
        return a + b > c and a + c > b and b + c > a

    # Funkcja do obliczania pola trójkąta z wykorzystaniem wzoru Herona
    def pole_trojkata(a, b, c):
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Funkcja do obliczania obwodu trójkąta
    def obwod_trojkata(a, b, c):
        return a + b + c

    # Wczytanie długości boków od użytkownika
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    c = float(input("Podaj długość boku c: "))

    # Sprawdzenie, czy podane boki tworzą trójkąt
    if poprawne_boki(a, b, c):
        pole = pole_trojkata(a, b, c)
        obwod = obwod_trojkata(a, b, c)
        print("Pole trójkąta wynosi:", pole)
        print("Obwód trójkąta wynosi:", obwod)
    else:
        print("Podane boki nie mogą tworzyć trójkąta.")


def main():
    #zad1()

    #zad2
    # liczba = float(input("Podaj liczbę zmiennoprzecinkową: "))
    # znak = zad2(liczba)
    #
    # if znak == 1:
    #     print("Znak liczby to: 1 (Dodatnia)")
    # elif znak == -1:
    #     print("Znak liczby to: -1 (Ujemna)")
    # else:
    #     print("Znak liczby to: 0")


    #zad3()
    #zad4()
    #zad5()
    #zad6()
    #zad7()
    #zad8()


main()
