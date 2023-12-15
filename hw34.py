num=int(input())
data={}
while True:
    temp=input().split()
    if(len(temp)==1):break
    data[temp[0]+temp[1]]=int(temp[2])
temp=set()
for i in data.keys():
    temp.update(i[0],i[1])
letters="".join(i for i in temp)
def arrangement(clist):
    if len(clist)==1:
        return clist
    ans=[]
    for idx,item in enumerate(clist):
        ans += [item+substr for substr in arrangement(clist[:idx] + clist[idx+1:])]
    return ans
def combo(clist):
    combos=[]
    for i in range(1,2**len(clist)):
        bnum="{0:b}".format(i).zfill(len(clist))#zfill填零
        combos.append(''.join(c for c,b in zip(clist,bnum) if int(b)))#zip把資料便二維儲存
    return combos
def determine(s):
    if(len(s)==1):
        return True
    for i in data.keys():
        if(s[:2]==i):
            return determine(s[1:])
            break
    return False
def f_count(c):
    value=0
    if(len(c)==2):
        return min(data[c],data[c[::-1]])
    value+=min(data[c[:2]],data[c[1::-1]])+f_count(c[1:])
    return value
all_combo=[perm for comb in combo(letters) for perm in arrangement(list(comb))]
new_combo=[]
for item in all_combo:
    if item[0]=="A" and item[-1]=="B":
        new_combo.append(item)
result=[]
for i in new_combo:
    if(determine(i)):
        result.append(i)
result=sorted(result,key=lambda x:len(x))
print(len(result[0])-1)
print(' '.join(result[0]))
print(max([f_count(i) for i in result]))
print(' '.join(result[-1]))