# 91
ice_cream = {"red": [300, 3], "blue": [200, 4], "yellow": [660, 6]}
print(ice_cream)
# 92
print(ice_cream["red"][0], "Won")
# 93
print(ice_cream["red"][1])
# 94
ice_cream["green"] = [500, 45]
print(ice_cream)
# 95
icecream = {'red' : 100, 'blue' : 200, 'yellow' : 300}
icecream_list = list(icecream.keys())
print(icecream_list)
# 96
icecream_values = list(icecream.values())
print(icecream_values)
# 97
print(sum(icecream_values))
# 98
new_product = {'new1': 10000, 'new2': 20000}
icecream.update(new_product)
print(icecream)
# 99
key = [1,2,3,4,5]
values = [11, 22, 33, 44, 55]
result = dict(zip(key, values))
print(result)
# 100
date = ['1/1', '1/2', '1/3', '1/4', '1/5']
price = [100, 200, 100, 200, 2300]
result1 = dict(zip(date, price))
print(result1)