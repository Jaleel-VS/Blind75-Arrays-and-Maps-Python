def groupAnagrams(strs):
    hm = dict()

    for s in strs:
        hash_key = ''.join(sorted(s))

        if hash_key not in hm:
            hm[hash_key] = []
        
        hm[hash_key].append(s)

    return list(hm.values())