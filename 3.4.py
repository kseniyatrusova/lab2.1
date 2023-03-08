import random
c = 0
b = 0
while b != 3:
    s = random.randint(0,100)
    x = random.randint(0,100)
    k = str(s) + "+" + str(x) + "="
    n = input(str(k))
    if int(n) == int(s+x):
        c += 1
        print ("Правильно")
    else:
        b += 1
        print ("Ответ неверный")
    if b == 3:
        print ("Игра окончена. Правильных ответов:",c)
        break

