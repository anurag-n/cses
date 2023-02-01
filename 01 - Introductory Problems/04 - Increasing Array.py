if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split(" ")]
    moves = 0
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            moves = moves + nums[i-1] - nums[i]
            nums[i] = nums[i-1]
    print(moves)
