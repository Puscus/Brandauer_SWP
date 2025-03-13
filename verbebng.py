class Tee:
    def __init__(self, name, blattart):
        self.name = name
        self.blattart = blattart

    def beschreibung(self):
        return f"{self.name} ist ein Tee aus {self.blattart}."

    def zubereiten(self):
        raise NotImplementedError("Diese Methode sollte in der Subklasse implementiert werden.")


class GruenerTee(Tee):
    def __init__(self):
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
    teesorten = [GruenerTee(), SchwarzerTee(), KraeuterTee()]

    for tee in teesorten:
        print(tee.beschreibung())
        print(tee.zubereiten())
