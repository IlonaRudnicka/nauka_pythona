# najprostszy sposob definiowania obiektu

    #pass jest to po prostu miejsce dla funkcjonalnosci, ktora bedzie dodana pozniej
    # metode mozna wywolac, ale nic nie zwroci
    # pass moze byc uzyte w ciele (a bodu, ktore nic nie robi)

# przyklad:
#def odejmij (a,b):
#    pass
# bo nie wiemy, jak napisac klase odejmij, ale chcemy, zeby dzialalo


# self reprezentuje instancje klasy, dzieki uzyciu self
#my mozemy miec dostep do wlasciwosci i metod klasy w Pythonie

#tworzenie obiektu realizujemy przez tzw. konstruktor - jest to spejalna metoda,
#ktora jest wykonywana, kiedy tworzymy nasz obiekt.
#W Pythonie taka funkcje pelni metoda __init__
class Paletka:
    def __init__(self, kolor):
        self.kolor_obiektu = kolor
        print(f"Utworzylismy obiekt o kolorze {self.kolor_obiektu} - ID: {id(self)}")
    #pass #instrukcja nullowa (od null) - cos jak komentarz, ale interpreter tego nie ignoruje

#tworzymy obiekt na podstawie klasy, podajemy nazwe obiektu (paletka_a) i wywolujemy konstruktor klasy (Paletka())

def testklasy():
    paletka_a = Paletka("czerwony")
    paletka_b = Paletka("niebieski")
    print("*******************************")
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne wlasciwosci i metody:")
    print(dir(paletka_a))
    print("*******************************")
    print(f"Obiekt typu {type(paletka_b)} zawiera od razu pewne wlasciwosci i metody:")
    print(dir(paletka_b))
    print("*******************************")
    print(f"Kolor dla paletka_a: {paletka_a.kolor_obiektu}")
    print(f"Kolor dla paletka_b: {paletka_b.kolor_obiektu}")

#f-string
#val = 'Python course'
#print (f"Rezultat zwracany przez nasza zmienna to {val}")

#name = 'Beata'
#age = 23
#print(f"Hello, my name is {name} and I am {age} years old")
