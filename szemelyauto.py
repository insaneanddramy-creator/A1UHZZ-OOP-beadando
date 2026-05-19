from auto import Auto


class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ferohelyek_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self._ferohelyek_szama = ferohelyek_szama

    @property
    def ferohelyek_szama(self):
        return self._ferohelyek_szama

    def adatok(self):
        return f"Személyautó - {self.rendszam}, {self.tipus}, {self.berleti_dij} Ft/nap, férőhelyek: {self.ferohelyek_szama}"