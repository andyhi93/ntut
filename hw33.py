def find_max(v):
    min_d=100
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            temp=count_d(v[i][1], v[i][2], v[i][3], v[j][1],v[j][2],v[j][3])
            if(temp<min_d and [v[i][0],v[j][0]]+v[i][1:]+v[j][1:] not in ans):
                min_d=temp
                ans[digit]=[v[i][0],v[j][0]]+v[i][1:]+v[j][1:]
def count_d(x1,y1,z1,x2,y2,z2):
    return abs(((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5)
data=[]
digit=0
ans=[[0],[0],[0]]
for i in range(int(input())):
    temp=input().split()
    for j in range(4):
        temp[j]=int(temp[j])
    data.append(temp)
for i in range(3):
    find_max(data)
    digit+=1
for i in ans:
    for j in i:
        print(j,end=" ")
    print()