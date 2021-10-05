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
    test1 = get_newton_sqrt(4, 2)
    print('get_newton_sqrt(4, 2)', test1)

    # radicalul numarului 5 folosind 2 pasi
    test2 = get_newton_sqrt(5, 2)
    print('get_newton_sqrt(5, 2)', test2)


test_get_newton_sqrt()
