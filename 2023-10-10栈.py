# writer：LeBron James
# My email 1269497440@qq.com


# 书上的例子
def greet2(name):
    print("How are you, " + name + "?")

def bye():
    print("Ok bye!")


def greet(name):
    print("Hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()


# 先调用greet函数，然后再调用greet2函数，最后调用bye函数，最后再返回到greet函数
a = greet('lerbon')
print(a)


def fax(x):
    if x == 1:
        return 1
    else:
        return x * fax(x - 1)


a = fax(9)
print(a)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.empty():
            raise IndexError("pop from empty stack")
        self.stack.pop()

    def top(self):
        if self.empty():
            raise IndexError("pop from empty stack")
        return self.stack[-1]

    def empty(self):
        self.stack == []

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.stack)
    stack.pop()
    stack.pop()
    """stack.pop()
    stack.pop()"""
    print(stack.stack)
#shift + F6 重命名批量修改