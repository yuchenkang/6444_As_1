# -*- coding: utf-8 -*-
"""
Spyder Editor
Getting bug ID from CVS files.
"""

import os
import re

count=0
c=0
root= ".\\eclipse_jdt"
wn = ".\\xxx.txt"
w=open(wn,'w')

print("read every file")
for root, dirs, files in os.walk(root):
    for filename in files:
        c=c+1
        f = open(os.path.join(root, filename), "r")
        #print(os.path.join(root, filename))
        count=count+1
        if count%20000==0:
            print(count)
        content = f.read().lower()
        match = re.search("(bug|bugs|fix|fixed)[# \t]*([0-9]+)", content)
        if match:
            w.write(match.group(2))
            print(os.path.join(root, filename))
            w.write(root)
            w.write("\n")
        f.close
print(str(c)+"\n")        
print(str(count)+"\n")        
w.seek(0)
w.close