def isPalindrome(s: str) -> bool:
    i = 0
    j = len(s)-1
    while i <= j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i] == s[j] or s[i] == s[j].upper() or s[i] == s[j].lower():
            i += 1
            j -= 1
        else:
            return False
    return True


isPalindrome("nabbbvan")
