import random
class Danhsach:
    def __init__(self, lst=None):
        if lst is None:
            self.data = []
        else:
            self.data = lst

    def nhap(self):
        n = int(input("Nhập số lượng phần tử: "))
        for i in range(n):
            self.data.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

    def create_lst(self):
        # n = int(input("Nhập số lượng phần tử: "))
        n = 8
        self.data = random.sample(range(0, 1000 + 1), n)

    def xuat(self):
        print("Danh sách các số nguyên: ", self.data)

    def tim(self, x):
        return x in self.data

    def them(self, x):
        self.data.append(x)

    def xoa(self, x):
        if x in self.data:
            self.data.remove(x)

    def sua(self, x, y):
        for index, value in enumerate(self.data):
            if value == x:
                self.data[index] = y

    def Swap(self, lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]


class Sapxep_NMu2(Danhsach):
    # Selection Sort
    def selection_sort(self, lst=None):
        if lst is None:
            lst = self.data
        N = len(lst)
        if N == 0:
            N = len(lst)
        if len(lst) <= 1:
            return lst
        K = 0
        while K < N-1:
            Min = lst[K]
            PosMin = K
            for Pos in range(K+1, N):
                if Min > lst[Pos]:
                    Min = lst[Pos]
                    PosMin = Pos
            lst[K], lst[PosMin] = lst[PosMin], lst[K]
            K += 1
        return lst

    # Đúng vậy, đoạn mã bạn đưa ra là một phiên bản của thuật toán sắp xếp chọn trực tiếp
    # (Selection Sort) trong Python. Thuật toán này hoạt động bằng cách duyệt qua danh sách
    # và tìm phần tử nhỏ nhất (hoặc lớn nhất) để đưa về vị trí đầu tiên, sau đó lặp lại quá
    # trình này với phần còn lại của danh sách. Quá trình này được lặp lại cho đến khi danh
    # sách được sắp xếp hoàn toàn.

    #Insertion Sort
    def insertion_sort(self, lst=None):
        if lst is None:
            lst = self.data
        N = len(lst)
        if N == 0:
            N = len(lst)
        K = 1
        while K < N:
            X = lst[K]
            Pos = 0
            while X > lst[Pos]:
                Pos = Pos + 1
            for i in range(K, Pos, -1):
                lst[i] = lst[i - 1]
            lst[Pos] = X
            K += 1
        return lst

    # Bubble Sort
    def bubble_sort(self, lst=None):
        if lst is None:
            lst = self.data
        N = len(lst)
        if N == 0:
            N = len(lst)
        for i in range(N-1):
            for j in range(N-1, i, -1):
                if (lst[j] < lst[j - 1]):
                    self.Swap(lst, j, j - 1)
        return lst

    def optimized_bubble_sort(self, lst=None):
        if lst is None:
            lst = self.data
        N = len(lst)
        if N == 0:
            N = len(lst)

        left = 0
        right = N - 1

        while left < right:
            # Sắp xếp từ trái sang phải
            new_right = left
            for i in range(left, right):
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    new_right = i
            right = new_right

            # Sắp xếp từ phải sang trái
            new_left = right
            for i in range(right, left, -1):
                if lst[i] < lst[i - 1]:
                    lst[i], lst[i - 1] = lst[i - 1], lst[i]
                    new_left = i
            left = new_left

        return lst


class HeapSort:
    def __init__(self, lst=None):
        if lst is None:
            self.data = []
        else:
            self.data = lst

    def heapify(self, lst, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and lst[largest] < lst[left]:
            largest = left

        if right < n and lst[largest] < lst[right]:
            largest = right

        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            self.heapify(lst, n, largest)

    def heap_sort(self, lst=None):
        if lst is None:
            lst = self.data
        n = len(lst)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(lst, n, i)

        for i in range(n - 1, 0, -1):
            lst[i], lst[0] = lst[0], lst[i]
            self.heapify(lst, i, 0)

        return lst

def binary_search(lst, x, left, right):
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def binary_insertion_sort(lst):
    n = len(lst)

    for i in range(1, n):
        x = lst[i]
        pos = binary_search(lst, x, 0, i)

        for j in range(i, pos, -1):
            lst[j] = lst[j - 1]

        lst[pos] = x

    return lst

import os
os.system('cls' if os.name == 'nt' else 'clear')

ds_sapxep = Sapxep_NMu2()
# ds_sapxep.nhap()
ds_sapxep.create_lst()
print("Danh sách trước khi sắp xếp:")
ds_sapxep.xuat()

# Cau 1
#ds_sapxep.selection_sort()
#print("Danh sách sau khi sắp xếp (selection_sort):")
#ds_sapxep.xuat()

# Cau 2
# ds_sapxep.insertion_sort()
# print("Danh sách sau khi sắp xếp (insertion_sort):")
#ds_sapxep.xuat()

# Cau 3
ds_sapxep.bubble_sort()
print("Danh sách sau khi sắp xếp (bubble_sort):")
ds_sapxep.xuat()
print()

# Cau 1_Nangcao
hs = HeapSort([9, 3, 5, 1, 7, 4, 8, 6])
print("Danh sách trước khi sắp xếp (heapsort):")
print(hs.data)
hs.heap_sort()
print("Danh sách sau khi sắp xếp (heapsort):")
print(hs.data)
print()

# Cau 2_Nangcao
unsorted_list = [9, 3, 5, 1, 7, 4, 8, 6]
print("Danh sách trước khi sắp xếp (binary_search):")
print(unsorted_list)
sorted_list = binary_insertion_sort(unsorted_list)
print("Danh sách sau khi sắp xếp (binary_search):")
print(sorted_list)

# Cau 3_Nangcao
ds_sapxep1 = Sapxep_NMu2()
ds_sapxep1.create_lst()
print("Danh sách trước khi sắp xếp:")
ds_sapxep1.xuat()
ds_sapxep1.optimized_bubble_sort()
print("Danh sách sau khi sắp xếp (bubble_sort_caitien):")
ds_sapxep1.xuat()
print()
