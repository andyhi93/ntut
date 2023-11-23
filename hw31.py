state=0
data=[]
temp=[0]
def binary(v,digit):
    new_v=""
    for i in range(digit):
        new_v+=str(v%2)
        v=v//2
    return new_v[::-1]
def gray(v):
    print(v)
    new_v=v[0]
    for i in range(len(v)-1):
        print(int(v[i]),int(v[i+1]))
        new_v+=str(int(v[i])^int(v[i+1]))
    return new_v
while(temp[0]!=-1):
    temp=input().split()
    if temp[0]=='-1':
        break
    state=binary(int(temp[0]),int(temp[1]))
    data.append(gray(state))
print(data)
for i in data:
    print(i)