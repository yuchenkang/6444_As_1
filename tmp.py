# -*- coding: utf-8 -*-
"""
Spyder Editor
Getting bug ID from CVS files.
"""

import os
import re

count=0

r= "./Workable"
wn = "./zzz.txt"
w=open(wn,'w')

print("read every file")
for root, dirs, files in os.walk(r):
    s=set()
    for filename in files:
        
        f = open(os.path.join(root, filename), "r")
        #print(os.path.join(root, filename))
        count=count+1
        if count%3000==0:
            print(count)
        content = f.read().lower()
        match = re.search("(bug|bugs|fix|fixed)[# \t]*([0-9]+)", content)
        if match:
            s.add(match.group(2))
        f.close
    for bug in s:
        w.write(bug)
        w.write("\t")
        w.write(str(root)[len(r)+1:])
        w.write("\n")
      
print(str(count)+"\n")        
w.seek(0)
w.close