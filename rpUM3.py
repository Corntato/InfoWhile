nr=0
suma=0
while not((nr%2==1) and (nr%3==0)):
    nr=eval(input('nr='))
    if nr%2==0:
        suma+=nr

print('suma nr pare=',suma)