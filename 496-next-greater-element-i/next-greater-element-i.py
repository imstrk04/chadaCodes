class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m_stack = [] # monotonic stack
        hashmap = {}
        for i in range(len(nums2)-1, -1, -1):
            cur_num = nums2[i]
            while m_stack and m_stack[-1] < cur_num:
                m_stack.pop()
            hashmap[cur_num] = -1 if not m_stack else m_stack[-1]
            m_stack.append(cur_num)
        
        #hashmap = {4:-1, 3:4, 2: 3, 1: 2}
        #m_stack = [4, 3, 2, 1]

        res = []
        for num in nums1:
            if num in hashmap:
                res.append(hashmap[num])

        # res = [3, -1]
        return res