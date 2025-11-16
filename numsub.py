def numSub(s):
        sub_strings = s.split("0")
        i = 0
        for sub_string in sub_strings:
            if len(sub_string) > 0:
                    d = len(sub_string)
                    while d > 0:
                            i += d
                            d -= 1
        return i % (10 ** 9 + 7)
        