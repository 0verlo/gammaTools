#!/usr/bin/env python
# coding=utf-8
import re

class gammaReader(object):
    def __init__(self,file_name):
        self.fileExist = False
        self.gammaDone = False
        self.contentType = 0
        self.elementCounter = 0
        self.gammaList = []
        
        if((None == file_name)|('' == file_name)):
            return
            
        self.fileReader = open(file_name,'r')
        for line in self.fileReader: 
                if("" != line.strip()):
                    self.gammaList.append(line.strip())
                    self.elementCounter = 0
        self.fileReader.close()
        self.fileExist = 1

        print(self.gammaList)
    
    def contentCheck(self):
        for element in self.gammaList:
            if((None != re.match(r'\d+$',element))&
                ((0 == self.contentType)|
                (1 == self.contentType))):
                self.contentType = 1
            elif((None != re.match(r'0x[a-fA-F0-9]+$',element))&
                ((0 == self.contentType)|
                (2 == self.contentType))):
                self.contentType = 2
            else:
                self.contentType = 0
                break
                
        if(1 == self.contentType):
            self.gammaList = list(map(int,self.gammaList))
            self.gammaDone = True
        elif(2 == self.contentType):
            self.gammaList = list(map(lambda x: int(x[2:], 16),self.gammaList))
            self.gammaDone = True
            
    def refrom(list):
        refromTest = ''
        counter = 0
        for content in list:
            counter = counter + 1
            refromTest = refromTest + str(content) + ','
            if(((counter-1)//16) != (counter//16)):
                refromTest = refromTest + '\n'                
        return refromTest
