from collections import Counter
import collections
import heapq
nums = [1,2,1,2,4,1,1,2,4,3,1,3,4,2]
k = 3

counter = Counter(nums)
print(counter)
cntToVals = collections.defaultdict(list)

for key, value in counter.items():
    cntToVals[value].append(key)
    
print(cntToVals)

""" cnts = [-cnt for cnt in cntToVals.keys()]

heapq.heapify(cnts)

print(cnts)

res = []

for i in range(len(cnts)):
    next_cnt = -heapq.heappop(cnts)
    print(next_cnt)
    for num in cntToVals[next_cnt]:
        if len(res) == k: return res
        res.append(num)

return res


 """