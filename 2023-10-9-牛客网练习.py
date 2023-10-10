# writer：LeBron James
# My email 1269497440@qq.com
import time

# continue 跳过本次循环
for i in range(1, 16):
    if i == 13:
        continue
    else:
        print(i, end=" ")
print('\n')

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = input("请输入一个数字：")

for i in range(len(list)):
    for j in range(len(list[i])):
       list[i][j] = int(list[i][j]) * int(n)
print(list)

print(len(list))
print(list[i])