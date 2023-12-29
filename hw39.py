import copy
def line(form):
    for i in form:
        if i in c:form[form.index(i)]=" "
    point=0
    ciri=[]
    cirj=[]
    for i in range(n*n):
        if(form[i]==" "):
            ciri.append(i//n)
            cirj.append(i%n)
    for i in set(ciri):
        if(ciri.count(i)==n):point+=1
    for j in set(cirj):
        if(cirj.count(j)==n):point+=1
    ct=0
    for i in range(len(ciri)):
        if(ciri[i]==cirj[i]):ct+=1
    if ct==n:point+=1
    ct=0
    for i in range(len(ciri)):
        if(ciri[i]+cirj[i]==(n-1)):ct+=1
    if(ct==n):point+=1
    return point
n=int(input())
m=int(input())
a=input().split()
b=input().split()
c=input().split()
if line(a)==line(b):print('Tie')
elif line(a)>line(b):print('A Win')
else:print('B Win')