# 191
data = [[2000, 3050, 2050, 1980], [7500, 2050, 2050, 1980], [15450, 15050, 15500, 14900]]
for line in data:
    for column in line:
        print(column * 1.00014)
# 192
for line in data:
    for column in line:
        print(column * 1.00014)
    print(".......")
# 193
result =[]
for line in data:
    for column in line:
        result.append(column * 1.00014)
print(result)
# 194
result1 = []
for line in data:
    result = []
    for column in line:
        result.append(column * 1.00014)
    result1.append(result)
print(result1)
# 195
ohlc = [["open", "high", "low", "close"], [100, 110, 120, 130], [200, 300, 400, 500], [300, 400, 500, 600, 700]]
for line in ohlc[1:]:
    print(line[3])
# 196
for line in ohlc[1:]:
    if line[3] > line[0]:
        print(line[3])
# 197
for line in ohlc[1:]:
    if line[2] > line[1]:
        print(line[2])
# 198
volatility = []
for line in ohlc[1:]:
    volatility.append(line[3]-line[0])
print(volatility)
# 199
for line in ohlc[1:0]:
    if line[2] > line[1]:
        print(line[3]-line[0])
# 200
total = 0
for line in ohlc[1:0]:
    total += line[3]-line[0]
print(total)