class Solution:

    def sortArray(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid] #lista do inicio ate o meio
            right = nums[mid:] # lista do meio ate o fim

            self.sortArray(left)
            self.sortArray(right)

            j, j, k = 0, 0, 0
            i = 0

            #roda do inicio ate o fim
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1


            while j < len(right):
                nums[k]=right[j]
                j += 1
                k += 1

        return nums

