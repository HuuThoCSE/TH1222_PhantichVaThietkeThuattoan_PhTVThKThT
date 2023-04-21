while True:
    M = int(input("Nhap M: "))
    if 1000 <= M <= 9999:
        break

i = 0
tong = 0
while tong < M:
    i += 1
    if i%2 == 0:
        tong += i
        print("S=", tong)