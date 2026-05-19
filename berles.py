class Berles:
    def __init__(self, auto, datum, berlo_nev):
        self._auto = auto
        self._datum = datum
        self._berlo_nev = berlo_nev

    @property
    def auto(self):
        return self._auto

    @property
    def datum(self):
        return self._datum

    @property
    def berlo_nev(self):
        return self._berlo_nev

    def adatok(self):
        return f"{self.datum} - {self.auto.rendszam} ({self.auto.tipus}) - Bérlő: {self.berlo_nev}"