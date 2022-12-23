upperen = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
loweren = upperen.lower()
n = input().split()
total = []

def cikl():
    total = []
    for i in m:
        if i.isupper():
            ind = upperen.index(i)
            ind = ind + x
            if ind >= len(upperen):
                ind -= len(upperen)
            total.append(upperen[ind])
        if i.islower():
            ind = loweren.index(i)
            ind = ind + x
            if ind >= len(upperen):
                ind -= len(upperen)
            total.append(loweren[ind])
        if not i.isalpha():
                total.append(i)
    off = ''
    for i in (total):
        for j in range(len(i)):
            off += i[j]
    return off

for i in range(len(n)):
    x=0
    m = str(n[i])
    for j in m:
        if j.isalpha():
            x+=1
    total.append(cikl()+' ')

print(*total, sep='')


#Day, mice. "Year" is a mistake!