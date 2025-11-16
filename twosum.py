def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            base = nums[i]
            right = nums[i + 1:]
            j = 0
            while j < len(right):
                if base + right[j] == target:
                    return [i, i + j + 1]
                j += 1
            i += 1