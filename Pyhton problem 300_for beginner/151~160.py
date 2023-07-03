# 151
List = [3, -4, -34, 30, -45]
for a in List:
    if a < 0:
        print(a)
# 152
List_1 = [3, 6, 12, 134]
for a in List_1:
    if a % 3 == 0:
        print(a)
# 153
for a in List_1:
    if a % 3 == 0 and a < 20:
        print(a)
# 154
List = ["breakfast", "lunch", "dinner", "meal"]
for a in List:
    if len(a) > 3:
        print(a)
# 155
list1 = ['A', 'B', 'C', 'd']
for a in list1:
    if a.isupper():
        print(a)
# 156
for a in list1:
    if a.isupper() is False:
        print(a)
# 157
for a in List:
    print(a[0].upper(), a[1:])
# 158
List2 = ["python.py", "Hello world.c", "problem.py", "list.h", "file.h"]
for a in List2:
    print(a.split('.')[0])
# 159
for a in List2:
    if a.split('.')[1] == 'h':
        print(a)
# 160
for a in List2:
    if (a.split('.')[1] == 'h') or (a.split('.') == 'c'):
        print(a)
