import random

def ziehung():
    zahlen = list(range(1, 46))
    lotto_zahlen = []

    for _ in range(6):  # 6 Zahlen sollen gezogen werden
        index = random.randint(0, len(zahlen) - 1)
        lotto_zahlen.append(zahlen[index])  # Zahl zur Ergebnisliste hinzufügen
        zahlen.pop(index)  # Zahl aus der Liste entfernen

    return lotto_zahlen


def statistik():
    statistik_dict = {i: 0 for i in range(1, 46)}
    
    for _ in range(1000):  # 1000 Ziehungen
        lotto_zahlen = ziehung()
        for zahl in lotto_zahlen:
            statistik_dict[zahl] += 1  # Häufigkeit der gezogenen Zahl erhöhen

    return statistik_dict


def main():
    print("Gezogene Zahlen:", ziehung())
    
    statistik_auswertung = statistik()
    print("\nStatistik nach 1000 Ziehungen:")
    
    for zahl, haeufigkeit in statistik_auswertung.items():
        print(f"Zahl {zahl}: {haeufigkeit} mal gezogen")


if __name__ == "__main__":
    main()
