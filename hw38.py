n,start=[int(x) for x in input().split()]
data={}
end=[]
for i in range(int(n)):
    temp=[int(x) for x in input().split()]
    data[temp[0]]=temp[1::]
    if(temp[1]==0):end.append(temp[0])
def advantrue(start,end,passed,gold,finalAns)->list:
    if(start in end or (data.get(start)[1] in passed and data.get(start)[2] in passed)):
        return [gold]
    for i in data.keys():
        if(i not in passed and i in data.get(start)[1::]):
            ans=advantrue(i, end, passed+[start], gold+data.get(i)[0],finalAns)
            for j in ans:
                if j not in finalAns:finalAns.append(j)
    return finalAns
print(max(advantrue(start, end, [], data.get(start)[0],[])))