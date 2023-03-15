import datetime

from osoba import Osoba

print("Zadejte datum narození: (př.: 1.1.2000)")

inp = input()
narozeni = datetime.datetime.strptime(inp, "%d.%m.%Y").date()
os = Osoba(narozeni)

vek = os.spocitejVek()
dni = os.zbytekDni()

print("Je ti {} let a narozeniny máš za {} dní.".format(vek, dni))
