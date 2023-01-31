if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        coins = [int(x) for x in input().split(" ")]
        if coins[0] == 0 and coins[1] == 0:
            print("YES")
        elif (coins[0] < 1) | (coins[1] < 1):
            print("NO")
        elif (coins[0] / coins[1] > 2.0) | (coins[1] / coins[0] > 2.0):
            print("NO")
        elif (coins[0] + coins[1]) % 3 == 0:
            print("YES")
        else:
            print("NO")
