n,start=[int(x) for x in input().split()]
data={}
end=[]
for i in range(int(n)):
    temp=[int(x) for x in input().split()]
    data[temp[0]]=temp[1::]
    if(temp[1]==0):end.append(temp[0])
def advantrue(start,end,passed,gold):
    print(passed,start)
    if(start in end or start in passed):
        return [gold]
    for i in data.keys():
        if(i not in passed and i in data.get(start)[1::]):
            ans=advantrue(i, end, passed+[start], gold+data.get(i)[0])
    return ans
count=advantrue(start, end, [], data.get(start)[0])
print(count)