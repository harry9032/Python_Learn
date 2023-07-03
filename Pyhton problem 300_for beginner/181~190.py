# 181
apartment = [["101", "102"], ["201", "202"], ["302", "303"]]
# 182
list1 = [["average", 100, 300, 200, 400], ["price", 80, 400, 900, 300]]
# 183
stock = {"open": [100, 300, 400], "close": [300, 100, 4000]}
# 184
stock = {"10/10": [90, 100, 123], "10/11": [1000, 300, 20000]}
# 185
print(apartment[0][0])
print(apartment[0][1])
print(apartment[1][0])
print(apartment[1][1])
print(apartment[2][0])
print(apartment[2][1])
for a in apartment:
    for b in a:
        print(b)
# 186
for a in apartment[::-1]:
    for b in a:
        print(b)
# 187
for a in apartment[::-1]:
    for b in a[::-1]:
        print(b)
# 188
for a in apartment:
    for b in a:
        print(b)
        print("//////")
# 189
for a in apartment:
    for b in a:
        print(b)
    print("///")
# 190
for a in apartment:
    for b in a:
        print(b)
print("////")