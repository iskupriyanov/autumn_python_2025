#todo: Даны три точки A , B , C на числовой оси. Найти длины
# отрезков AC и BC и
# их сумму.
# Примечание: все точки получаем через функцию input().

A = int(input())
B = int(input())
C = int(input())
AB = abs(B-A)
BC = abs(C-B)
SUMM = AB+BC
print (AB)
print (BC)
print (SUMM)