# 171
price = [2000, 3000, 4000, 5000]
for a in range(4):
    print(price[a])
# 172
for a in range(4):
    print(a, price[a])
# 173
for a in range(4):
    print(4 - a, price[a])
# 174
for a in range(1, 4):
    print(90+10*a, price[a])
# 175
my_list = ["a", "b", "c", "d", "e", "f"]
for a in range(3):
    print(my_list[a], my_list[a+1])
# 176
for a in range(3):
    print(my_list[a], my_list[a+1], my_list[a+2])
# 177
for a in [3, 2, 1]:
    print(my_list[a], my_list[a-1])
# 178
list1 = [100, 200, 400, 800]
for a in [0, 1, 2]:
    print(abs(list1[a+1] - list1[a]))
# 179
list2 = [100, 200, 400, 600, 800, 1000, 1300]
for a in range(4):
    print(abs((list2[a]+list2[a+1]+list2[a+2])/3))
# 180
low1 = [100, 200, 300, 400, 500]
high1 = [150, 300, 430, 880, 1000]
volatitiy = []
for i in range(len(low1)):
    volatitiy.append(high1[i]-low1[i])
