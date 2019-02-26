# -*- coding: utf-8 -*-

from pprint import pprint
from collections import defaultdict
csv="""
1,Dinesh,2
2,Ramesh,4
3,Sandeep,4
4,Abhishek,null
"""
def show_val(title, val):
    pprint(val)

lines = [ l.strip() for l in csv.strip().splitlines() ]
ppl = [ tuple(l.split(',')) for l in lines ]     #convert list into people tuples
len(ppl)
x=ppl[len(ppl)-1]
last=x[2]      #to iterate till last value since they are in the order, if not,consider maximum value 
#print(ppl,last)

emps = defaultdict(list)
for i in ppl:
    emps[i[2]].append(i)
#pprint(emps.keys())     #creating dict to build tree/ to access it easily according to the heirarchy
#pprint(emps.values())
#pprint(emps)

def buildtree(t=None, emp_eid=last):
    toemp = emps.get(emp_eid, None)   #contructing a data hierarchy
    if toemp is None:         #checking for parent node/top level employee
        return t
    for eid, name, mid in toemp:        
        level1={ 'name':name,'eid':eid} 
        if t is None:
            t = level1
        else:
            levels = t.setdefault('re-level',[])  
            levels.append(level1)
        buildtree(level1,eid)     #Building tree using the defined structure.
    return t

data = buildtree()
pprint(data)   

"""
Since I used tree structure I left the output to this point. The logic 
behind it is clear so my guess for the output too."""