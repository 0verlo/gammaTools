#!/usr/bin/env python
# coding=utf-8

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
