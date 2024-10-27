#biblioteka datetime: służy
# do manipulacji datami i czasem w Pythonie.
# Umożliwia konwersję stringów na obiekty daty
# oraz formatowanie dat do czytelnej postaci.

from datetime import datetime
import time

def zmierz_czas(funkcja):
    """
    Dekorator do mierzenia czasu wykonania funkcji.

    Args:
        funkcja (callable): Funkcja, której czas wykonania ma być mierzony.

    Returns:
        callable: Funkcja opakowana w mierzenie czasu.
    """
    def wewnetrzna(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        end = time.time()
        print(f"Czas wykonania {funkcja.__name__}: {end - start:.4f} sekundy")
        return wynik
    return wewnetrzna

#klasa Zadanie odpowiedzialna za reprezentację poszczególnych zadań
class Zadanie:
    """
    Reprezentuje zadanie do wykonania.

    Attributes:
        tytul (str): Tytuł zadania.
        opis (str): Opis zadania.
        termin_wykonania (datetime): Termin wykonania zadania.
        wykonane (bool): Status wykonania zadania.
    """
    #Inicjalizuje atrybuty tytul, opis oraz termin_wykonania.
    def __init__(self, tytul, opis, termin_wykonania):
        """
        Inicjalizuje instancję klasy Zadanie.

            Args:
                tytul (str): Tytuł zadania.
                opis (str): Opis zadania.
                termin_wykonania (str): Termin wykonania w formacie 'YYYY-MM-DD'.

            Raises:
                ValueError: Jeśli termin wykonania nie jest w formacie 'YYYY-MM-DD'.
        """
        #self..... atrybuty które będą przechowywać informacje takie jak
        #tytuł opis
        self.tytul = tytul
        self.opis = opis
        try:
            #Próbuje skonwertować string termin_wykonania do
            # obiektu datetime za pomocą strptime z formatem %Y-%m-%d
            self.termin_wykonania = datetime.strptime(termin_wykonania, '%Y-%m-%d')

        #Jeśli format daty jest niepoprawny, podnosi ValueError z odpowiednim komunikatem.
        except ValueError:
            raise ValueError("Termin wykonania musi być w formacie YYYY-MM-DD")
        #po dodaniu będzie miał ustawiony na False czyli będzie dodawać na niewykonywane
        self.wykonane = False

#Metoda __str__, która zwraca czytelny opis zadania.
#Zwraca string zawierający tytuł, opis, termin wykonania oraz status zadania.
    def __str__(self):
        """
            Zwraca czytelny opis zadania.

            Returns:
                str: Opis zadania.
        """
        status = "Wykonane" if self.wykonane else "Do wykonania"
        return (f"Zadanie: {self.tytul}\n"
                f"Opis: {self.opis}\n"
                f"Termin wykonania: {self.termin_wykonania.strftime('%Y-%m-%d')}\n"
                f"Status: {status}\n")


#Metoda, która zmienia status zadania na wykonane (True).
    def oznacz_wykonane(self):
        self.wykonane = True

#klasa ZadaniePriorytowe dziedziczy klasą Zadanie
class ZadaniePriorytetowe(Zadanie):
    """
    Reprezentuje zadanie priorytetowe, dziedziczy z klasy Zadanie.

       Attributes:
           priorytet (str): Priorytet zadania (niski, średni, wysoki).
    """
    # #Inicjalizuje atrybuty tytul, opis, termin_wykonania prorytet.
    def __init__(self, tytul, opis, termin_wykonania, priorytet):
        """
        Inicjalizuje instancję klasy ZadaniePriorytetowe.

            Args:
                tytul (str): Tytuł zadania.
                opis (str): Opis zadania.
                termin_wykonania (str): Termin wykonania w formacie 'YYYY-MM-DD'.
                priorytet (str): Priorytet zadania (niski, średni, wysoki).

            Raises:
                ValueError: Jeśli priorytet nie jest jednym z ['niski', 'sredni', 'wysoki'].
        """

        #funkcja super() wywołuje konstruktor klasy bazowej (Zadanie)
        #dzięki temu nie będzie trzeba podawać ponownie jak przypadku klasy zadanie
        super().__init__(tytul, opis, termin_wykonania)
        #jesli dany użytkow poda co innego będzie dostawać powiadomienie w "raise ValueError..."
        if priorytet not in ['niski', 'sredni', 'wysoki']:
            raise ValueError("Priorytet musi być 'niski', 'sredni' lub 'wysoki'")
        self.priorytet = priorytet


#będzie pobierac opis zadania, a następnie dodaje do niego informację o priorytecie.
    def __str__(self):
        """
        Zwraca czytelny opis zadania priorytetowego.

            Returns:
                str: Opis zadania priorytetowego.
        """

        base_str = super().__str__()
        return base_str + f"Priorytet: {self.priorytet}\n"

#klasa ZadanieRegularne dziedziczy klasą Zadanie
class ZadanieRegularne(Zadanie):
    """
    Reprezentuje zadanie regularne, dziedziczy z klasy Zadanie.

       Attributes:
           powtarzalnosc (str): Częstotliwość powtarzania zadania (np. codziennie, cotygodniowo).
    """

    def __init__(self, tytul, opis, termin_wykonania, powtarzalnosc):
        """
        Inicjalizuje instancję klasy ZadanieRegularne.

            Args:
                tytul (str): Tytuł zadania.
                opis (str): Opis zadania.
                termin_wykonania (str): Termin wykonania w formacie 'YYYY-MM-DD'.
                powtarzalnosc (str): Częstotliwość powtarzania zadania.
        """

        #funkcja super() wywołuje konstruktor klasy bazowej (Zadanie)
        #dzięki temu nie będzie trzeba podawać ponownie jak przypadku klasy zadanie
        super().__init__(tytul, opis, termin_wykonania)
        self.powtarzalnosc = powtarzalnosc  # np. 'codziennie', 'cotygodniowo', 'comiesięcznie'

    def __str__(self):
        """
        Zwraca czytelny opis zadania regularnego.

            Returns:
                str: Opis zadania regularnego.
        """
        base_str = super().__str__()
        return base_str + f"Powtarzalność: {self.powtarzalnosc}\n"

#klasa ManagerZadan  zarządzająca listą zadań.
# Odpowiada za dodawanie, usuwanie, edytowanie,
# oznaczanie jako wykonane oraz wyświetlanie zadań.
class ManagerZadan:
    """
    Klasa zarządzająca listą zadań.

       Attributes:
           lista_zadan (list): Lista obiektów typu Zadanie.
    """

    def __init__(self):
        """
            Inicjalizuje instancję klasy ManagerZadan.
        """
        self.lista_zadan = []

#Dodaje zadanie do listy zadań
    @zmierz_czas
    def dodaj_zadanie(self, zadanie, **dodatkowe_informacje):
        """
        Dodaje zadanie do listy zadań.

            Args:
                zadanie (Zadanie): Obiekt zadania do dodania.
                **dodatkowe_informacje: Dodatkowe informacje do dodania do zadania (opcjonalne).
        """

        if zadanie in self.lista_zadan:
            print("Zadanie już istnieje w liście.")
        else:
            for klucz, wartosc in dodatkowe_informacje.items():
                setattr(zadanie, klucz, wartosc)
            self.lista_zadan.append(zadanie)
            print("Zadanie dodane.")

# Usuwa zadanie z listy
    @zmierz_czas
    def usun_zadanie(self, zadanie):
        """
        Usuwa zadanie z listy zadań.

            Args:
                zadanie (Zadanie): Obiekt zadania do usunięcia.
        """

        if zadanie in self.lista_zadan:
            self.lista_zadan.remove(zadanie)
            print("Zadanie usunięte.")
        else:
            print("Zadanie nie znalezione w liście.")

#Oznacza zadanie jako wykonane, zmieniając jego status na True.
    @zmierz_czas
    def oznacz_jako_wykonane(self, zadanie):
        """
        Oznacza zadanie jako wykonane.

            Args:
                zadanie (Zadanie): Obiekt zadania do oznaczenia.
        """

        if zadanie in self.lista_zadan:
            zadanie.oznacz_wykonane()
            print("Zadanie oznaczone jako wykonane.")
        else:
            print("Zadanie nie znalezione w liście.")

# Umożliwia edycję zadania.
    @zmierz_czas
    def edytuj_zadanie(self, zadanie, nowy_tytul=None, nowy_opis=None, nowy_termin=None):
        """
        Edytuje istniejące zadanie.

            Args:
                zadanie (Zadanie): Obiekt zadania do edycji.
                nowy_tytul (str, optional): Nowy tytuł zadania. Domyślnie None.
                nowy_opis (str, optional): Nowy opis zadania. Domyślnie None.
                nowy_termin (str, optional): Nowy termin wykonania w formacie 'YYYY-MM-DD'. Domyślnie None.
        """
        if zadanie in self.lista_zadan:
            if nowy_tytul:
                zadanie.tytul = nowy_tytul
            if nowy_opis:
                zadanie.opis = nowy_opis
            if nowy_termin:
                try:
                    zadanie.termin_wykonania = datetime.strptime(nowy_termin, '%Y-%m-%d')
                except ValueError:
                    print("Niepoprawny format daty. Termin nie został zmieniony.")
            print("Zadanie zaktualizowane.")
        else:
            print("Zadanie nie znalezione w liście.")

#Wyświetla listę zadań w czytelny sposób, numerując każde zadanie.
    def wyswietl_zadania(self):
        """
        Wyświetla listę zadań w czytelny sposób.
        """

        for i, zadanie in enumerate(self.lista_zadan, 1):
            print(f"{i}. {zadanie}")

    def zapisz_do_pliku(self, nazwa_pliku="zadania.txt"):
        """
        Zapisuje listę zadań do pliku tekstowego.

            Args:
                nazwa_pliku (str): Nazwa pliku do zapisu. Domyślnie 'zadania.txt'.
        """

        with open(nazwa_pliku, 'w') as plik:
            for idx, zadanie in enumerate(self.lista_zadan, start=1):
                plik.write(f"{idx}. {zadanie.tytul}\n")
                plik.write(f"   Opis: {zadanie.opis}\n")
                plik.write(f"   Termin wykonania: {zadanie.termin_wykonania.strftime('%Y-%m-%d')}\n")
                plik.write(f"   Status: {'Wykonane' if zadanie.wykonane else 'Do wykonania'}\n")

                if isinstance(zadanie, ZadaniePriorytetowe):
                    plik.write(f"   Priorytet: {zadanie.priorytet}\n")
                elif isinstance(zadanie, ZadanieRegularne):
                    plik.write(f"   Powtarzalność: {zadanie.powtarzalnosc}\n")

                plik.write("\n")
        print(f"Zadania zapisane do pliku {nazwa_pliku}.")

    def wczytaj_z_pliku(self, nazwa_pliku="zadania.txt"):
        """
        Wczytuje listę zadań z pliku tekstowego.

            Args:
                nazwa_pliku (str): Nazwa pliku do odczytu. Domyślnie 'zadania.txt'.
        """

        self.lista_zadan.clear()
        try:
            with open(nazwa_pliku, 'r') as plik:
                linie = plik.readlines()
                i = 0
                while i < len(linie):
                    # Sprawdź, czy linia zawiera numer zadania i tytuł
                    if linie[i].strip() and linie[i].strip()[0].isdigit():
                        # Odczytaj tytuł
                        tytul = linie[i].split(". ", 1)[1].strip()

                        # Odczytaj opis
                        opis = linie[i + 1].split(": ", 1)[1].strip()

                        # Odczytaj termin wykonania
                        termin = linie[i + 2].split(": ", 1)[1].strip()

                        # Odczytaj status zadania
                        status = linie[i + 3].split(": ", 1)[1].strip()

                        # Stwórz podstawowe zadanie
                        zadanie = Zadanie(tytul, opis, termin)
                        if status == "Wykonane":
                            zadanie.oznacz_wykonane()

                        # Sprawdź, czy zadanie ma priorytet lub powtarzalność
                        if (i + 4) < len(linie) and "Priorytet:" in linie[i + 4]:
                            priorytet = linie[i + 4].split(": ", 1)[1].strip()
                            zadanie = ZadaniePriorytetowe(tytul, opis, termin, priorytet)
                            if status == "Wykonane":
                                zadanie.oznacz_wykonane()
                            i += 5  # Przesuń indeks o 5 linii

                        elif (i + 4) < len(linie) and "Powtarzalność:" in linie[i + 4]:
                            powtarzalnosc = linie[i + 4].split(": ", 1)[1].strip()
                            zadanie = ZadanieRegularne(tytul, opis, termin, powtarzalnosc)
                            if status == "Wykonane":
                                zadanie.oznacz_wykonane()
                            i += 5  # Przesuń indeks o 5 linii

                        else:
                            i += 4  # Przesuń indeks o 4 linii dla zwykłego zadania

                        # Dodaj zadanie do listy
                        self.lista_zadan.append(zadanie)
                    else:
                        i += 1  # Przesuń indeks o 1 linie w przypadku pustych linii lub błędów
                print(f"Zadania wczytane z pliku {nazwa_pliku}.")
        except FileNotFoundError:
            print(f"Plik {nazwa_pliku} nie istnieje.")
