#class Solution:
#    def findMedianSortedArrays(self, nums1, nums2):
"""
:type nums1: List[int]
:type nums2: List[int]
:rtype: float
"""

nums1 = []
nums2 = [2,3]

m = len(nums1)
n = len(nums2)
mid = (m + n) // 2
m1 = 0
n1 = 0

temp = [0] * (mid + 1)
t1 = 0

while (t1 < mid + 1 and m1 < m and n1 < n):
    if (nums1[m1] < nums2[n1]):
        temp[t1] = nums1[m1]
        m1 += 1
    else:
        temp[t1] = nums2[n1]
        n1 += 1
    t1 += 1

while (m1 < m and t1 < mid + 1):
    temp[t1] = nums1[m1]
    t1 += 1
    m1 += 1

while (n1 < n and t1 < mid + 1):
    temp[t1] = nums2[n1]
    t1 += 1
    n1 += 1

if (m + n) % 2 == 0:
    print((temp[mid] + temp[mid - 1]) / 2.0)
    #return (temp[mid] + temp[mid - 1]) / 2.0
else:
    print(temp[mid])
    #return temp[mid]
