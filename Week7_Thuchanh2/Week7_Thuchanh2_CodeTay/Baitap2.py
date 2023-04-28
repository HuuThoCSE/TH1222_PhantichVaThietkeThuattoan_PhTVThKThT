class Danhsach():
    def __init__(self, lst=None):
        if lst is None:
            self.data = []
        else:
            self.data = lst

    def Nhap(self):
        n = int(input("Nhập số lượng phần từ: "))
        for i in range(n):
            self.data.append(int(f"Nhập phần tử thứ {i+1} ="))

    def Xuat(self):
        print("Danh sách số nguyên", self.data)

ds = Danhsach()
ds.Nhap()
ds.Xuat()