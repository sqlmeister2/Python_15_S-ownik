#kolekcja slownik
#slownik ma pary wartosci. Klucz, wartosc - objasnienie klucza
#slownik może miec różne typy wartości
slownik = {1: "Poniedziałek", 2: "Wtorek", 7: "Niedziela", 5: True}

#alternatywny sposób na utworzeni słwonika
my_dictionary = dict(piotr=40, s=2, cc=3)
print(my_dictionary)


#nie liczymy od zera. Dajemy index ze slownika
print(slownik[1])
print(slownik[7])
print(slownik)

#dodanie nowego elementu
slownik[3] = "Środa"
slownik[4] =  False
slownik[6] = 5
slownik["Natalia"] = "aaa"
print(slownik)

#klucze też mogą być różnego typu i muszą być unikalne
slownik["a"] = 1
print(slownik)

#brak indeksu, wyrzuca wyjątek
#print(slownik[8])

#funkcja get pozwala zabezpieczyc się w drugim argumencie na niesitniejący indeks
print(slownik.get(8, "Indeks nie istnieje"))

#wyswietlanie calego slownika linia po linii

#wyswietlanie klucza
print("\nPętla dla kluczy:")
for l in slownik:
#for l in slownik.keys(): to samo
    print(l)

#wyswietlanie wartosci
print("Pętla dla wartości: ")
for l in slownik.values():
    print(l)

#lub
for v in slownik:
    print(slownik[v])
print("--------")



#usuwanie elementow ze slownika
print("----")
print(slownik.pop(1)) #podajemy klucz
print(slownik)

#Usuwanie wsazanego klucza z wartością
del slownik[2]
print(slownik)

slownik.pop(3)
print(slownik)

#dodanie nowych wartosci w jednej linii lub nadpisac istniejący
slownik.update({22: "Ada", 32: "Admin", 7: "Środa"})
print(slownik)

print(slownik.keys())
print(slownik.keys())
lista_kluczy = list(slownik.keys())
print(lista_kluczy)

print(slownik.values())

#stworzenie słownika za pomocą tupli i listy
ages = dict([("piotr",20), ("adam",40), ("olgierd",50)])
print(ages)

countryLeaders = {"PL": "śmieć", "US": "Bidden", "GER": "Merkel"}
print(countryLeaders["PL"])
print(countryLeaders)
print(countryLeaders.items())
print(countryLeaders.keys())
print(countryLeaders.values())
#usuwanie ostatniego elementu kolekcji
print(countryLeaders.popitem())
print(countryLeaders)
print(countryLeaders.pop("PL"))
print(countryLeaders)

countryLeaders["Putin"] = "RU"
print(countryLeaders)

#metoda setdefault ustawienia domyslnej wartosci dla danego klucza jezeli nie istnieje
#countryLeaders["FR"] = "Chirak"
countryLeaders.setdefault("FR", "Macron")
print(countryLeaders)

print(countryLeaders.get("PL"))