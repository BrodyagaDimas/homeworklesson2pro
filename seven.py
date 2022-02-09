n = int(input("Введите число: "))
if n<0: n=-n
product = 1 if n else 0

while n:
    n, dig = divmod(n, 10)
    product *=dig
print("Произведение цифр равно: ", product)


