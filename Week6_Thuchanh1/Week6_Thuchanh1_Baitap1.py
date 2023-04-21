while True:
    qt = float(input("Nhap vao diem Qua trinh: "))
    if 0 <= qt <= 10:
        break
while True:
    gk = float(input("Nhap vao diem Giua ky: "))
    if 0 <= gk <= 10:
        break
while True:
    ck = float(input("Nhap vao diem Cuoi ky: "))
    if 0 <= ck <= 10:
        break

dhp = qt*0.1+gk*0.4 + ck*0.5
print("Diem hoc phan:", dhp)
print("Diem chu: ", end="")
if(dhp >= 8.5):
    print("A")
elif(dhp >= 7):
    print("B")
elif(dhp >= 5.5):
    print("C")
elif(dhp >= 4):
    print("D")
else:
    print("F")