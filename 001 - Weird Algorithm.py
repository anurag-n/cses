def simulate_execution(n, l):
    l.append(n)
    if n == 1:
        return l
    elif n % 2 == 0:
        n = n//2
        return simulate_execution(n, l)
    elif n % 2 == 1:
        n = n * 3 + 1
        return simulate_execution(n, l)
    else:
        return None


if __name__ == "__main__":
    num = int(input())
    result = simulate_execution(num, [])
    print(*result)
