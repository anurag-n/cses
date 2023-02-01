if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split(" ")]
    num_map = {}
    for num in nums:
        if num not in num_map:
            num_map[num] = 1
    print(len(num_map))
