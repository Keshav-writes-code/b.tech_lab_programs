import math
# Linear search function 
def lin_search(a,x):
  return next((i for i,v in enumerate(a) if v==x),-1) 
# Binary search function
def bin_search(a,l,h,x):
  if h>=l: 
    m=(h+l)//2
    if a[m]==x:return m # Element found
    elif a[m]>x:return bin_search(a,l,m-1,x) 
    else:return bin_search(a,m+1,h,x)
  return -1
print("Enter values in Ascending Order")
a=[]
i=1
while 1:
  v=input(f"Value {i} :- ") # Take input
  if not v:break
  a.append(int(v))
  i+=1
print("\nEntered elements: ",*a,sep=", ")
c=int(input("\n1. linear search\n2. binary search\nChoose an Algo :- "))
x=int(input("\nEnter element to search: "))
if c==1:r=lin_search(a,x) 
elif c==2:r=bin_search(a,0,len(a)-1,x)
else:print("Invalid choice")

# Print final result
print(["Element not found","Element found at index "+str(r)][r!=-1])
