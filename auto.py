class Auto:
    def __init__(self, ps):
        """Konstruktor für die Auto-Klasse mit PS als Attribut."""
        self.ps = ps

    def __repr__(self):
        """
        Repräsentation des Objekts für die Entwickler-/Debug-Ausgabe.
        Beispielsweise: Auto(50 PS)
        """
        return f"Auto({self.ps} PS)"
    
    def __str__(self):
        """
        String-Repräsentation für den Nutzer. 
        Kann identisch zu __repr__ gestaltet sein oder abweichen.
        """
        return f"{self.ps} PS"
    
    def __add__(self, other):
        """
        Addition: a1 + a2 -> Summe ihrer PS.
        Gibt entweder die Summe als Integer zurück (110) 
        oder erzeugt ein neues Auto-Objekt. 
        Hier geben wir direkt den Integer-Wert zurück.
        """
        if isinstance(other, Auto):
            return self.ps + other.ps
        else:
            return NotImplemented
    
    def __sub__(self, other):
        """
        Subtraktion: a1 - a2 -> Differenz ihrer PS.
        Gibt einen Integer zurück.
        """
        if isinstance(other, Auto):
            return self.ps - other.ps
        else:
            return NotImplemented
    
    def __mul__(self, other):
        """
        Multiplikation: a1 * a2 -> Produkt ihrer PS.
        Gibt einen Integer zurück.
        """
        if isinstance(other, Auto):
            return self.ps * other.ps
        else:
            return NotImplemented

    def __eq__(self, other):
        """
        Vergleich auf Gleichheit: a1 == a2
        Vergleicht die PS.
        """
        if isinstance(other, Auto):
            return self.ps == other.ps
        else:
            return NotImplemented

    def __lt__(self, other):
        """
        Kleiner-Vergleich: a1 < a2
        Vergleicht die PS.
        """
        if isinstance(other, Auto):
            return self.ps < other.ps
        else:
            return NotImplemented

    def __gt__(self, other):
        """
        Größer-Vergleich: a1 > a2
        Vergleicht die PS.
        """
        if isinstance(other, Auto):
            return self.ps > other.ps
        else:
            return NotImplemented


# --- TESTBEREICH ---

if __name__ == "__main__":
    a1 = Auto(50)
    a2 = Auto(60)

    # Überprüfung der einzelnen Magic Methods
    print("a1 =", a1)             # Ausgabe: 50 PS
    print("a2 =", a2)             # Ausgabe: 60 PS

    # Addition
    print("a1 + a2 =", a1 + a2)   # Ausgabe: 110

    # Subtraktion
    print("a1 - a2 =", a1 - a2)   # Ausgabe: -10
    print("a2 - a1 =", a2 - a1)   # Ausgabe: 10

    # Multiplikation
    print("a1 * a2 =", a1 * a2)   # Ausgabe: 3000

    # Vergleichsoperationen
    print("a1 == a2 ->", a1 == a2)  # False
    print("a1 < a2  ->", a1 < a2)   # True
    print("a1 > a2  ->", a1 > a2)   # False
