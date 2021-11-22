
def item(a, b):
    while models:
        item=a.pop()
        b.append(item)
        print(ready_models)
def item_1(b):
    for i in b:
          print(f'Уже напечатано: {i}')
          
models=['auto', 'pen', 'iphone', 'xiaome', 'huawei']
ready_models=[]
item(models, ready_models)
item_1(ready_models)

