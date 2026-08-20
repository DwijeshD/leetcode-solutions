
        for i in range(len(nums)):
            prefix += nums[i]
            needed = prefix - k
            if needed in map:
                counter += map[needed]
            map[prefix] = map.get(prefix, 0) + 1

        return counter

        