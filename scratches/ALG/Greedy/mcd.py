
def mcd(a, b):
    if a % b == 0:
        return b
    else:
        mcd(b, a % b)


num1 = 2
num2 = 9
print(mcd(num1, num2))


# def euclide_ricorsivo(a: int, b: int) -> int:
#     if b == 0:
#         return a
#     return euclide_ricorsivo(b, a % b)
#
# print(euclide_ricorsivo(48, 18))  # Output: 6
