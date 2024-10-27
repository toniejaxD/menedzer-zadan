# main.py

from zadania import Zadanie, ZadaniePriorytetowe, ZadanieRegularne, ManagerZadan


#funkcja menu
def wyswietl_menu():
    """
    Wyświetla menu główne aplikacji menedżera zadań.
    """
    print("\n--- Menedżer Zadań ---")
    print("1. Dodaj zadanie")
    print("2. Usuń zadanie")
    print("3. Oznacz zadanie jako wykonane")
    print("4. Edytuj zadanie")
    print("5. Wyświetl wszystkie zadania")
    print("6. Sortuj zadania według terminu wykonania")
    print("7. Zapisz zadania do pliku")
    print("8. Wczytaj zadania z pliku")
    print("9. Wyjście")

#po kliknięciu 1 opcji będzie się wyswietlać wybór pomiędzy prorytowe, regularne czy zwykłe
def dodaj_zadanie(manager):
    """
    Dodaje nowe zadanie na podstawie danych wprowadzonych przez użytkownika.

    :param manager: Obiekt klasy ManagerZadan, który zarządza listą zadań.
    """
    #input pobiera informacje od użytkownika gdy poda dane w konsoli
    typ = input("Wybierz typ zadania (1 - Priorytetowe, 2 - Regularne, 3 - Zwykłe): ")
    tytul = input("Podaj tytuł zadania: ")
    opis = input("Podaj opis zadania: ")
    termin = input("Podaj termin wykonania (YYYY-MM-DD): ")

    if typ == '1':
        priorytet = input("Podaj priorytet (niski, średni, wysoki): ").lower()
        try:
            zadanie = ZadaniePriorytetowe(tytul, opis, termin, priorytet)
            manager.dodaj_zadanie(zadanie)
        except ValueError as e:
            print(e)
    elif typ == '2':
        powtarzalnosc = input("Podaj powtarzalność (np. codziennie, cotygodniowo): ")
        zadanie = ZadanieRegularne(tytul, opis, termin, powtarzalnosc)
        manager.dodaj_zadanie(zadanie)
    elif typ == '3':
        zadanie = Zadanie(tytul, opis, termin)
        manager.dodaj_zadanie(zadanie)
    else:
        print("Nieprawidłowy wybór typu zadania.")

#po kliknięciu 2 opcji będzie można usunać danego zadania według numeru listy
def usun_zadanie(manager):
    """
    Usuwa zadanie na podstawie numeru zadania podanego przez użytkownika.

    :param manager: Obiekt klasy ManagerZadan, który zarządza listą zadań.
    """
    manager.wyswietl_zadania()
    try:

        #za pomocą int(input())Konwertuje dane wpisane przez użytkownika na liczbę całkowitą
        indeks = int(input("Podaj numer zadania do usunięcia: ")) - 1
        if 0 <= indeks < len(manager.lista_zadan):
            zadanie = manager.lista_zadan[indeks]
            manager.usun_zadanie(zadanie)
        else:
            print("Nieprawidłowy numer zadania.")
    except ValueError:
        print("Proszę podać prawidłowy numer.")

#po kliknięciu 3 opcji będzie można oznaczyć jako wykonane zadanie
def oznacz_jako_wykonane(manager):
    """
    Oznacza zadanie jako wykonane na podstawie numeru zadania podanego przez użytkownika.

    :param manager: Obiekt klasy ManagerZadan, który zarządza listą zadań.
    """
    manager.wyswietl_zadania()
    try:
        indeks = int(input("Podaj numer zadania do oznaczenia jako wykonanego: ")) - 1
        if 0 <= indeks < len(manager.lista_zadan):
            zadanie = manager.lista_zadan[indeks]
            manager.oznacz_jako_wykonane(zadanie)
        else:
            print("Nieprawidłowy numer zadania.")
    except ValueError:
        print("Proszę podać prawidłowy numer.")

#po kliknięciu 4 opcji będzie można edytować danego zadania według numeru zadań
def edytuj_zadanie(manager):
    """
    Edytuje zadanie na podstawie numeru zadania podanego przez użytkownika.

    :param manager: Obiekt klasy ManagerZadan, który zarządza listą zadań.
    """
    manager.wyswietl_zadania()
    try:
        indeks = int(input("Podaj numer zadania do edycji: ")) - 1
        if 0 <= indeks < len(manager.lista_zadan):
            zadanie = manager.lista_zadan[indeks]
            nowy_tytul = input(f"Podaj nowy tytuł (obecny: {zadanie.tytul}) lub naciśnij Enter, aby pominąć: ")
            nowy_opis = input(f"Podaj nowy opis (obecny: {zadanie.opis}) lub naciśnij Enter, aby pominąć: ")
            nowy_termin = input(
                f"Podaj nowy termin (YYYY-MM-DD) (obecny: {zadanie.termin_wykonania.strftime('%Y-%m-%d')}) lub naciśnij Enter, aby pominąć: ")
            manager.edytuj_zadanie(zadanie, nowy_tytul or None, nowy_opis or None, nowy_termin or None)
        else:
            print("Nieprawidłowy numer zadania.")
    except ValueError:
        print("Proszę podać prawidłowy numer.")

#po kliknięciu 6 przycisku będzie sortować według dat
def sortuj_zadania(manager):
    """
    Sortuje listę zadań według terminu wykonania.

    :param manager: Obiekt klasy ManagerZadan, który zarządza listą zadań.
    """
    #sort(key=...): Sortuje listę zadań według daty wykonania
    #lambda zadanie: zadanie.termin_wykonania: Lambda to krótka
    # funkcja, która mówi, żeby sortować zadania według terminu wykonania.
    manager.lista_zadan.sort(key=lambda zadanie: zadanie.termin_wykonania)
    print("Zadania posortowane według terminu wykonania.")


def main():
    """
    Główna funkcja aplikacji, obsługująca interakcję użytkownika z programem.
    """
    manager = ManagerZadan()

    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            dodaj_zadanie(manager)
        elif wybor == '2':
            usun_zadanie(manager)
        elif wybor == '3':
            oznacz_jako_wykonane(manager)
        elif wybor == '4':
            edytuj_zadanie(manager)
        elif wybor == '5':
            manager.wyswietl_zadania()
        elif wybor == '6':
            sortuj_zadania(manager)
        elif wybor == '7':
            manager.zapisz_do_pliku()
        elif wybor == '8':
            manager.wczytaj_z_pliku()
        elif wybor == '9':
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Proszę spróbować ponownie.")

if __name__ == "__main__":
    main()