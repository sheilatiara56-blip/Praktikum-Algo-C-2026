def tambah(a, b):
    return a + b
print(tambah(5,3))

def kurang(a, b):
    return a - b
print (kurang(10,4))

def kali(a, b):
    return a * b
print (kali(6,7))

def bagi(a, b):
    return a/b
print (bagi(20,4))

def modulus(a, b):
    return a % b
print (modulus(15,4))

def fibonacci(n):
    if n == 0:
        return 0
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))
#ga kepikran caranya bang :(