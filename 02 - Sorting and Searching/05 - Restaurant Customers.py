if __name__ == "__main__":
    n = int(input())
    times = [input().split(" ") for _ in range(n)]
    times = [(int(x[0]), int(x[1])) for x in times]
    times.sort(key=lambda x: x[0])
    i = 1
    j = 0
    s = 1
    res = 1

    print(res)
