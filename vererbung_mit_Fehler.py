class Tee:
    def __init__(self, name, blattart):
        # Typprüfungen, um potenzielle Fehler bei der Initialisierung abzufangen
        if not isinstance(name, str):
            raise TypeError("Das Attribut 'name' muss ein String sein.")
        if not isinstance(blattart, str):
            raise TypeError("Das Attribut 'blattart' muss ein String sein.")
        if not name.strip():
            raise ValueError("Der 'name' darf nicht leer sein.")
        if not blattart.strip():
            raise ValueError("Die 'blattart' darf nicht leer sein.")

        self.name = name
        self.blattart = blattart

    def beschreibung(self):
        """Gibt eine kurze Beschreibung des Tees zurück."""
        return f"{self.name} ist ein Tee aus {self.blattart}."

    def zubereiten(self):
        """
        Diese Methode sollte in jeder Unterklasse überschrieben werden.
        Falls sie nicht überschrieben wird, wird ein NotImplementedError ausgelöst.
        """
        raise NotImplementedError("Diese Methode sollte in der Subklasse implementiert werden.")


class GruenerTee(Tee):
    def __init__(self):
        # Hier werden gültige Strings übergeben
        super().__init__("Grüner Tee", "grünen Teeblättern")

    def zubereiten(self):
        return "Grünen Tee bei 80°C für 2-3 Minuten ziehen lassen."


class SchwarzerTee(Tee):
    def __init__(self):
        super().__init__("Schwarzer Tee", "schwarzen Teeblättern")

    def zubereiten(self):
        return "Schwarzen Tee bei 100°C für 3-5 Minuten ziehen lassen."


class KraeuterTee(Tee):
    def __init__(self):
        super().__init__("Kräutertee", "getrockneten Kräutern")

    def zubereiten(self):
        return "Kräutertee bei 90°C für 5-7 Minuten ziehen lassen."


if __name__ == "__main__":
    # Teesorten-Liste
    teesorten = [GruenerTee(), SchwarzerTee(), KraeuterTee()]

    for tee in teesorten:
        try:
            # Mögliche Fehlerquellen:
            # - falsche Implementierung der Subklassen
            # - NotImplementedError, wenn zubereiten() nicht überschrieben
            # - TypeError, ValueError aus dem Konstruktor
            beschr = tee.beschreibung()
            zubereitungs_hinweis = tee.zubereiten()

            print(beschr)
            print(zubereitungs_hinweis)
            print("---")

        except NotImplementedError as nie:
            print(f"Fehler (NotImplementedError): {nie}")
        except (TypeError, ValueError) as e:
            print(f"Fehler bei der Initialisierung oder Verwendung: {e}")
        except Exception as e:
            # Fängt alle anderen nicht spezifizierten Fehler ab
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
