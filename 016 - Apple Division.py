if __name__ == "__main__":
    n = int(input())
    wts = [int(x) for x in input().split(" ")]
    total = sum(wts)
    res = total
    for i in range(0, (1 << n)):
        s = 0
        for j in range(0, n):
            if i & 1 << j:
                s += wts[j]
        curr = abs(total-2*s)
        res = min(res, curr)
    print(res)
