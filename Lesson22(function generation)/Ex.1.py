def gen():
    for i in lst_my:
        yield i
    
lst_my=['a', 'b', 'c', 'd']
y=gen()
print(next(y))
print(next(y))
print(next(y))
print(next(y))
