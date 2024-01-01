import math
classNameC=[]
classNameS=[]
department=[]
stu_semester=[]
class ClassData:
    def __init__(self,CourseCode,Semester,DataDict):
        self.CourseCode=CourseCode
        self.Semester=Semester
        self.DataDict={}
    def SaveData(self,s):
        temp=s.split()
        self.DataDict[temp[0]]=temp[1::]
def calculate(cd,stu_sem,class_sem):
    print(cd,stu_sem,class_sem)
    temp="_".join([cd,class_sem])
    stu_data=[]
    percnt=[1]
    for i in temp.DataDict.keys():
        if i[:3]==stu_sem:stu_data.append([i,point(temp.DataDict.get(i))])
    stu_data=sorted(stu_data,key=lambda x:x[1],reverse=True)
    for i in range(1,100):
        if len(percnt)==3:break
        if math.ceil(i*0.01*len(stu_data))-percnt[len(percnt)-1]!=0:
            percnt.append(i)
    for i in range(3):
        print(stu_data[i][0],stu_data[i][1],str(percnt[i])+'%','0%')
def point(p):
    if p=="w":return 0
    elif len(p)==2:return math.ceil(p[0]*0.7+p[1]*0.3)
    else: return p
for i in range(int(input())):
    temp=input().split()
    tname="_".join(temp[:2])#cd_classSem
    classNameS.append(tname)
    tname=ClassData(temp[0],temp[1],{})
    classNameC.append(tname)
    for j in range(int(temp[2])):
        tname.SaveData(input())
srch=input()
print(classNameC)
for i in classNameC:
    for j in i.DataDict.keys():
        print(j)
        department.append(int(j[3:6]))#科系
        stu_semester.append(int(j[:3]))#入學年
department=sorted(set(department))
stu_semester=sorted(set(stu_semester))
print(department,'\n',stu_semester)
for i in department:
    for j in stu_semester:
        