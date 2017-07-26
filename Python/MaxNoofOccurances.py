import collections
a = [1,2,3,3,3,1,2,5,6,3,1,2,9,3,2]

d = {}

for i in a:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1
        
maxvalue = max(d.values())

for i,j in d.items(): 
      if j==maxvalue:
          print(i, "appears most of the times")