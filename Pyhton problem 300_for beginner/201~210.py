# 201
def print_coin():
    print("coin")


# 202
print_coin()
# 203
for a in range(100):
    print_coin()


# 204
# error example
# hello()
# def hello():
# print("Hello")
# 205
def print_coin_100():
    for i in range(100):
        print("coin")


# 206
def message():
    print("A")
    print("B")


message()
print("c")
message()
# 207
print("A")


def message():
    print("B")


print("C")
message()
# 208
print("A")


def message1():
    print("B")


print("C")


def message2():
    print("C")


message1()
print("E")
message2()
# 209


def message1():
    print("A")


def message2():
    print("B")
    message1()


message2()
# 210


def message1():
    print("A")


def message2():
    print("B")


def message3():
    for i in range(3):
        message2()
        print("C")
    message()
message1()


message3()
