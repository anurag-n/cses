def gray_code(n):
    if n == 0:
        return [0]
    t = gray_code(n-1)
    return t + [i + (1 << n-1) for i in t][::-1]


if __name__ == "__main__":
    num = int(input())
    # for i in range(0, pow(2, n)):
    #     bit_string = [str(1-(((i-(1 << j)) % (1 << j+2)) // (1 << j+1))) for j in range(n)]
    #     print("".join(bit_string))
    print("\n".join([format(x, 'b').zfill(num) for x in gray_code(num)]))
