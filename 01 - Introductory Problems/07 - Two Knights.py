if __name__ == "__main__":
    n = int(input())
    for i in range(1, n+1):
        if i == 1:
            print(0)
        elif i == 2:
            print(6)
        else:
            c = i * i * (i * i - 1) // 2
            d = 8 + (4 * (i-3) * (i))
            print(c - d)
