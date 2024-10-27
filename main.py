#kolekcja slownik
#slownik ma pary wartosci. Klucz, wartosc - objasnienie klucza
#slownik może miec różne typy wartości
slownik = {1: "Poniedziałek", 2: "Wtorek", 7: "Niedziela", 5: True}
print(slownik)

#slownik może mieć różne typy kluczy
slownik = {1:'Ania', 'b':'Kasia'}
print(slownik)

#slownik, który ma taka sama wartość w kluczu, działa, ale jest tylko brana pod uwagę tylko ostatnia para, gdzie jakiś klucz się dubluje
slownik = {1:'Start', 2:'Stop', 1:'Półmetek'}
print(slownik)

# alternatywny sposób na utworzeni słwonika
# tu klucz nie może być liczbą, ani nie jest podawany jako string
my_dictionary = dict(piotr=40, s=2, cc=3)
print(my_dictionary)


# nie liczymy od zera. Dajemy klucz ze słownika
slownik = {1:'Ania', 2:'Kasia', 7:'Dorota'}
print(slownik[2])
print(slownik[7])
print(slownik)

#dodanie nowego elementu
slownik = {1:'Ania', 2:'Kasia', 7:'Dorota'}
print(slownik)
slownik[3] = "Środa"
slownik[4] =  False
slownik[6] = 5
slownik["Natalia"] = "aaa"
slownik[3] = 'Czwartek' #nadpisanie wartości dla klucza który już istnieje
print(slownik)

# klucze też mogą być różnego typu i muszą być unikalne
slownik = {1:'Ania', 2:'Kasia', 7:'Dorota'}
slownik["a"] = 1
slownik['a'] = 10
print(slownik)

# brak indeksu, wyrzuca wyjątek
slownik = {1:'Ania', 2:'Kasia', 7:'Dorota'}
# print(slownik[8])

# funkcja get pozwala zabezpieczyc się w drugim argumencie na niesitniejący indeks
slownik = {1:'Ania', 2:'Kasia', 7:'Dorota'}
print(slownik.get(8, "Indeks nie istnieje"))

#wyswietlanie calego slownika linia po linii

# wyswietlanie klucza
print("\nPętla dla kluczy:")
slownik = {1:'Ania', 2:'Kasia', 7:'Dorota'}
# for l in slownik:
for l in slownik.keys(): #to samo
    print(l)

#wyswietlanie wartosci
print("Pętla dla wartości: ")
slownik = {1:'Ania', 2:'Kasia', 7:'Dorota'}
for l in slownik.values():
    print(l)
#lub
for v in slownik:
    print(slownik[v])
print("--------")

# usuwanie elementow ze slownika
print("----")
slownik = {1:'Ania', 2:'Kasia', 7:'Dorota'}
print(slownik)
print(slownik.pop(1)) #podajemy klucz
print(slownik)

# Usuwanie wskazanego klucza z wartością
slownik = {1:'Ania', 2:'Kasia', 7:'Dorota'}
del slownik[2]
print(slownik)
slownik.pop(7)
print(slownik)

# dodanie nowych wartosci w jednej linii lub nadpisac istniejący
slownik = {1:'Ania', 2:'Kasia', 7:'Dorota'}
slownik.update({22: "Ada", 32: "Admin", 7: "Środa"})
print(slownik)

#można dodawać do siebie słowniki ale nie + tylko operatorem |
slownik1 = {1:'Guten Tag', 2:'Guten Abend', 'trzy':'Good morning'}
slownik2 = {1:'Czesc', 4:'hi'}
slownik3 = slownik1 | slownik2 
print(slownik3)

# wypakowanie obiektow kluczy do postaci listy
slownik = {1:'Ania', 2:'Kasia', 7:'Dorota'}
print(slownik.keys())
lista_kluczy = list(slownik.keys())
print(lista_kluczy)

#wypakowanie wartosci słownika do postaci listy
slownik = {1:'Ania', 2:'Kasia', 7:'Dorota'}
print(slownik.values())
print(list(slownik.values()))

#stworzenie słownika za pomocą tupli i listy
ages = dict([("piotr",20), ("adam",40), ("olgierd",50)])
print(ages)

#klucze, wartości i pary w słowniku
countryLeaders = {"PL": "Duda", "US": "Bidden", "GER": "Merkel"}
print(countryLeaders["PL"])
print(countryLeaders)
print(countryLeaders.items())
print(list(countryLeaders.items())) #konwersja na listę z tuplami par klucz:wartość
print(countryLeaders.keys())
print(countryLeaders.values())

countryLeaders = {"PL": "Duda", "US": "Bidden", "GER": "Merkel"}
#usuwanie ostatniego elementu kolekcji
print(countryLeaders.popitem())
print(countryLeaders)
print(countryLeaders.pop("PL"))
print(countryLeaders)

#metoda setdefault dodanie pary z domyslną wartosci dla danego klucza jezeli nie istnieje
countryLeaders = {"PL": "Duda", "US": "Bidden", "GER": "Merkel"}
# countryLeaders["FR"] = "Chirak"
countryLeaders.setdefault("FR", "Macron")
print(countryLeaders)

