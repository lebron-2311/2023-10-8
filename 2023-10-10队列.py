# writer：LeBron James
# My email 1269497440@qq.com
class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.empty():
            raise IndexError("pop from empty stack")
        self.queue.pop(0)

    def empty(self):
        self.queue == []

    def size(self):
        return len(self.queue)

if __name__ == '__main__':
    Queue = queue()
    Queue.enqueue(1)
    Queue.enqueue(2)
    Queue.enqueue(3)
    print(Queue.queue)
    Queue.dequeue()
    Queue.dequeue()
    print(Queue.queue)

