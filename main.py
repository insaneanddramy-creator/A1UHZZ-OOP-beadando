from datetime import datetime, date

from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles
from autokolcsonzo import Autokolcsonzo


def datum_bekerese():
    datum_szoveg = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ")

    try:
        datum = datetime.strptime(datum_szoveg, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Hibás dátumformátum. Helyes formátum: ÉÉÉÉ-HH-NN")

    if datum < date.today():
        raise ValueError("Múltbeli dátumra nem lehet autót bérelni.")

    return datum


def rendszer_inditasa():
    kolcsonzo = Autokolcsonzo("Dóra Autókölcsönző")

    auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 15000, 5)
    auto2 = Szemelyauto("DEF-456", "Suzuki Swift", 12000, 5)
    auto3 = Teherauto("GHI-789", "Ford Transit", 22000, 1200)

    kolcsonzo.auto_hozzaadasa(auto1)
    kolcsonzo.auto_hozzaadasa(auto2)
    kolcsonzo.auto_hozzaadasa(auto3)

    kolcsonzo._berlesek.append(Berles(auto1, date(2026, 5, 25), "Kovács Anna"))
    kolcsonzo._berlesek.append(Berles(auto2, date(2026, 5, 26), "Nagy Péter"))
    kolcsonzo._berlesek.append(Berles(auto3, date(2026, 5, 27), "Tóth Béla"))
    kolcsonzo._berlesek.append(Berles(auto1, date(2026, 5, 28), "Szabó Réka"))

    return kolcsonzo


def menu_megjelenitese():
    print("\n--- AUTÓKÖLCSÖNZŐ RENDSZER ---")
    print("1 - Autók listázása")
    print("2 - Autó bérlése")
    print("3 - Bérlés lemondása")
    print("4 - Aktuális bérlések listázása")
    print("0 - Kilépés")


def main():
    kolcsonzo = rendszer_inditasa()

    print(f"Üdvözlünk a(z) {kolcsonzo.nev} rendszerében!")

    while True:
        menu_megjelenitese()
        valasztas = input("Válassz egy menüpontot: ")

        try:
            if valasztas == "1":
                kolcsonzo.autok_listazasa()

            elif valasztas == "2":
                kolcsonzo.autok_listazasa()
                rendszam = input("Add meg a bérelni kívánt autó rendszámát: ")
                datum = datum_bekerese()
                berlo_nev = input("Add meg a bérlő nevét: ")

                ar = kolcsonzo.auto_berlese(rendszam, datum, berlo_nev)
                print(f"Sikeres bérlés. Fizetendő összeg: {ar} Ft")

            elif valasztas == "3":
                kolcsonzo.berlesek_listazasa()
                rendszam = input("Add meg a lemondani kívánt bérlés autójának rendszámát: ")
                datum = datum_bekerese()

                kolcsonzo.berles_lemondasa(rendszam, datum)
                print("A bérlés sikeresen lemondva.")

            elif valasztas == "4":
                kolcsonzo.berlesek_listazasa()

            elif valasztas == "0":
                print("Kilépés a programból.")
                break

            else:
                print("Érvénytelen menüpont.")

        except ValueError as hiba:
            print(f"Hiba: {hiba}")


if __name__ == "__main__":
    main()