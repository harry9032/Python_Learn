# 31
a = "3"
b = "4"
print(a + b)
# 32
print("Hi" * 3)
# 33
print("-"*80)
# 34
t1 = 'python'
t2 = 'java'
print((t1+' '+t2+' ')*3)
# 35 : %formatting
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 =13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
# 36 : use .formate
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
# 37 : use f-string
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
# 38
amount = "5,432,345"
remove = amount.replace(',','')
change_type_remove = int(remove)
print(change_type_remove)
# 39
date = '2020/03(E) (IFRS 연결)'
print(date[:7])
# 40 - strip()
data1 = "    abcde    "
data1_change = data1.replace(' ','')
print(data1_change)