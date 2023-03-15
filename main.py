import time

startTime = time.time()
print(f"Let od 1970: {startTime/60/60/24/365}")
print(time.localtime())
local = time.localtime()
print("Dnes je {}. {}. {}.".format(local[2], local[1], local[0]))

import calendar

month = calendar.month(2019, 11)
print("Kalendář na tento měsíc")
print(month)
