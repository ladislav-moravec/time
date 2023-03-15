import datetime

print("Pro zadaný interval datumů vypíše všechny pátky 13.:")

#Zadání datumů
print("Zadejte 1. datum (př. 1.1.2000):")
input1 = input()
date1 = datetime.datetime.strptime(input1, "%d.%m.%Y").date()

print("Zadejte 2. datum:")
input2 = input()
date2 = datetime.datetime.strptime(input2, "%d.%m.%Y").date()

#delta - zvětšuje datum o den (pro testování) > do prvního pátku, pak o 7
delta = datetime.timedelta(1)
testDate = date1

print("Pátky 13.: ", end='')
while date2 > testDate:

    if (testDate.weekday() == 4): # našli jsme pátek, budeme se posouvat o 7 dní
        delta = datetime.timedelta(7)

    #day - proměnná !!! weekday() - funkce
    if (testDate.day == 13 and testDate.weekday() == 4):
        print(" {},".format(testDate), end='')

    testDate += delta

print()
