import unittest
from ka.poker_simulator import (
    erstelle_deck,
    ist_paar,
    ist_drilling,
    ist_vierling,
    ist_flush,
    ist_straight,
    ist_full_house,
    ist_straight_flush,
)

class TestPokerMethods(unittest.TestCase):

    def setUp(self):
        self.deck = erstelle_deck()

    def test_ist_paar(self):
        karten = [("Herz", "2"), ("Karo", "2"), ("Pik", "3"), ("Kreuz", "4"), ("Herz", "5")]
        self.assertTrue(ist_paar(karten))

    def test_ist_drilling(self):
        karten = [("Herz", "2"), ("Karo", "2"), ("Pik", "2"), ("Kreuz", "4"), ("Herz", "5")]
        self.assertTrue(ist_drilling(karten))

    def test_ist_vierling(self):
        karten = [("Herz", "2"), ("Karo", "2"), ("Pik", "2"), ("Kreuz", "2"), ("Herz", "5")]
        self.assertTrue(ist_vierling(karten))

    def test_ist_flush(self):
        karten = [("Herz", "2"), ("Herz", "3"), ("Herz", "4"), ("Herz", "5"), ("Herz", "6")]
        self.assertTrue(ist_flush(karten))

    def test_ist_straight(self):
        karten = [("Herz", "2"), ("Karo", "3"), ("Pik", "4"), ("Kreuz", "5"), ("Herz", "6")]
        self.assertTrue(ist_straight(karten))

    def test_ist_full_house(self):
        karten = [("Herz", "2"), ("Karo", "2"), ("Pik", "2"), ("Kreuz", "3"), ("Herz", "3")]
        self.assertTrue(ist_full_house(karten))

    def test_ist_straight_flush(self):
        karten = [("Herz", "2"), ("Herz", "3"), ("Herz", "4"), ("Herz", "5"), ("Herz", "6")]
        self.assertTrue(ist_straight_flush(karten))

if __name__ == "__main__":
    unittest.main()
