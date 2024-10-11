def isAnagram(s, t):

    if len(s) != len(t):
        return False
    
    counter = dict()

    for c in s:
        counter[c] = counter.get(c, 0) + 1

    for c in t:
        if c not in counter or counter[c] == 0:
            return False
        counter[c] -= 1

    return True