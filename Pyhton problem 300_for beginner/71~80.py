#71
my_variable = ()
print(type(my_variable))
# 72
movie = ("Avatar", "Avatar2", "Avatar3")
# 73
numbers = (1, )
# 74
t = (1, 2, 3, 4)
#t[0] = 'a' - It can't be
# 75
t = 1, 2, 3, 5
print(t)
# 76 - change tuple
t = ('a', 'b', 'c', 'd')
t = ('A', 'B', 'C', 'D')
# 77 tuple -> list
list_t = list(t)
print(list_t)
# 78 list -> tuple
tuple_t = tuple(list_t)
print(tuple_t)
# 79
list_fruit = ['apple', 'banana', 'mango']
a, b, c = list_fruit
print(a, c)
# 80
data = tuple(range(2, 100, 2))
print(data)
