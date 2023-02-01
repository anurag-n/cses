n = int(input())
nums = [int(x) for x in input().split(" ")]

p = 0
s = -1 * pow(10, 14)
for num in nums:
    p = p+num if p+num >= num else num
    s = p if p > s else s
print(s)
