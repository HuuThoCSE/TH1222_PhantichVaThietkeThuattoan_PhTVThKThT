def CheckSNT(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def SumNFistSNT(N):
    count, num, total = 0, 2, 0
    while count < N:
        if CheckSNT(num):
            total += num
            count += 1
        num += 1
    return total

def Fibonasi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonasi(n-1)+Fibonasi(n-2)

def SumTwoString(str1, str2):
    ds1 = [int(x) for x in str1.split()]
    ds2 = [int(x) for x in str2.split()]

    if len(str1) != len(str2):
        raise ValueError("Do dai 2 chuoi khong bang nhau")

    dsSum = [x + y for x, y in zip(ds1, ds2)]

    return " ".join(str(x) for x in dsSum)

# run
N = 7
if CheckSNT(N):
    print(f"{N} la so nguyen to")
else:
    print(f"{N} khong phai la so nguyen to")

tong = SumNFistSNT(N)
print(f"Tong {N} so nguyen to dau tien la: {tong}")

print("Fibonasi:", Fibonasi(N))

str1 = "1 2 3 4 5"
str2 = "6 7 8 9 8"

SumStr = SumTwoString(str1, str2)
print(f"Tong 2 chuoi so nguyen: {SumStr}")