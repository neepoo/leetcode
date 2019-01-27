"""
Dividing a set into two equal length subsets,
 that one subset is always greater than the other.
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for num in nums2:
            nums1.append(num)
        nums1.sort()
        if len(nums1)%2:
            return nums1[len(nums1)//2]
        else:
            return (nums1[len(nums1)//2-1] + nums1[len(nums1)//2])/2

if __name__ == "__main__":
    so = Solution()
    print(so.findMedianSortedArrays([1,2], [3,4]))