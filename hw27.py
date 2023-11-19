number=int(input())
depth=int(input())
data=[["" for _ in range(7)]for _ in range(number)]
for i in data:
    temp_str=input()
    index=0
    floor=0
    state=[""]
    l=["{","(","["]
    r=["}",")","]"]
    while(index<len(temp_str)):
        if(temp_str[index] in ["{","(","["]):
            floor+=1
            i[floor]+=str(temp_str[index])
        elif(temp_str[index] in ["}",")","]"]):
            i[floor]+=str(temp_str[index])
            floor-=1
            if(floor<0):
                i[0]="fail"
                break
        else:
            i[floor]+=str(temp_str[index])
        index+=1
    if(floor!=0):
        i[0]="fail"
    else:
        for j in range(1,7):
            temp=""
            for k in range(len(i[j])):
                if(i[j][k] in ["{","(","[","}",")","]"]):
                    temp+=i[j][k]
            m=0
            while(m<len(temp)):
                if(l.index(temp[m])==r.index(temp[m+1])):
                   m+=1
                else:
                    i[0]="fail"
                    break
                m+=1
        if(i[0]!="fail"):
            for j in range(len(i[depth])):
                if(i[depth][j] not in ["{","}","[","]","(",")"]):
                    i[0]+=str(i[depth][j])
            if(i[0]==""):
                i[0]="EMPTY"
for i in data:
    if(i[0]!="fail"):
        print("pass,",i[0])
    else:
        print(i[0])