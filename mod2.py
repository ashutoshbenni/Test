def fact(n=5):
    return n if n < 2 else n * fact(n - 1)

print("calling mod2.py...")