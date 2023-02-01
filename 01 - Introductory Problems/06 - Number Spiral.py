if __name__ == "__main__":
    n = int(input())
    coords = [input() for x in range(n)]
    for coord in coords:
        r, c = tuple([int(x) for x in coord.split(" ")])
        diag = max(r, c)
        if diag % 2 == 0:
            res = diag * diag - (diag - 1) + (diag - c) + (r - diag)
        else:
            res = diag * diag - (diag - 1) + (c - diag) + (diag - r)
        print(res)
