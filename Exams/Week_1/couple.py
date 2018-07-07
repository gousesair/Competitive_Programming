def check(l):
   n=len(l)
   couple=[None]*n
   for i, p2 in enumerate(l):
       couple[p2]=i
   count=0
   for i in range(0,n,2):
       x, z=l[i:i+2]
       y=x-1 if x%2 else x+1
       if y!=z:
           j=couple[y]
           l[j]= z
           couple[z]=j
           count+=1
   return count 

print(check([1,3,4,0,2,5]))
print(check([3,2,0,1]))
print(check([1,0]))