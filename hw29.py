state=0
data=[]
def cal(v):
    if v==0 or v==1:
        return 0
    elif v%2==0:
        v=v/2
        return cal(v)+1
    else:
        v=(v+1)/2
        return cal(v)+1
def binary(v,digit):
    new_v=""
    for i in range(digit):
        new_v+=str(v%2)
        v=v//2
    return new_v[::-1]
while(state==0):
    data.append(cal(int(input(),2)))
    state=int(input())
for i in data:
    print(binary(i,4))