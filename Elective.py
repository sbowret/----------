x = int(input("Ввод"))
a = 0
b = 0
while x > 0:
    a += 1
   
    b =x % 8
    x //= 8
print(a)
print(b)    