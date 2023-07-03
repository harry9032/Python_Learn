import random

poker = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

A = random.choice(poker.keys())
B = random.choice(poker)

print(A, "진행하시겠습니까?")
Y_N = input()
if Y_N == 'yes':
    if A > B:
        print("승리하셨습니다")
    else:
        print("패배하셨습니다")
else:
    print("게임을 종료합니다")