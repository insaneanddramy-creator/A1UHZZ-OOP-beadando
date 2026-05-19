from berles import Berles


class Autokolcsonzo:
    def __init__(self, nev):
        self._nev = nev
        self._autok = []
        self._berlesek = []

    @property
    def nev(self):
        return self._nev

    def auto_hozzaadasa(self, auto):
        self._autok.append(auto)

    def autok_listazasa(self):
        if not self._autok:
            print("Nincs autó a rendszerben.")
            return

        print("\nElérhető autók:")
        for auto in self._autok:
            print(auto.adatok())

    def berlesek_listazasa(self):
        if not self._berlesek:
            print("Nincs aktuális bérlés.")
            return

        print("\nAktuális bérlések:")
        for index, berles in enumerate(self._berlesek, start=1):
            print(f"{index}. {berles.adatok()}")

    def auto_keresese(self, rendszam):
        for auto in self._autok:
            if auto.rendszam.lower() == rendszam.lower():
                return auto
        return None

    def auto_elerheto(self, auto, datum):
        for berles in self._berlesek:
            if berles.auto == auto and berles.datum == datum:
                return False
        return True

    def auto_berlese(self, rendszam, datum, berlo_nev):
        auto = self.auto_keresese(rendszam)

        if auto is None:
            raise ValueError("Nincs ilyen rendszámú autó.")

        if not self.auto_elerheto(auto, datum):
            raise ValueError("Az autó ezen a napon már foglalt.")

        uj_berles = Berles(auto, datum, berlo_nev)
        self._berlesek.append(uj_berles)

        return auto.berleti_dij

    def berles_lemondasa(self, rendszam, datum):
        for berles in self._berlesek:
            if berles.auto.rendszam.lower() == rendszam.lower() and berles.datum == datum:
                self._berlesek.remove(berles)
                return True

        raise ValueError("Nem található ilyen bérlés.")