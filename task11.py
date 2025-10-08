#  todo: Дан номер месяца (1 — январь, 2 — февраль, ...). Вывести название соответствующего
#  времени года ("зима", "весна" и т.д.).

month_num = int(input("Введите номер месяца"))
print (month_num)

if month_num == 1 or month_num==2 or month_num == 12:
    print ("зима")
elif month_num == 3 or month_num==4 or month_num == 5:
    print ("весна")
elif month_num == 6 or month_num==7 or month_num == 8:
    print ("лето")
elif month_num == 9 or month_num == 10 or month_num == 11:
    print("лето")
else:
    print ("Некорректный номер")

