from auto import Auto


class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self._teherbiras = teherbiras

    @property
    def teherbiras(self):
        return self._teherbiras

    def adatok(self):
        return f"Teherautó - {self.rendszam}, {self.tipus}, {self.berleti_dij} Ft/nap, teherbírás: {self.teherbiras} kg"