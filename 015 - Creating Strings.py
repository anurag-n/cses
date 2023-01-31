def create_strings(char_map):
    list_chars = [k for k in char_map.keys() if char_map[k] > 0]
    if len(list_chars) == 1:
        return [list_chars[0] * char_map[list_chars[0]]]
    else:
        list_chars.sort()
        result = []
        for i in range(len(list_chars)):
            new_char_map = char_map.copy()
            new_char_map[list_chars[i]] = char_map[list_chars[i]] - 1
            other_list = create_strings(new_char_map)
            result += [list_chars[i] + cr for cr in other_list]
        return result


if __name__ == "__main__":
    in_str = input()
    ch_map = {}
    for char in in_str:
        if char not in ch_map:
            ch_map[char] = 1
        else:
            ch_map[char] += 1
    res = create_strings(ch_map)
    print(len(res))
    print("\n".join(res))
