hm = {}
words = ["hello", "world", "hello", "python"]
for  i,word in enumerate(words):
    t = tuple(word)
    hm[word]= []
    hm[word].append(i)
    hm[word].append(word)
    print(hm)
    
    
print(hm.keys())
print(hm.values())