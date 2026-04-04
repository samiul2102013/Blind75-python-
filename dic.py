# Values are NOT in sync with keys
data = {'c': 1, 'a': 3, 'b': 2}

sor = sorted(data.items())
print(sor)
# Sort by Value (index 1)
sorted_val = sorted(data.items(), key=lambda x: x[1])

print(sorted_val)