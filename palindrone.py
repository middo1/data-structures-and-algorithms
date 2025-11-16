def isPalindrome(self, x: int) -> bool:
    x_str = str(x)
    x_arr = list(x_str)
    x_arr.reverse()
    i = 0
    l = len(x_arr) 
    while i < l:
        if x_str[i] != x_arr[i]:
            return False
        i += 1
    return True