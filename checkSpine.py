#!/usr/bin/env python
#coding=utf-8

import sys
import os
path = sys.argv[1]
inputSuffix = sys.argv[2]
print('\nThe search path is: ' + path)
print('Check spine for a ' + inputSuffix + ' file\n')
def getListFiles(suffix):
   ret = []
   for root, dirs, files in os.walk(path):
      for filespath in files:
         ret.append(os.path.join(root,filespath))
   listSpicalPath = []
   for i in ret:
      realName = os.path.splitext(i)
      if realName[1] == suffix:
         listSpicalPath.append(realName[0])
   return listSpicalPath

ret1 = getListFiles(".atlas")
print('The Spine animation has been found,Check spine for a corresponding ' + inputSuffix + ' file\n')
ret2 = getListFiles("." + inputSuffix)
noSuffixRet = []
for value in ret1:
   if value not in ret2:
      noSuffixRet.append(value)

if len(noSuffixRet) > 0:
   print('There is no corresponding ' + inputSuffix + ' file as follows:')
   for value in noSuffixRet:
      print(value)
else:
   print('All spine animations have corresponding '+ inputSuffix + ' files')

