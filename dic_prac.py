from collections import Counter
import collections
nums = [1,4,6,4,5,1,6,6]
counter = Counter(nums)
print(counter)  # frequecy sorted in descending order
print(f"{counter.keys()}, {counter.values()}") 
 
cntToVals = collections.defaultdict(list)

for val, cnt in counter.items():
    cntToVals[cnt].append(val)
    print(cntToVals) 
 