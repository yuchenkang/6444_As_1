# -*- coding: utf-8 -*-
"""
Spyder Editor

Getting bug ID from CVS files.
"""

import os
import re

count=0
wn= "/media/yuchen/My Passport/6444/cvs/bug_ID.txt"
s=set()
print("read every file")
for root, dirs, files in os.walk("/media/yuchen/My Passport/6444/cvs/eclipse"):
    for filename in files:
        f = open(os.path.join(root, filename), "r")
        #print(os.path.join(root, filename))
        count=count+1
        if count%20000==0:
            print(count)
        content = f.read()
        match = re.search("(Bug|Bugs|bug|bugs|Fix|fix|Fixed|fixed)[# \t]*([0-9]+)", content)
        if match:
            #print(match)
            #print(match.group(0))
            #print(match.group(1))
            #print(match.group(2))
            s=set.union(s, {match.group(2)})
        f.close
print(str(count)+"\n")        
print("print bug ID")
w=open(wn,'w')
for bug_id in s:
    w.write(bug_id)
    w.write("\n")
w.seek(0)
w.close
