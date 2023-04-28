class Danhsach:
    def __init__(self, lst=None): # lst : líst
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
        for i in range(len(self.data)):
            if x == self.data[i]:
                return i

    def them(self, x):
        self.data.append(x)

    def xoa(self, x):
        if x in self.data:
            self.data.remove(x)

    def sua(self, x, y):
        for index, value in enumerate(self.data):
            if value == x:
                self.data[index] = y


# Sử dụng lớp DanhSach
ds = Danhsach()
ds.nhap()
ds.xuat()

x = int(input("Nhập số cần tìm: "))
index = ds.tim(x)
if index != -1:
    print(f"Số {x} tìm thấy ở vị trí {index+1}")
else:
    print(f"Số {x} không tìm thấy trong danh sách")

ds.them(int(input("Nhập số cần thêm: ")))
ds.xuat()

ds.xoa(int(input("Nhập số cần xóa: ")))
ds.xuat()

index = int(input("Nhập vị trí cần sửa: "))
new_value = int(input("Nhập giá trị mới: "))
ds.sua(index, new_value)
ds.xuat()