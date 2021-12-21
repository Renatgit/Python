def gen():
    for i in kor:
        yield i
y=gen()
lst_n=[4, 16, 64, 256]
kor=[item**1/2 for item in lst_n]
g=0
while g<len(kor):
    print(next(y))
    g+=1
