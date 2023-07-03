# 211
def message(a):
    print(a)


message("hi")
message("hello")
# 212


def message(a, b):
    print(a + b)


message(1, 3)
message(3, 6)
# 213


def a(A):
    print(A)


# print() - wrong
# 214
def plus(a, b):
    print(a+b)

# plus("A", 3) - wrong : not same type
# 215
def print_with_smile(message):
    print(message+":D")

# 216
print_with_smile("Hi")

# 217
def print_upper_price(price):
    print(price * 1.3)
# 218
def print_sum(a, b):
    print(a+b)

# 219
def print_aritemtic_operation(a, b):
    print(a+b, a*b, a-b, a%b)

# 220
def print_max(a, b, c):
    if (a>=b) and (a>=c):
        print(a)
    elif (b>=a) and (b>=c):
        print(b)
    else:
        print(c)

# or!
def print_max1(a, b, c):
    MAX = float('-inf')
    if a > MAX:
        MAX = a
    if b > MAX:
        MAX = b
    if c > MAX:
        MAX = c
    print(MAX)