# a = int(input("ВВедите число1"))
# b = int(input("ВВедите число2"))
# c = int(input("ВВедите число3"))
# d = int(input("ВВедите число4"))


# mid_num = (a + b + c)/4
# print(round(mid_num,2))
kov = 0
a = int(input("ВВедите число1"))
kov = kov + 1
sum = 0
mid = 0

while a != 0:
    print("Вы ввели", kov, "чисел")
    sum = sum + a
    print("Сумма чисел равна",sum)
    print("Цикл продолжается")
    a = int (input("ВВедит числоA"))
    kov = kov + 1