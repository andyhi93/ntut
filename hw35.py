def find_zero(s_data):
    con=[]
    ans=[]
    temp=s_data.split(" + ")
    for i in temp:con.append(i.split())
    for i in con:
        for k in data.keys():
            c=0
            for j in i:
                if j in data.get(k):
                    c+=1
                    if c==len(i):
                        ans.append(k)
    ans=set(sorted(ans,key=lambda x:sort_data.index(x)))
    for i in ans:print(i,end=" ")
data={}
for i in range(int(input())):
    temp=input().split()
    data[temp[0]]=temp[1:]
sort_data=[i for i in data.keys()]
search_data=[]
for i in range(int(input())):search_data.append(input())
choose=int(input())
if choose==0:
    for i in search_data:
        find_zero(i)