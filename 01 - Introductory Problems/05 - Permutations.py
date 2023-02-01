if __name__ == "__main__":
    n = int(input())
    if n in [2,3]:
        print("NO SOLUTION")
    else:
        print(*(list(range(n-1, 0, -2)) + list(range(n, 0, -2))))
