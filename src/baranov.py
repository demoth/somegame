import random
import matplotlib.pyplot

def getProbabilities(list):
    n11=0
    n10=0
    n1=0.0
    n00=0
    n01=0
    n0=0.0
    for i in xrange(len(list)-1):
        if list[i] == 1:
            n1 += 1
            if list[i+1] == 0:
                n10 += 1
            else:
                n11 += 1
        else:
            n0 += 1
            if list[i+1] == 0:
                n00 += 1
            else:
                n01 += 1
    if not n1:
        p10 = p11 = 0.0
    else: 
        p10 = n10/n1
        p11 = n11/n1
    if not n0:
        p00=p01=0.0
    else:
        p00 = n00/n0
        p01 = n01/n0
#    print 'p00=',p00
#    print 'p01=',p01
#    print 'p10=',p10
#    print 'p11=',p11
    
    return p00,p01,p10,p11
        

def roll(p,t,f):
    if p > random.uniform(0,1):
        return t
    else:
        return f

def generate(n,p01,p10):
    result = []
    zeros = 0
    ones = 0
    start = roll(0.5,1,0)
    prev = start;
    for i in xrange(n): 
        if prev == 0:
            next = roll(p01,1,0)
            zeros += 1
        else:
            next = roll(p10,0,1)
            ones += 1
        result.append(next)
        prev = next
    return result
        
data = open('131.txt')
data = list(''.join(data.read().split()))
data = [int(i) for i in data]
p00,p01,p10,p11=getProbabilities(data)
test = generate(6500,p01,p10)
print getProbabilities(test)
print getProbabilities(data)

