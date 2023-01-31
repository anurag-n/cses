if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split(" ")]
    print(((n*(n+1))//2) - sum(nums))
