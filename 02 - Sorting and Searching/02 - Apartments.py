if __name__ == "__main__":
    n, m, k = [int(x) for x in input().split(" ")]
    pref = [int(x) for x in input().split(" ")]
    sizes = [int(x) for x in input().split(" ")]
    app_map = {}
    for i in range(n):
        app_map[i] = [j for j in range(m) if -k <= sizes[j]-pref[i] <= k]
