import string
def is_prime(n):
    for i in range(2,n):
        if n%i==0:return False
    return True
def find(s):
    if len(s)==0:
        return None
    if s[:len(front)]==front:
        for i in range(len(front),len(s)):
            if(s[i:i+3] in behind):
                clip=s[len(front):i]
                if is_prime(len(clip)) and clip not in gene:
                    gene.append(clip)
                for j in range(len(front),len(s)):
                    if s[j:j+len(front)]==front:
                        find(s[j:])
                        break
                break
front=input()
behind=input().split()
DNA=input()
gene=[]
find(DNA)
letters=string.ascii_uppercase
if len(gene)==0:
    print('No gene')
else:
    gene=sorted(gene)
    gene=sorted(gene,key=lambda x:len(x))
    for i in gene:
        print(i)