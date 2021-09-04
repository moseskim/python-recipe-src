s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}

# s1 - s2
# s1 - s2 = s1에는 있고 s2에는 없는 요소 = A, B
s = s1.difference(s2)
print(s)

# s2 - s1
# s2 - s1 = s2에는 있고 s1에는 없는 요소 = D, E
s = s2.difference(s1)
print(s)
