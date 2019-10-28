#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

print("hello")
def extend(list,number):
    originLen = len(list)
    print(originLen)
    extendNumb = number*1.0/(originLen)
    mark = 0
    mark2 = 0
    outlist = []
    while (mark < (originLen-1)):
        while (mark2 < extendNumb):
            outlist.append(list[mark]+int(((list[mark+1]-list[mark])/extendNumb*mark2)+0.5))
            mark2=mark2+1
        mark2=0        
        mark=mark+1
    outlist.append(list[mark])
    outLen = len(outlist)
    print(outLen)
    return outlist
    
def reform(list):
    refromTest = ''
    counter = 0
    for content in list:
        counter = counter + 1
        refromTest = refromTest + str(content) + ','
        if(((counter-1)//16) != (counter//16)):
            refromTest = refromTest + '\n'                
    return refromTest

def balance(listMain, listSub):
    balanceList = []
    if (len(listMain) == len(listSub)):
        counter = 0
        while(counter < len(listMain)):
            balanceList.append(int((listMain[counter]+listSub[counter])/2+0.5))
            counter = counter + 1
            
    return balanceList
    
def smooth(list):
    smoothList = []
    x = np.arange(0, len(list), 1) #x轴为1,2,3...n(n=len(list))
    y = np.array(list) #y轴为list的值
    n = 2
    z1 = np.polyfit(x, y, n)#用n次多项式拟合
    p1 = np.poly1d(z1)
    smoothList=[int(p1(x)+0.5) for x in range(len(list))]

    return smoothList
    
def draw(listResult, listBeforeSmooth=[]):
    x = np.arange(0, len(listResult), 1) #x轴为1,2,3...n(n=len(list))
    y = np.array(listResult) #y轴为list的值
    plt.plot(x, y, 'r',label='result curve')
    
    if (([] != listBeforeSmooth)&
        (len(listResult) == len(listBeforeSmooth))):
        z = np.array(listBeforeSmooth)
        plt.plot(x, z, '*',label='curve before smooth')
        
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.legend(loc=4) #指定legend的位置,读者可以自己help它的用法
    plt.title('gamma')
    plt.show()
    
    return


