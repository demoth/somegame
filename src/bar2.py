'''
Created on 21.04.2011

@author: sorseg
'''
import matplotlib.pyplot as plt
data = open('9.2.txt')
list=[]

for line in data:
    list +=[line.split()]

list = list[1:]
list1,list2,list3,list4 = zip(*list)

list1 = [ float(i) for i in list1]
list2 = [ float(i) for i in list2]
list3 = [ float(i) for i in list3]
list4 = [ float(i) for i in list4]
plt.hist(list1,bins=15)
plt.hold(True)
plt.hist(list2)
#plt.hist(list3)
#plt.hist(list4)
plt.show()