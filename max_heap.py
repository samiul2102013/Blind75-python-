import heapq
li = [3,2,5,3,8,2,1]

neg_li = [-x for x in li]
heapq.heapify(neg_li)
print(neg_li)  # max heapified list, not necessarily sorted