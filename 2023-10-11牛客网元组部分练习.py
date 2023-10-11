# writer：LeBron James
# My email 1269497440@qq.com

# 1.如何把字符串转换成元组
"""a = input()
b = input()
tuple = (a, b)
print(tuple)"""

# 2. 元组是不可变的，所以不能修改元组的值而且是（）不是[]
entry_form = ("Niuniu", "Niumei")
print(entry_form)
try:
    entry_form[1] = "Niukele"  # 元组是不可变的，所以不能修改元组的值所以会报错
except:
    print('The entry form cannot be modified!')
print(entry_form)

# 3.
"""如果你想要一行输入多个字符串表示考生的名字，并以空格进行间隔，可以使用input()函数读取输入，并使用split()方法将输入的字符串分割成一个名字列表。
以下是示例代码：

names = input("请输入考生的名字（以空格间隔）：").split()
print(names)
在这段代码中，input()函数用于接收用户输入的字符串。然后，我们使用split()方法将输入的字符串按照空格进行分割，生成一个名字列表names。最后，我们将这个名字列表打印输出。
请注意，输入的名字之间需要用空格进行间隔。"""

print("*" * 90)
"""names = input("请输入考生的名字（以空格间隔）：").split()
name_tuple = tuple(names)
print(name_tuple)
print(name_tuple[0:3])"""



# 4.
"""name_list = ['Tom', 'Tony', 'Allen', 'Cydin', 'Lucy', 'Anna']
tuple1 = tuple(name_list)

name = input()

if name in name_list:
    print(tuple1)
    print('Congratulations!')
else:
    print(tuple1)
    print('What a pity!')"""



# 5.
"""tupele1 = tuple(1, 2, 3, 4, 5)
print(tupele1)
print(len(tupele1))
tupele12 = tuple(4, 5, 6, 7, 8)
tuple3 = tupele1 + tupele12
print(tuple3)
print(len(tuple3))"""





















#在创建元组时，你需要将元素作为一个整体传递给tuple()函数，而不是将每个元素作为单独的参数传递。
tuple1 = tuple([1, 2, 3, 4, 5])
print(tuple1)
print(len(tuple1))

tuple12 = tuple([4, 5, 6, 7, 8])
tuple3 = tuple1 + tuple12
print(tuple3)
print(len(tuple3))
