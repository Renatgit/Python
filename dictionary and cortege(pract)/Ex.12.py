first=[1, 2, 3]
second=[4, 5, 6]
empty=[(i, n) for i in first for n in second]
print(empty)
for i in empty:
    print(i)
#for i in first:
#   for n in second:
#        empty.append((i, n))
#        print(empty)
#for i in empty:
#    print(i)
