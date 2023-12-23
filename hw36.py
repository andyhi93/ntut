N,start,end=input().split()
break_p=input().split()
data=[]
for i in range(int(N)):
    temp=input().split()
    data.append(temp)
def path(start,end,tempAns,finalAns):
    if(start==end):
        return [tempAns]
    for i in data:
        if(start in i):
            next=i[1-i.index(start)]
            if(next not in tempAns):
                ans=path(next, end, tempAns+[next], finalAns)
                for j in ans:
                    if(j not in finalAns):
                        finalAns.append(j)
    return finalAns
tempAns=path(start, end, [start], [])
if(len(tempAns)==0):print('NO')
else:
    ans=[]
    for i in break_p:
        for j in tempAns:
            if(i in j and j not in ans):
                ans.append(j)
    ans=list(min(ans,key=lambda x:len(x)))
    for i in break_p:
        if(i in ans):
            print(i)
            print(" ".join(ans))