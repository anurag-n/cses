swap_1 = {'1': '1', '2': '3', '3': '2'}
swap_2 = {'1': '2', '2': '1', '3': '3'}


def hanoi(n):
    if n == 1:
        return [['1', '3']]
    t_prev = hanoi(n-1)
    t_1 = hanoi(1)
    return [[swap_1[item[0]], swap_1[item[1]]] for item in t_prev] + t_1 + \
           [[swap_2[item[0]], swap_2[item[1]]] for item in t_prev]


if __name__ == "__main__":
    num = int(input())
    res = [" ".join(line) for line in hanoi(num)]
    print(str((1 << num) - 1))
    print("\n".join(res))
