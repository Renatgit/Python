favorite_places={
    'park': ['Den', 'Renat', 'Kirill'],
    'pool': ['Den'],
    'shop': ['Renat','Den']
    }
den=[]
renat=[]
kirill=[]
for k, v in favorite_places.items():
    if v=='Den' in k:
        den.append(k)
print(den)
print(renat)
print(kirill)
