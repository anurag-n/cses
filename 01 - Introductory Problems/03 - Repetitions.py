if __name__ == "__main__":
    dna = input()
    prev = None
    ctr = 0
    max_ctr = 1
    for p in dna:
        if p == prev:
            ctr = ctr + 1
        else:
            if ctr > max_ctr:
                max_ctr = ctr
            ctr = 1
            prev = p
    print(max(max_ctr, ctr))
