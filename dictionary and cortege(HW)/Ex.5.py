rivers={
    'Egypt':'Nile',
    'Ukrain':'Dnepr',
    'Brazil':'Amazon'
    }

for k, v in rivers.items():
    print(f'\nThe {v} runs through {k}')
    print('-'*30)

print(f'\nAll countries in dictionary:')
for key in rivers.keys():
    print(f'\t{key}')
    
print(f'\nAll rivers in dictionary:')
for value in rivers.values():
    print(f'\t{value}')
