# writer：LeBron James
# My email 1269497440@qq.com
list = []
for i in range(0, 10):
    list.append(i)
print(list)

print("-" * 50)

print([i for i in range(0, 10)])

print("-" * 50)

list = ['apple', 'ice cream', 'watermelon', 'chips', 'hotdogs', 'hotpot']
while len(list) != 0:
    list.pop(-1)
    print(list)
print("-" * 50)
users_list = ['Niuniu', 'Niumei', 'HR', 'Niu Ke Le', 'GURR', 'LOLO']
for i in range(len(users_list)):
    if users_list[i] == 'HR':
        print('Hi, ' + users_list[i] + '!Would you like to hire someone?')
    print('Hi, ' + users_list[i] + '!Welcome to Nowcoder!')
print("-" * 50)

"""users_list = ['Niuniu', 'Niumei', 'HR', 'Niu Ke Le', 'GURR', 'LOLO']
for i in users_list:
    if i == 'HR':
        print('Hi, ' + users_list[i] + '! Would you like to hire someone?')
    else:
        print('Hi, ' + users_list[i] + '! Welcome to Nowcoder!')"""

users_list = ['Niuniu', 'Niumei', 'HR', 'Niu Ke Le', 'GURR', 'LOLO']
for user in users_list:
    if user == 'HR':
        print('Hi, ' + user + '! Would you like to hire someone?')
    else:
        print('Hi, ' + user + '! Welcome to Nowcoder!')

list = [3, 45, 9, 8, 12, 89, 103, 42, 54, 79]
"""
x = input("请输入一个数字：")
for i in range(len(list)):
    if list[i] == int(x):
        print(list[0:i],end=" ")
        break"""
x = input()

for i in list:
    if i == int(x):
        break
    print(i)

print("-" * 50)

my_list = [3, 45, 9, 8, 12, 89, 103, 42, 54, 79]
x = int(input("请输入一个数字："))
for i in range(len(my_list)):
    if my_list[i] == x:
        print(my_list[0:i])
        break