def gen():
    for i in pr_l:
        yield i



pr_l=['Python', 'JavaScript', 'C++', 'C', 'Java']
for v in gen():
    print(v)
