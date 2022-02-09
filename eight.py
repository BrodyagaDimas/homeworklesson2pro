integer_number=12345

while integer_number>0:
    if integer_number%10 == 5:
        print ("Да")
        break
    integer_number=integer_number//10
else:print ("Нет")