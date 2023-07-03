# 51
movie_list = ["A", "B", "C"]
# 52
movie_rank = ["Avatar", "Avatar2", "Avatar3"]
movie_rank.append("Avatar4")
print(movie_rank)
# 53
movie_rank.insert(1, "superman")
print(movie_rank)
# 54
del movie_rank[1]
print(movie_rank)
# 55
del movie_rank[2]
print(movie_rank)
del movie_rank[2]
print(movie_rank)
# 56
lang1 = ["C", "C++", "Python"]
lang2 = ["Java", "C#", "Go"]
langs = lang1 + lang2
print(langs)
# 57
numbers = [1,2,3,4,5,6,7]
print("max:", max(numbers))
print("min:", min(numbers))
# 58
print("sum:", sum(numbers))
# 59 len : langs
print("len_langs:", len(langs))
# 60 average numbers
average_numbers = sum(numbers)/len(numbers)
print(average_numbers)
