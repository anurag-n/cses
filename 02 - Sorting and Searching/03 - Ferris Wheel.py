if __name__ == "__main__":
    n, x = [int(x) for x in input().split(" ")]
    weights = [int(x) for x in input().split(" ")]
    weights.sort()
    i = 0
    j = n-1
    g = 0
    if n == 1:
        print(1)
    else:
        while i <= j:
            if i == j:
                g += 1
                j -= 1
            elif weights[i] + weights[j] <= x:
                g += 1
                i += 1
                j -= 1
            else:
                g += 1
                j -= 1
        print(g)
