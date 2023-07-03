# 221
def print_reverse(message):
    print(message[::-1])
# 222
def print_score(a):
    print(sum(a)/len(a))
# 223
def print_even(a):
    for b in a:
        if b%2 == 0:
            print(b)

# 224
def print_keys(A):
    for key in A.keys():
        print(key)
# 225
my_dict = {"10/16": [100, 300, 400, 500], "10/17": [20, 30 ,40, 50]}
def print_value(key):
    print(my_dict[key])

# 226
def print_5(A):
    len_A = int(len(A)/5)
    for x in range(len_A + 1):
        print(A[x*5:x*5 + 5])
# 227
def print_mxn(A, B):
    len_A = int(len(A)/B)
    for x in range(len_A + 1):
        print(A[x*B:x*B+B])
# 228
def payment(A):
    return int(A/12)

# 229
def print_LR(A, B):
    print("right:"+A)
    print("left:"+B)

# 230
print_LR(b=100, a=300)