n, s = [int(x) for x in input().split(" ")]
list_int = [int(x) for x in input().split(" ")]
f = False
num_map = {}
for i in range(n):
    if s-list_int[i] not in num_map:
        num_map[list_int[i]] = (s-list_int[i], i+1)
    else:
        print(i+1, num_map[s-list_int[i]][1])
        f = True
if not f:
    print("IMPOSSIBLE")
