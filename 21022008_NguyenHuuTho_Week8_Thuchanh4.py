import random
class DanhSach:
    def __init__(self, lst=None):
        if lst is None:
            self.data = []
        else:
            self.data = lst

    def nhap(self):
        n = int(input("Nhập số lượng phần tử: "))
        for i in range(n):
            self.data.append(int(input(f"Nhập phần tử thứ {i + 1}:")))

    def create_lst(self):
        # n = int(input("Nhập số lượng phần tử: "))
        n = 8
        self.data = random.sample(range(0, 1000 + 1), n)

    def xuat(self):
        print("Danh sách các số nguyên:", self.data)

    def swap(self, lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]


class SapXep_NlogN(DanhSach):
    def __init__(self, lst=None):
        super().__init__(lst)

    # Heap_sort
    def create_heap(self, lst, n):
        for t in range(n // 2, 0, -1):
            i = t
            j = 2 * i
            while j <= n:
                if j < n and lst[j - 1] < lst[j]:
                    j += 1
                if lst[i - 1] < lst[j - 1]:
                    self.swap(lst, i - 1, j - 1)
                    i = j
                    j = 2 * i
                else:
                    break

    def heap_sort(self):
        n = len(self.data)
        if n <= 1:
            return self.data

        for p in range(n, 1, -1):
            self.create_heap(self.data, p)
            self.swap(self.data, 0, p - 1)
        return self.data

    # Quick_sort
    def partition_sort(self, lst, first, last):
        if first >= last:
            return
        pivot = lst[(first + last) // 2]
        i = first
        j = last
        while i <= j:
            while lst[i] < pivot:
                i += 1
            while lst[j] > pivot:
                j -= 1
            if i <= j:
                self.swap(lst, i, j)
                i += 1
                j -= 1
        self.partition_sort(lst, first, j)
        self.partition_sort(lst, i, last)

    def quick_sort(self):
        self.partition_sort(self.data, 0, len(self.data) - 1)

    # Radix Sort
    def counting_sort(self, lst, digit):
        size = len(lst)
        output = [0] * size
        count = [0] * 10

        # Step 3: Place each number in the appropriate bucket based on the kth digit
        for i in range(size):
            index = lst[i] // digit
            count[index % 10] += 1

        # Update count array to reflect the actual position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = size - 1
        while i >= 0:
            index = lst[i] // digit
            output[count[index % 10] - 1] = lst[i]
            count[index % 10] -= 1
            i -= 1

        # Step 4: Concatenate the result of the buckets to get the sorted list
        for i in range(size):
            lst[i] = output[i]

    def radix_sort(self):
        # Step 1: Initialize k (k=0)
        digit = 1
        # Step 5: Increase k (k=k+1)
        while max(self.data) // digit > 0:
            # Step 2: Initialize 10 empty buckets
            # Step 6: Repeat Step 2 if k < number of digits in the max number
            self.counting_sort(self.data, digit)
            digit *= 10
        # Step 7: End


import os
os.system('cls' if os.name == 'nt' else 'clear')

ds1 = SapXep_NlogN()
ds1.create_lst()
print("Danh sách trước khi sắp xếp:")
ds1.xuat()

# Cau1
# ds1.heap_sort()
# print("Danh sách sau khi sắp xếp (Heap Sort):")
# ds1.xuat()

# Cau2
# ds1.quick_sort()
# print("Danh sách sau khi sắp xếp (Quick Sort):")
# ds1.xuat()

# Cau3
ds1.radix_sort()
print("Danh sách sau khi sắp xếp (Radix Sort):")
ds1.xuat()



