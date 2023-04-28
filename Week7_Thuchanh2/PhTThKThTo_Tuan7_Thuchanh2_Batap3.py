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

class Sapxep(Danhsach):
    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(self, lst=None):
        if lst is None:
            lst = self.data
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = self.merge_sort(lst[:mid])
        right = self.merge_sort(lst[mid:])
        return self.merge(left, right)

    def sap_xep(self):
        self.data = self.merge_sort()

class Sapxep_N2(Sapxep):
    def bubble_sort(self):
        for i in range(len(self.ds) - 1):
            for j in range(len(self.ds) - 1, i, -1):
                if self.ds[j] < self.ds[j - 1]:
                    self.ds[j], self.ds[j - 1] = self.ds[j - 1], self.ds[j]

    def bubble_sort_improved(self):
        n = len(self.ds)
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, n):
                if self.ds[i - 1] > self.ds[i]:
                    self.ds[i], self.ds[i - 1] = self.ds[i - 1], self.ds[i]
                    swapped = True
            n -= 1

if __name__ == "__main__":
    ds = Danhsach()

    ds.nhap(5)
    ds.xuat()

    ds.them(10)
    ds.xuat()

    ds.xoa(10)
    ds.xuat()

    vi_tri = ds.tim(3)
    if vi_tri != -1:
        print(f"Số 3 tìm thấy tại vị trí: {vi_tri}")
    else:
        print("Số 3 không tìm thấy trong danh sách")

    ds.sua(1, 20)
    ds.xuat()
