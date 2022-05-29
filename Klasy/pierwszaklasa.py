# najprostszy sposob definiowania obiektu

    #pass jest to po prostu miejsce dla funkcjonalnosci, ktora bedzie dodana pozniej
    # metode mozna wywolac, ale nic nie zwroci
    # pass moze byc uzyte w ciele (a bodu, ktore nic nie robi)

# przyklad:
#def odejmij (a,b):
#    pass
# bo nie wiemy, jak napisac klase odejmij, ale chcemy, zeby dzialalo

class Paletka:
    pass #instrukcja nullowa (od null) - cos jak komentarz, ale interpreter tego nie ignoruje

#tworzymy obiekt na podstawie klasy, podajemy nazwe obiektu (paletka_a) i wywolujemy konstruktor klasy (Paletka())

def testklasy():
    paletka_a = Paletka()
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne wlasciwosci i metody:")
    print(dir(paletka_a))

#f-string
#val = 'Python course'
#print (f"Rezultat zwracany przez nasza zmienna to {val}")

#name = 'Beata'
#age = 23
#print(f"Hello, my name is {name} and I am {age} years old")
