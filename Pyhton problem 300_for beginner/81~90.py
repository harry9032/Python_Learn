# 81
scores = [8.8, 8.9, 8.7, 8.6, 8.5, 9.7, 9.3, 9.1, 10.0, 21.0]
*valid_scores, _, _, _ = scores
print(valid_scores)
# 82
a, b, *valid_scores1 = scores
print(valid_scores1)
# 83
_, *valid_scores2, _ = scores
print(valid_scores2)
# 84
temp = {}
# 85
ice_cream = {"choco": 100, "red": 200, "blue": 300}
print(ice_cream)
# 86
ice_cream["green"] = 2000
ice_cream["yellow"] = 30000
print(ice_cream)
# 87
print("메로나 가격:", ice_cream["choco"])
# 88
ice_cream["blue"] = 13000
print(ice_cream["blue"])
# 89
del ice_cream["blue"]
print(ice_cream)
ice_cream["red"]
# 90

