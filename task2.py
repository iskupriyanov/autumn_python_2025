# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
#
# Преобразуйте переменную age в Boolean
# age = "123abc"
#
# Преобразуйте переменную flag в Boolean
# flag = 1
#
# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
#
# Преобразуйте значение 0 и 1 в Boolean
#
# Преобразуйте False в строку

age = "23"
age_1 = int(age)
foo = '23abc'
foo_1 = int(foo[:2])
print (type(age_1))
print (type(foo_1))

age2 = "123abc"
age2 = bool(age2)
print(type(age2))

flag = 1
flag_1 = bool(flag)
print (type(flag_1))

str_one = "Privet"
str_ine = bool(str_one)
str_two = ""
str_two = bool(str_two)
print(type(str_one))
print(type(str_two))