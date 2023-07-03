# 21 - indexing(1)
letters = 'python'
print(letters[0], letters[2])
# 22 - indexing(2)
license_plate = '24가 2210'
print(license_plate[-4:])
# 23 - indexing(3)
string_1 = "121212"
print(string_1[::2])
# 24 - indexing(4)
string_2 = "123456789"
print(string_2[::-1])
# 25
phone_number = "010-1234-1234"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)
# 26
phone_number2 = phone_number1.replace(" ", "")
print(phone_number2)
# 27
url = "http://google.co.kr"
url_split = url.split('.')
print(url_split[-1])
# 28
lang = 'python'
lang_change = "P" + lang[1:]
print(lang_change)
# 29
string = "aBCDEFG"
string_change = string.replace('a', 'A')
print(string_change)
# 30
string = 'abcd'
string.replace('b', 'B')
print(string)
