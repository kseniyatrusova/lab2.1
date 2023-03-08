
n = ""
while n != "стоп":
    n = input("Введите слово")
    if n == "стоп": break
    if "ф" in str(n): print("Ого! Это редкое слово!")
    else: print("Эх, это не очень редкое слово")
