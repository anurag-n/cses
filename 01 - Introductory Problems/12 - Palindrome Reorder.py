if __name__ == "__main__":
    orig_string = input()
    n = len(orig_string)
    string_map = {}
    for ch in orig_string:
        if ch in string_map:
            string_map[ch] += 1
        else:
            string_map[ch] = 1
    odds = [x for x in string_map if string_map[x] % 2 == 1]
    if len(odds) > 1:
        print("NO SOLUTION")
    elif n % 2 == 1 and len(odds) == 1:
        pal_string = odds[0] * string_map[odds[0]]
        for key, val in [(x, string_map[x]) for x in string_map if string_map[x] % 2 == 0]:
            pal_string = key * (val//2) + pal_string + key * (val//2)
        print(pal_string)
    else:
        pal_string = ""
        for key, val in string_map.items():
            pal_string = key * (val // 2) + pal_string + key * (val // 2)
        print(pal_string)
