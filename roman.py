def romanToInt(s):
    roman = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    res = 0
    for i, j in enumerate(s):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[j]
        else:
            res += roman[j]
    return res