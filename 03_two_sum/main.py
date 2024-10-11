def twoSum(nums, target):
    indices = dict()

    for i, n in enumerate(nums):
        value = target - n

        if value in indices:
            return [i, indices[value]]

        indices[n] = i

    return []
        