import datetime

print("Vypisuji součty cifet v datu pro následujících 7 dní:\n")
for i in range(1,8):
    date = datetime.date.today() + datetime.timedelta(i)
    soucet = date.day + date.month + date.year

    print("{} - {}".format(date, soucet))
