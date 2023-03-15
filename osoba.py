import datetime

class Osoba:

    # Založení objektu osoba s proměnnou datum_narození
    def __init__(self, datum_narozeni):
        self.datum_narozeni = datum_narozeni

    # Počítání věku
    # Vek nejprve spočítáme nepřesně, a pak zkoušíme,
    # jestli po přidání věku k datu narození nepřesáhneme dnešek.
    # (Znamenalo by to, že osoba ještě v tomto roce narozeniny neměla).
    # Pokud přesáhneme - odečteme 1 od věku
    def spocitejVek(self):
        dnes = datetime.date.today()

        vek = dnes.year - self.datum_narozeni.year

        testDatum = self.datum_narozeni.replace(year = self.datum_narozeni.year + vek)

        if(dnes < testDatum):
            vek -= 1

        return vek

    # Počítání zbylých dní do dalších narozenin
    # Zjistíme dnešní den.
    # Zjistíme datum dalších narozenin
    # (k datu narozenin přičteme vek z "spocitejVek" a 1 rok (další narozeniny))
    # Hodnoty odečteme a zjistíme rozdíl ve dnech, kolik chybí do dalších narozenin
    def zbytekDni(self):
        dnes = datetime.date.today()
        dalsiNarozeniny = self.datum_narozeni.replace(year = self.datum_narozeni.year + self.spocitejVek() + 1)
        rozdil = dalsiNarozeniny - dnes

        return rozdil.days
