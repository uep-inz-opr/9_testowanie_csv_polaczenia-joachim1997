import unittest
from unittest import TestCase
import csv

class Polaczenia:

    def __init__(self, plik_wejsciowy):

        self.plik_wejsciowy = plik_wejsciowy
        self.dane = self.wczytaj_dane()

    def wczytaj_dane(self):

        dane_dict = dict()

        with open(self.plik_wejsciowy, "r") as plik_csv:

            csvreader = csv.reader(plik_csv, delimiter=",")
            header = next(csvreader)

            for row in csvreader:
                polaczenie = int(row[0])

                if polaczenie not in dane_dict:
                    dane_dict[polaczenie] = 0

                dane_dict[polaczenie] += 1

            return dane_dict

    def pobierz_najczesciej_dzwoniacego(self):

        return max(self.dane.items(), key=lambda polaczenie:polaczenie[1])

if __name__ == "__main__":

    print(Polaczenia(input()).pobierz_najczesciej_dzwoniacego())
