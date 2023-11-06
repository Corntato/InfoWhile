sum=0
pr=1
n=int(input('dati nr de elemnte n='))
i=1
while n>=i:
    sum+=n
    pr*=n
    i+=1

print('suma elementelor=',sum)
print('produasul elementelor=',pr)
print('media elementelor=',sum/n)