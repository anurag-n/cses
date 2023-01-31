if __name__ == "__main__":
    n = int(input())
    if (n * (n+1)) % 4 != 0:
        print("NO")
    else:
        print("YES")
        if n % 2 == 0:
            list1 = [i for i in range(1, n//4 + 1)] + [n-i for i in range(0, n//4)]
            list2 = [i for i in range(n//4 + 1, n//2 + 1)] + [n-i for i in range(n//4, n//2)]
        else:
            list1 = [i for i in range(n, n//2, -2)] + [i for i in range(n//2 - 1, 1, -2)]
            list2 = [i for i in range(n-1, n//2, -2)] + [i for i in range(n//2, 0, -2)]
        print(len(list1))
        print(*list1)
        print(len(list2))
        print(*list2)
