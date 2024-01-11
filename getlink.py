def generate_strings(a: str, b: str, n: int) -> None:
    n = int(input("Lütfen bir sayı girin: "))
    if n == 0:
        print(a,b)
        return 
    for i in range(n):
        for j in range(2 ** i):
            print(a * (2 ** (n - i - 1)) + b * (2 ** i) + a * (2 ** i) + b * (2 ** (n - i - 1)), end=' ')          
        print()
generate_strings('a', 'b', 3)
