import random

pocker = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
A = random.choice(pocker)
B = random.choice(pocker)

print(A, "진행하시겠습니까?")
Y_N = input()
if Y_N == 'yes':
    if A > B:
        print("승리하셨습니다")
    else:
        print("패배하셨습니다")
else:
    print("게임을 종료합니다")