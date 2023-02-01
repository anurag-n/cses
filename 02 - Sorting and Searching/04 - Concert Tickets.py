if __name__ == "__main__":
    n, m = [int(x) for x in input().split(" ")]
    h = [int(x) for x in input().split(" ")]
    t = [int(x) for x in input().split(" ")]
    h.sort()
    for price in t:
        r = -1
        for i in range(m-1, -1, -1):
            if price <= h[i]:
                r = h.pop(i)
                m = len(h)
                break
        print(r)
