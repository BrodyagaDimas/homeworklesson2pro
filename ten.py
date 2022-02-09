n=int(input("Введите число: "))

count = 0
for i in range (1,n+1):
    m=n
    while m>=5:
        if m%10 == 5:
            count += 1
    m=m//10
print ("Количество цифр пять = ", count)
