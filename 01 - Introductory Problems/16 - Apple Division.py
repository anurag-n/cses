if __name__ == "__main__":
    n = int(input())
    wts = [int(x) for x in input().split(" ")]
    total = sum(wts)
    res = total
    for i in range(0, (1 << n)):
        bin_i = (bin(i)[2:]).zfill(n)
        s = sum([wts[j] for j in range(0, n) if bin_i[j] == "1"])
        curr = abs(total-2*s)
        res = min(res, curr)
    print(res)
