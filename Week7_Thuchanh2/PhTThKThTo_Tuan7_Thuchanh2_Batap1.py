import math

def solve_general_recursive(a, b, d_func, n):
    def case_1():
        return n ** (math.log(a, b))

    def case_2():
        return n ** (math.log(d(b), b))

    def case_3():
        return n ** (math.log(a, b)) * math.log(n, b)

    d_b = d_func(b)

    if a > d_b:
        return case_1()
    elif a < d_b:
        return case_2()
    else:
        return case_3()


# Ví dụ sử dụng
def d_func(n):
    return n ** 2  # Hàm tiến triển d(n) = n^2

a = 4
b = 2
n = 16

result = solve_general_recursive(a, b, d_func, n)
print(f"T({n}) = {result}")