def drob (txt):                                         # Функция преобразования строки в дробь
    if txt[-2:] == "/0":                                # Предупреждение деления на ноль
        print (txt, "Попытка деления на НОЛЬ. Программа будет завершена")
        quit()                                          # Завершение программы
    a = []
    if txt.count(" ") > 0:                              # Если дробь имеет целую часть:
        a.append(txt.split(" ")[0])                     # первым элементом списка будет эта целая часть
        a.append(txt.split(" ")[1].split("/")[0])       # вторым элементом списка будет числитель
        a.append(txt.split(" ")[1].split("/")[1])       # третим элементом списка будет знаменатель
        if a[1] == "0":                                 # Если числитель = 0:
                a = [txt.split(" ")[0]]                 # в списке будет только целая часть без дробной части

    elif txt.count("/") > 0:                            # Если дробь не имеет целого числа:
        a.append("0")                                   #
        a.append(txt.split("/")[0])
        a.append(txt.split("/")[1])
    else:
        a.append(txt)



    for i in range(len(a)): a[i] = int(a[i])

    if len(a) == 1:

        a.append(a[0])
        a.append(1)
        a.remove(a[0])

    else:
        if a[0] < 0:
            a[0] = -a[0]
            a[1] = -(a[0] * a[2] + a[1])
            a.remove(a[0])
        else:
            a[1] = a[0]*a[2]+a[1]
            a.remove(a[0])

    return a

def summ (a,b,znak):                                    #Функция суммирования или вычитания двух дробей
    #print (a,b)
    if znak == "+":
        c = [a[0]*b[1]+b[0]*a[1], a[1]*b[1]]
        znak = "сложение"
    else:
        c = [a[0]*b[1]-b[0]*a[1], a[1]*b[1]]
        znak = "вычитание"
    #print (c)
    n = max(c[0],c[1])
    while n > 0:
        if c[0] % n == 0 and c[1] % n == 0:
            c[0] = int(c[0] / n)
            c[1] = int(c[1] / n)
        n -= 1

    if abs(c[0]) > abs(c[1]):
        tseloe = c[0]//c[1]
        chislitel = c[0]%c[1]
        znamenatel = c[1]
        if chislitel == 0: n = str(int(tseloe))
        else: n = str(int(tseloe))+" "+str(int(chislitel))+"/"+str(int(znamenatel))


    else:
        n = str(c[0])+"/"+str(c[1])

    ar = "первое слогаемое: {} \nвторое слогаемое: {} \nоперация: {}\nРезультат:\nнеправильная дробь: {}/{} \nправильная дробь: {}".format(a,b,znak,str(c[0]),str(c[1]),n)
    return ar

inp = input ("Введите выражение с дробями в формате \"n x/y +/- n x/y\": ")
#inp = "-1 1/2 + -5 1/2"

if inp.count(" + ") > 0:
    list = inp.split(" + ")
    znak = "+"
elif inp.count(" - ") > 0:
    list = inp.split(" - ")
    znak = "-"
else:
    print("Операция недопустима (должно быть либо сложение, либо вычитание). Программа будет завершена.")
    quit()
print (list[0],znak, list[1])
print (summ(drob(list[0]),drob(list[1]), znak))


#print(drob("2"))
#print(drob("-2"))
#print(drob("-1/2"))
#print(drob("-1 1/2"))
#print(drob("-1 1/0"))



                                                    #АВТОМАТИЧЕСКОЕ ТЕСТИРОВАНИЕ
                                                #из 100 случайных вариаций выражений
#import random
#for i in range(0,100):
#    s1 = random.choice("+-")+str(random.randint(0,10))+" "+str(random.randint(0,10))+"/"+str(random.randint(1,10))
#    if s1[:2] == "+0": s1 = s1[3:]
#    if s1[:2] == "-0": s1 = "-"+s1[3:]
#    if s1[0] == "+": s1 = s1[1:]
#    s2 = random.choice("+-") + str(random.randint(0, 10)) + " " + str(random.randint(0, 10)) + "/" + str(
#         random.randint(1, 10))
#    if s2[:2] == "+0": s2 = s2[3:]
#    if s2[:2] == "-0": s2 = "-" + s2[3:]
#    if s2[0] == "+": s2 = s2[1:]
#
#    new = s1+" "+random.choice("+-")+" "+s2
#    print (new)
#
#    if new.count(" + ") > 0:
#        list = new.split(" + ")
#        znak = "+"
#    elif inp.count(" - ") > 0:
#        list = new.split(" - ")
#        znak = "-"
#    else:
#        print("Операция недопустима (должно быть либо сложение, либо вычитание). Программа будет завершена.")
#        quit()
#    print(list[0], znak, list[1])
#    print(summ(drob(list[0]), drob(list[1]), znak))


