def get_input(text):
    while True:
        value = float(input(text))
        if 0 <= value <= 10:
            return value

qt = get_input("Nhap vao diem Qua trinh: ")
gk = get_input("Nhap vao diem Cuoi ky: ")
ck = get_input("Nhap vao diem Cuoi ky: ")

def KTraDiemHP(dhp):
    if(dhp >= 8.5):
        return "A"
    if(dhp >= 7):
        return "B"
    if(dhp >= 5.5):
        return "C"
    if(dhp >= 4):
        return "D"
    return "F"

dhp = qt * 0.1 + gk * 0.4 + ck * 0.5
print("Diem hoc phan:", dhp)
print("Diem chu:", KTraDiemHP(dhp))