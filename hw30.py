state=0
data=[]
def T(v):
    times=0
    for i in range(v+1):
        times+=cal(i)
    return times
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
while(state!=-1):
    state=int(input(),2)
    data.append(T(state))
for i in data[:-1]:
    print(binary(i,14))