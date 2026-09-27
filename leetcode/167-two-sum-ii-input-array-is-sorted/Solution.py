class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        # for i in range(len(numbers)):
        #     for j in range(len(numbers)):
        #         if ((numbers[i] + numbers[j]) == target) and (i < j) and (j <= len(numbers)):
        #             return [i+1,j+1]

        # numbers = [1,2,3,4,5,6,7,8,9] target = 7

        lower = 0
        upper = len(numbers) -1

        while lower <= upper:
            print(lower, upper)
            total = numbers[lower] + numbers[upper]

            if total == target:
                return [lower + 1, upper + 1]

            if total > target:
                upper -= 1
            if total <  target:
                lower += 1
            
