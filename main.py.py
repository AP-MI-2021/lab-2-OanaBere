from math import sqrt
def printMenu():
    print ('1. Dati o valoare pentru verificarea conjecturii lui Goldbach ')
    print ('2. Verificarea conjecturii lui Goldbach')
    print ('3. Dati o valoare si un numar de pasi confrom cerintei 4 ')
    print ('4. Radicalul unui numar folosind metoda lui Newton (afisarea aproximarii)')
    print ('5. Iesire')

def verificare_prim(a):

    if a < 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(3, int(sqrt(a)) + 1, 2):
        if a % i == 0:
            return False
    return True


def get_goldbach(n):
    """
    :param n: numar natural
    :return: doua numere prime, un minim si un maxim, a caror suma este egala cu n
    """

    for a in range(1, int(n / 2)):
        if verificare_prim(a):
            b = n - a
            if verificare_prim(b):
                return a, b

# functie care returneaza aproximarea radacinei unui numar folosind metoda Newton dupa un anumit numar de pasi

def get_newton_sqrt(n, steps):
    """
    :param n: numarul dat
    :param steps:numarul de pasi
    :return:float
    """
    x = n
    # numar iteratii
    count = 0

    while (1):
        count += 1

        # calcularea celui mai apropiat x
        root = 0.5 * (x + (n / x))

        # verificarea numarului de iteratii
        if (count == steps):
            break

        # Update root
        x = root

    return root


def test_get_newton_sqrt():
    # radicalul numarului 4 folosind 2 pasi
    assert get_newton_sqrt(4, 2) == 2.05


    # radicalul numarului 5 folosind 2 pasi
    assert get_newton_sqrt(5, 2) == 2.3333333333333335



test_get_newton_sqrt()

def main():
    while True:
        printMenu()
        optiune = input('Alegeti optiunea: ')
        if optiune == "1":
            n= int(input("n = "))
        elif optiune == "2":
            print(get_goldbach(n))
        elif optiune == "3":
            n = int(input("n = "))
            steps = int(input("m = "))
        elif optiune == "4":
            print(get_newton_sqrt(n, steps))
        elif optiune == "5":
            break

main()
