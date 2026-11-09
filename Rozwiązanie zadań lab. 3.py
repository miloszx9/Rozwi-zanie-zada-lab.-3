# Zadanie 1
paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Pozostałe paliwo: {paliwo} litrów, czas: {czas} s")
    paliwo -= paliwo_zużyte_na_s
    czas += 1

print("Koniec lotu.")


# Zadanie 2
licznik_pierwszych = 0
licznik = 2
pierwsze = []

while licznik_pierwszych < 10:
    czy_pierwsza = True
    d = 2
    while d * d <= licznik:
        if licznik % d == 0:
            czy_pierwsza = False
            break
        d += 1
    if czy_pierwsza:
        pierwsze.append(str(licznik))
        licznik_pierwszych += 1
    licznik += 1

print(",".join(pierwsze))


# Zadanie 3
ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
liczba_bloków = 5
liczba_lokali = 10

for ulica in ulice:
    for blok in range(1, liczba_bloków + 1):
        for lokal in range(1, liczba_lokali + 1):
            print(f"Ulica: {ulica}, Blok: {blok}, Lokal: {lokal}")


# Zadanie 4 (dodatkowe)
x = int(input("Podaj liczbę przyjaciół: "))
n = int(input("Podaj liczbę zamówionych potraw: "))

ceny = []
i = 0
while i < n:
    cena = float(input(f"Podaj cenę potrawy {i+1}: "))
    ceny.append(cena)
    i += 1

suma_cen = sum(ceny)
srednia_cena = suma_cen / n if n > 0 else 0
liczba_osob = x + 1  # przyjście z grupą x przyjaciół + Ty
rachunek_na_osobe = suma_cen / liczba_osob if liczba_osob > 0 else 0

print(f"Średnia cena potrawy: {srednia_cena:.2f} zł")
print(f"Do zapłaty na osobę (dla {liczba_osob} osób): {rachunek_na_osobe:.2f} zł")


# Zadanie 5
lista_liczb = list(range(80, -1, -4))
print(lista_liczb)


# Zadanie 6
while True:
    liczba = int(input("Podaj liczbę całkowitą (ujemna kończy program): "))
    if liczba < 0:
        print("Wykryto liczbę ujemną. Koniec pętli.")
        break
    print(f"Podano: {liczba}")


# Zadanie 7
# A) Wersja z pętlą while i continue
n = int(input("Podaj liczbę studentów (n): "))
suma_punktow = 0
licznik = 0

print("Wprowadź punkty (0-100):")
while licznik < n:
    punkty = float(input(f"Punkty studenta {licznik+1}: "))
    if punkty < 0 or punkty > 100:
        print("Nieprawidłowa liczba punktów! Pomijam.")
        continue
    suma_punktow += punkty
    licznik += 1

srednia = suma_punktow / n if n > 0 else 0
print(f"Średnia punktów w grupie: {srednia}")

# B) Wersja z pętlą nieskończoną i break
suma_punktow_b = 0
licznik_b = 0
print("\nWprowadzanie punktów (wpisz liczbę ujemną aby zakończyć):")
while True:
    punkty = float(input("Podaj punkty (0-100, lub < 0 aby przerwać): "))
    if punkty < 0:
        break
    if punkty > 100:
        print("Punkty poza zakresem (0-100), pomijamy.")
        continue
    suma_punktow_b += punkty
    licznik_b += 1

srednia_b = suma_punktow_b / licznik_b if licznik_b > 0 else 0
print(f"Średnia punktów (wersja B): {srednia_b}")


# Zadanie 8
tekst = "Python jest super"
print("Zerowy znak:", tekst[0])
print("Ostatni znak:", tekst[-1])
print("Co drugi, od zerowego:", tekst[::2])
print("Co trzeci, od pierwszego:", tekst[1::3])
print("Od dziesiątego do ostatniego:", tekst[10:])
print("Od końca do początku:", tekst[::-1])


# Zadanie 9
# 1. Wczyta imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
imie = input("Podaj imię: ")
print(f"Witaj {imie}")

# 2. Wczyta wiek oraz wyświetli tekst „Twój wiek to: ” oraz wczytany wiek.
wiek = input("Podaj wiek: ")
print(f"Twój wiek to: {wiek}")

# 3. Wczyta imię i nazwisko i wyświetli inicjały.
imie_nazw = input("Podaj imię i nazwisko: ")
czesci = imie_nazw.split()
if len(czesci) >= 2:
    inicjaly = czesci[0][0].upper() + czesci[1][0].upper()
    print(f"Inicjały: {inicjaly}")
else:
    print("Podano za mało danych.")

# 4. Wczyta łańcuch i wyświetli go pięć razy.
lancuch = input("Podaj łańcuch znaków: ")
print((lancuch + "\n") * 5)

# 5. Wczyta dwa łańcuchy, a w trzecim zapamięta połączone te dwa łańcuchy.
l1 = input("Podaj pierwszy łańcuch: ")
l2 = input("Podaj drugi łańcuch: ")
l3 = l1 + l2
print(f"Połączone łańcuchy: {l3}")

# 6. Wczyta dwa łańcuchy, a w trzecim zapamięta pierwszą połowę napisu (dla pierwszego z nich)
l_A = input("Podaj pierwszy łańcuch do wyznaczenia połowy: ")
polowa_lA = l_A[:len(l_A)//2]
print(f"Pierwsza połowa pierwszego łańcucha: {polowa_lA}")