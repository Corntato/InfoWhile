sp=0
sn=0
np=0
nn=0
i=1
while i<=12:
    t=eval(input('temperatura='))
    if t>=0:
        sp+=t
        np+=1
    if t<0:
        sn+=t
        nn+=1
        i+=1

print('media t pozitive=',round((sp/np),2),'C')
print('media t pozitive=',round((sn/nn),2),'C')