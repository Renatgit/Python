dic = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
    }
print(dic)
for k, v in dic.items():
    if v%2==0:
        print(f'{k} --> even') 
    else:
        print(f'{k} --> odd')
