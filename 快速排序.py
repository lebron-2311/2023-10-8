# writer：LeBron James
# My email 1269497440@qq.com
"""def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]  # 基准元素

    for j in range(low, high):
        # 当前元素小于或等于基准元素
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # 交换

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1"""


class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def partition(self, left, right):
        arr = self.arr
        k = left
        for i in range(left, right):
            if arr[i] <= arr[right]:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quicksort(self, left, right):
        if left < right:
            q = self.partition(left, right)
            self.quicksort(left, q - 1)
            self.quicksort(q + 1, right)


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    qs = QuickSort(lst)
    qs.quicksort(0, len(lst) - 1)
    print(lst)
