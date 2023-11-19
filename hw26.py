n=int(input())#人口
m=int(input())#計算期間
a=int(input())#確診人數
b=float(input())#傳染人數
c=int(input())#康復天數
d=float(input())#免疫率
def cal(n,m,a,b,c,d):
    h=int(d*n)#免疫人
    total=0
    data=[]
    data.append([0,0,0,0])
    data.append([1,a,a,0])
    recover=0
    print(data[1][0],data[1][1],data[1][2],data[1][3])
    for day in range(2,m+1):
        x=int((b/c)*(1-d)*a)
        a=x+data[day-1][1]
        data.append([day,x+data[day-1][1],x,recover])
        if(data[day][1]>=n-h or h+data[day][1]==n):
            data[day][1]=n-h
            a=n-h
            data[day][2]=n-h-data[day-1][1]
            x=n-h-data[day][1]
        if(day-c>=1):
            a-=data[day-c][2]
            data[day][1]-=data[day-c][2]
            data[day][3]=data[day-c][2]
            d+=data[day-c][2]/n
            h+=data[day-c][2]
        print(data[day][0],data[day][1],data[day][2],data[day][3])
    for i in range(1,m+1):
        total+=data[i][2]
    return total
print(cal(n,m,a,b,c,d))
