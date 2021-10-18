def print_menu():
    print("1. Citire lista de nr. intregi.")
    print("2. Afisare lista fara numere prime.")
    print("3. Determinarea daca media aritmetica a unei liste este mai mare ca un nr dat n.")
    print("4. Afișarea listei obținută prin adăugarea după fiecare element numărul de div proprii ai elementului.")
    print("5. Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un tuplu în care pe prima poziție este numărul, pe a doua poziție va fi indexul elementului din listă, iar pe a treia poziție apare numărul de apariții a numărului.")

    

def citire_lista():
    """

    :return: lista citita de utilizator
    """
    lista = []
    givenString = input("Dati nr., separate prin virgule: ")
    numAsString = givenString.split(",")
    for x in numAsString:
        lista.append(int(x))
    return lista


def ListaFaraNrPrime (l):
    """
    Functia va afla din lista citita, toate numerele care nu sunt prime si le va adauga in lista rez[]
    :param l: reprezinta lista citita de utilizator
    :return: lista finala, fara numere prime
    """
    rez = []
    for x in l:
        ok = True
        if x < 2:
            ok = False
        else:
            for i in range(2, x//2 + 1):
                if x % i == 0:
                    ok = False
        if ok is False:
            rez.append(x)
    return rez

def test_ListaFaraNrPrime():
    assert ListaFaraNrPrime([2, 3, 4, 5, 6]) == [4, 6]
    assert ListaFaraNrPrime([2, 3, 5, 7]) == []
    assert ListaFaraNrPrime([1, 2, 3]) == [1]

def mediaAritmeticaMaiMareCa(l, n):
    """
    Functia va returna media aritmetica a listei citite de utilizator
    parametrii l, n: l - reprezinta lista citita de utilizator, n - nr citit de utilizator, pt care media aritmetica sa fie mai mare
    return: va returna media aritmetica a numerelor din lista l
    """
    sum_nr = 0
    count_nr = 0
    for x in l:
        sum_nr += x
        count_nr += 1
    medie_aritmetica = sum_nr // count_nr
    if medie_aritmetica > n:
        return "DA"
    else:
        return "NU"


def ListaElemCuDivProprii (l):
    """
    parametru l: reprezinta lista citita de utilizator
    return: va returna lista finala, cu nr de divizori proprii dupa fiecare element citit
    """
    rez = []
    for x in l:
        rez.append(x)
        divProp = 0
        for i in range(2, x):
            if x % i == 0:
                divProp += 1
        rez.append(divProp)
    return rez


def test_mediaAritmeticamMaiMareCa():
    assert mediaAritmeticaMaiMareCa([10, -3, 25, -1, 3, 25, 18], 10) == "DA"
    assert mediaAritmeticaMaiMareCa([1, 2, 3], 3) == "NU"
    assert mediaAritmeticaMaiMareCa([1, 2, 3], 2) == "NU"


def test_ListaElemCuDivProprii():
    assert ListaElemCuDivProprii([19, 5, 24, 12, 9]) == [19, 0, 5, 0, 24, 6, 12, 4, 9, 1]
    assert ListaElemCuDivProprii([1, 2, 3]) == [1, 0, 2, 0, 3, 0]
    assert ListaElemCuDivProprii([2, 3, 4, 6]) == [2, 0, 3, 0, 4, 1, 6, 2]


def prelucrareTuplu(l):
    """
    Functia va returna in lista rez, un tuplu, conform cerintei. Mai intai se va retine in vectorul
    de frecventa cnt = {} nr de aparitii in lista a fiecarui element. Variabila intreaga 'index' va afisa pozitia fiecarui element.
    param l: reprezinta lista citita de utilizator
    return: se va returna lista ceruta
    """
    rez = []
    cnt = {}
    for x in l:
        cnt[x] = cnt.get(x, 0) + 1
    index = 0
    for x in l:
        rez.append("(" + str(x) + ", " + str(index) + ", " + str(cnt[x]) + ")")
        index += 1
    return rez


def test_prelucrareTuplu():
    assert prelucrareTuplu([25, 13, 26, 13]) == ['(25, 0, 1)', '(13, 1, 2)', '(26, 2, 1)', '(13, 3, 2)']
    assert prelucrareTuplu([13, 13, 13, 13]) == ['(13, 0, 4)', '(13, 1, 4)', '(13, 2, 4)', '(13, 3, 4)']
    assert prelucrareTuplu([1, 2, 3]) == ['(1, 0, 1)', '(2, 1, 1)', '(3, 2, 1)']


test_prelucrareTuplu()
test_ListaElemCuDivProprii()
test_ListaFaraNrPrime()
test_mediaAritmeticamMaiMareCa()
def main():
    l = []
    while True:
        print_menu()
        optiune = input("Alegeti optiunea: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(ListaFaraNrPrime(l))
        elif optiune == "3":
            n = int(input("Dati nr.:"))
            print(mediaAritmeticaMaiMareCa(l, n))
        elif optiune == "4":
            print(ListaElemCuDivProprii(l))
        elif optiune == "5":
            print(prelucrareTuplu(l))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, reincercati!")


if __name__ == "__main__":
    main()
