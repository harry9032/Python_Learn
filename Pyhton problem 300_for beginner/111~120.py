# 111
a = input("입력:")
print(a * 2)
# 112
b = input("입력: ")
print(int(b) - 10)
# 113
c = input("입력: ")
if int(c) % 2 == 0:
    print("짝수")
else:
    print("홀수")
# 114
d = input("입력하세요: ")
if int(c) > 235:
    print(225)
else:
    print(int(c) + 20)
# 115
e = input("입력: ")
E = int(e) - 20
if E < 0:
    print(0)
elif E > 255:
    print(255)
else:
    print(E)
# 116
clock = input("현재시간: ")
if clock[-2:] == '00':
    print("정각입니다")
else:
    print("정각이 아닙니다.")
# 117
fruit = ["apple", "pare", "banana"]
user = input()
if user in fruit:
    print("정답")
else:
    print("틀렸습니다")
# 118
investment_list = ["APPLE", "LG", "MS", "K"]
INVEST = input()
if INVEST in investment_list:
    print("nice")
else:
    print("BADD")
# 119
fruit = {"spring": "strawberry", "summer": "tomato", "winter": "none"}
Fruit_input = input()
if Fruit_input in fruit:
    print("Good")
else:
    print("wrong")
# 120
Fruit_input_value = input()
if Fruit_input_value in fruit.values():
    print("goood")
else:
    print("False")
