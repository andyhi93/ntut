A,B,X,Y=input(),input(),input(),input()
C=A+" "+B
print(C)
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
temp=C.split(" ")
exc_codeX=[]
exc_codeY=[]
for i in range(len(X)):
    if(X[i] in letters):
        if(letters.index(X[i])>25):
            exc_codeX.append(letters.index(X[i])-26)
        else:            
            exc_codeX.append(letters.index(X[i]))
for i in range(len(Y)):
    if(Y[i] in letters):
        if(letters.index(Y[i])>25):
            exc_codeY.append(letters.index(Y[i])-26)
        else:            
            exc_codeY.append(letters.index(Y[i]))
for v in temp:
    temp_code=[]
    correct=0
    if(len(v)==len(X)):
        for i in range(len(v)):
            if(v[i] in letters):
                if(letters.index(v[i])>25):
                    temp_code.append(letters.index(v[i])-26)
                else:            
                    temp_code.append(letters.index(v[i]))
            else:
                temp_code[0]=-1
        for i in range(len(X)):
            if(temp_code[i]==exc_codeX[i]):
                correct+=1
        if(correct==len(X)):
            temp[temp.index(v)]=Y
D=""
for i in temp:D+=i+" "
print(D)
temp_len=""
for i in C.split(" "):temp_len+=i
print(len(temp_len),end=" ")
temp_len=""
for i in temp:temp_len+=i
print(len(temp_len))
temp=D.split()
for v in D.split():
    temp_code=[]
    correct=0
    if(len(v)==len(Y)):
        for i in range(len(v)):
            if(v[i] in letters):
                if(letters.index(v[i])>25):
                    temp_code.append(letters.index(v[i])-26)
                else:            
                    temp_code.append(letters.index(v[i]))
            else:
                temp_code.append(-1)
        for i in range(len(Y)):
            if(temp_code[i]==exc_codeY[i]):
                correct+=1
        if(correct==len(Y)):
            temp[temp.index(v)]=v[::-1]
for i in temp:print(i,end=" ")
print()
delta=abs(len(X)-len(Y))
repeat=0
for i in range(0,len(C),delta):
    if(C[i]==" "):
        repeat+=1
    else:
        repeat=0
    if(repeat<2):
        print(C[i],end="")