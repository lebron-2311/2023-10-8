# writer：LeBron James
# My email 1269497440@qq.com
import sys
import csv

'''
NOTE: DELETE ALL pass when you implement the program
'''

Name = []  # 定义一个空列表


def add_name(name):
    Name.append(name)  # 将新的姓名添加到列表中
    print("Successfully! You have added a name.")


def remove_name(name):
    if name in Name:
        Name.remove(name)
        print("Successfully remove name")
    else:
        print("Error: The name does not exist.")
    return Name


# remove code from the list


def print_name():
    for i in Name:
        print(i)
    print("Successfully print name")

    # print the list of names


def save_to_file(filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name'])
        writer.writerows([[name] for name in Name])
    print("Successfully save to file")


# 写入名称列表的所有行
# save the current data in the list to a text file


# main ----------------------------------

while (True):
    cmd = input('command? [add|remove|print|save|exit]').lower()
    if cmd == 'add':
        name = input('please input name ')
        add_name(name)
        print(name)
    elif cmd == 'remove':
        name = input('please remove name: ')
        remove_name(name)
        print(Name)

    # input name
    # call the remove method
    elif cmd == 'print':
        print_name()
    elif cmd == 'save':
        # call the save method
        save_to_file(filename='name.csv')
        print("Names saved to file.")
    elif cmd == 'exit':
        break
    else:
        print("Sorry, i can't understand your command")

print('System terminate, Bye!')
