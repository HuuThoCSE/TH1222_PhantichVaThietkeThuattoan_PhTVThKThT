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

ds_sapxep = Sapxep()
ds_sapxep.nhap()
print("Danh sách trước khi sắp xếp:")
ds_sapxep.xuat()
ds_sapxep.sap_xep()
print("Danh sách sau khi sắp xếp:")
ds_sapxep.xuat()
