class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        sorted_list = sorted(counter.items(), key = lambda item:item[1], reverse = True)
        ans_list = []
        for key, value in sorted_list[:k]:
            ans_list.append(key)
        return ans_list
        