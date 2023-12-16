def find_zero(s_data):
    con=[]
    temp=s_data.split(" + ")
    for i in temp:con.append(i.split())
    for i in data.keys():
        temp=data.get(i)
        for j in con:
            count=0
            for k in j:
                if k in i:count+=1
            if count==len(i):
                print(i.end=" ")
data={}
for i in range(int(input())):
    temp=input().split()
    data[temp[0]]=temp[1:]
print(data)
search_data=[]
for i in range(int(input())):search_data.append(input())
print(search_data)
choose=int(input())
if choose==0:
    for i in search_data:
        print(i)
        find_zero(i)