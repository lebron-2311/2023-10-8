# writer：LeBron James
# My email 1269497440@qq.com
# 11517840 Bowen Zheng
import time


# Transposition sorting
def bubblesort():
    list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    for i in range(len(list)):  # 比较i 和 i+1 所以从0到len(list)-1
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]  # 交换两个数的位置
    print(list)


bubblesort()
print(bubblesort())
print("*" * 90)
"""代码打印None是因为你在print(bubblesort())中调用了bubblesort()函数，而该函数没有返回任何值。
   在Python中，如果函数没有显式使用return语句返回一个值，那么默认情况下它会返回None。
   为了解决这个问题，你可以直接调用bubblesort()函数而不需要将其作为参数传递给print()函数"""


def bubblesort():
    list = [21, 357, 763, 960, 292, 125, 198, 813, 591, 935, 940, 145, 118, 540, 988, 980, 656, 939, 208, 820, 687, 271,
            690, 763, 668, 370, 786, 939, 752, 139, 740, 30, 56, 513, 350, 223, 94, 167, 652, 216, 535, 130, 864, 838,
            108, 538, 180, 323, 729, 673, 562, 410, 454, 303, 297, 61, 810, 723, 213, 982, 198, 474, 520, 640, 383, 912,
            405, 511, 423, 387, 267, 36, 945, 293, 428, 626, 740, 935, 723, 639, 448, 112, 629, 40, 285, 414, 252, 136,
            971, 553, 866, 147, 173, 664, 520, 368, 914, 504, 695, 212]
    for i in range(len(list)):  # 比较i 和 i+1 所以从0到len(list)-1
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]  # 交换两个数的位置
    return list


print(bubblesort())  # 这样就不会打印None了因为函数有返回值


# 时间复杂度
def evaluate_time():
    start_time = time.time()
    bubblesort()
    end_time = time.time()
    print("Execution time:", end_time - start_time)


evaluate_time()

print("*" * 90)
import random


def generate_random_list(length):
    random_list = [random.randint(1, 1000) for _ in range(length)]
    return random_list


# Example usage
random_list = generate_random_list(100)
print(random_list)
