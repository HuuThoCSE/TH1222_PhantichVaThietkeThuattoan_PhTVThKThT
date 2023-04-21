# Khởi tạo số gà và số chó
ga = 0
cho = 0

# Vòng lặp để tìm số gà và số chó
for i in range(37):
    j = 36 - i
    if 2 * i + 4 * j == 100:
        ga = i
        cho = j
        break

# In kết quả
print(f"Số gà là: {ga}")
print(f"Số chó là: {cho}")