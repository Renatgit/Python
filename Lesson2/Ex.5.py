n=int(input('n = '))
p=0.5
S=0
for i in range(1 , n+1):
    S+=p
    p/=2
    print(S)
print(S)
