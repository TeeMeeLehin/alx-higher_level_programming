#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) != str or roman_string is None):
        return 0
    int_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    rs = list(roman_string)
    i = 0

    while (i < len(rs)):
        next_num = int_dic[rs[i + 1]] if i + 1 < len(rs) else 0
        if int_dic[rs[i]] >= next_num:
            result += int_dic[rs[i]]
            i += 1
        else:
            result += (int_dic[rs[i + 1]] - int_dic[rs[i]])
            i += 2
    return result
