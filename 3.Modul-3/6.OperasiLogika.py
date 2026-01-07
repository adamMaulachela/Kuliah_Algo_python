# operasi logika atau boolean

# not, or, and, xor

# NOT
print("====NOT====")
a = False # tipe data : boolean
c = not a # True
print("data a =", a)
print("-------------- NOT")
print("data c =", c) # TRUE

# OR (jika salah satu true, maka hasilnya adalah true)
print("====OR====")
a = False
b = False
c = a or b # false
print(a, "OR", b, "=", c) # False
a = False
b = True
c = a or b # True
print(a, "OR", b, " =", c)  # Tr
a = True
b = False
c = a or b # true
print(a, " OR", b, "=", c) # true
a = True
b = True
c = a or b # True
print(a, " OR", b, " =", c) # True

# AND (jika dua buah nilai true, maka hasil true)
print("====AND====")
a = False
b = False
c = a and b # False
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b # false
print(a, "AND", b, " =", c)
a = True
b = False
c = a and b # false
print(a, " AND", b, "=", c)
a = True
b = True
c = a and b # true
print(a, " AND", b, " =", c)

# XOR (akan true jika salah satu true, sisanya false)
print("====XOR====")
a = False
b = False
c = a ^ b # false
print(a, "XOR", b, "=", c)
a = False
b = True 
c = a ^ b # true
print(a, "XOR", b, " =", c)
a = True
b = False
c = a ^ b # true
print(a, " XOR", b, "=", c)
a = True
b = True
c = a ^ b # false
print(a, " XOR", b, " =", c)
