def fibo(n=10):
    i = 0
    a, b = 0, 1
    while i < 10:
        print(a, end = " ")
        a, b = b, a+b
        i += 1

if __name__ == "__main__":
    print("calling Subpkg/mod3.py...")
