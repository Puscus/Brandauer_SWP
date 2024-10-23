import random
from collections import Counter


farben = ["Herz", "Karo", "Pik", "Kreuz"]
symbole = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]


deck = [(farbe, symbol) for farbe in farben for symbol in symbole]


def ziehe_fuenf_karten(deck):
    return random.sample(deck, 5)


def ist_paar(karten):
    symbole = [symbol for _, symbol in karten]
    symbol_haeufigkeit = Counter(symbole)
    return 2 in symbol_haeufigkeit.values()


def ist_drilling(karten):
    symbole = [symbol for _, symbol in karten]
    symbol_haeufigkeit = Counter(symbole)
    return 3 in symbol_haeufigkeit.values()


def ist_vierling(karten):
    symbole = [symbol for _, symbol in karten]
    symbol_haeufigkeit = Counter(symbole)
    return 4 in symbol_haeufigkeit.values()


def ist_flush(karten):
    farben = [farbe for farbe, _ in karten]
    return len(set(farben)) == 1


def ist_straight(karten):
    symbole = [symbol for _, symbol in karten]
    symbol_werte = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]
    indices = sorted([symbol_werte.index(s) for s in symbole])
    return indices == list(range(indices[0], indices[0] + 5))


def ist_full_house(karten):
    symbole = [symbol for _, symbol in karten]
    symbol_haeufigkeit = Counter(symbole)
    werte = symbol_haeufigkeit.values()
    return 3 in werte and 2 in werte


def ist_straight_flush(karten):
    return ist_straight(karten) and ist_flush(karten)


def simuliere_pokerhands(n):
    kombinationen = {
        "Paar": 0,
        "Drilling": 0,
        "Vierling": 0,
        "Flush": 0,
        "Straight": 0,
        "Full House": 0,
        "Straight Flush": 0,
    }

    for _ in range(n):
        karten = ziehe_fuenf_karten(deck)

        if ist_straight_flush(karten):
            kombinationen["Straight Flush"] += 1
        elif ist_vierling(karten):
            kombinationen["Vierling"] += 1
        elif ist_full_house(karten):
            kombinationen["Full House"] += 1
        elif ist_flush(karten):
            kombinationen["Flush"] += 1
        elif ist_straight(karten):
            kombinationen["Straight"] += 1
        elif ist_drilling(karten):
            kombinationen["Drilling"] += 1
        elif ist_paar(karten):
            kombinationen["Paar"] += 1

    return kombinationen


def berechne_prozentuale_anteile(kombinationen, gesamtanzahl):
    for kombi, anzahl in kombinationen.items():
        anteil = (anzahl / gesamtanzahl) * 100
        print(f"{kombi}: {anteil:.2f}%")


n = 10000
kombinationen = simuliere_pokerhands(n)
berechne_prozentuale_anteile(kombinationen, n)
