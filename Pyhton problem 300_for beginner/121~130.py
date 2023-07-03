# 121
A = input("")
if A.islower():
    print(A.upper())
else:
    print(A.lower())
# 122
score = input("score: ")
score = int(score)
if 81 <= score <= 100:
    print("A")
elif 61 <= score <= 80:
    print("B")
elif 41 <= score <= 60:
    print("C")
elif 21 <= score <= 40:
    print("D")
else:
    print("E")
# 123
money = {"dollar": 1167, "JPY": 1.096, "Euro": 1268}
money_input = input("입력: ")
num, currency = money_input.split()
print(float(num) * money[currency], "원")
# 124
A = input("number1: ")
B = input("number2: ")
C = input("number3: ")
A = int(A)
B = int(B)
C = int(C)
if A >= B and A >= C:
    print("A")
elif B >= A and B >= C:
    print("B")
else:
    print("C")
# 125
number = input("Put the number: ")
number = number.split('-')
if number == "82":
    print("korea")
else:
    print("not Korea")
# 126
mail = input("mail: ")
mail = mail[0:3]
if mail in ["001", "002", "003"]:
    print("001 is good")
else:
    print("It is hard to deliver")
# 127
ID = input("ID: ")
ID = ID.split('-')[1]
if ID in ["1", "3"]:
    print("male")
else:
    print("female")
# 128
if int(ID[1:3]) <= 8:
    print("Souel")
else:
    print("Wrong")
# 129
ID_input = input("ID: ")
ID_input = ID_input.replace("-", "")
