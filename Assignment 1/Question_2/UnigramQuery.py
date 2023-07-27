import nltk
import pickle
import os
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

p="C:/Users/muska/OneDrive/Desktop/Unigram_pickle_data.txt"
fil=open(p,"rb")
a=pickle.load(fil)
fil.close()

f=[]
c=1
n=int(input())
for i in range(0,n):
    print("Q:",c)
    c=c+1
    s=input()
    word = set(stopwords.words('english'))
    tok = nltk.word_tokenize(s.lower())
    rw=[]
    for w in tok:
        if w not in word:
            rw.append(w)
    sen=''        
    for x in rw:
        sen += x+' '
    p = sen.translate(str.maketrans('', '', string.punctuation))
    p= re.sub(r"\s+", " ", p, flags=re.UNICODE)
    p = nltk.word_tokenize(p)

    l=[]
    for j in range(0,len(p)-1):
        st=str(input())
        l.append(st.lower())
       

    x=[]
    y=0
    z=0
    for j in range(0,len(p)+len(l)):
        if j%2==0:
            x.append(p[y])
            y=y+1
        else:
            x.append(l[z])
            z=z+1

    sen=''        
    for k in x:
        sen += k+' '  
    f.append(sen)

count=0

def operation_or(v1,v2):
    global count
    res=[]
    m=len(v1)
    n=len(v2)
    a=0
    b=0

    while((a!=m) or (b!=n)):
        if(a==m):
            while(b!=n):
                res.append(v2[b])
                b+=1

        elif(b==n):
            while(a!=m):
                res.append(v1[a])
                a+=1

        elif(v1[a]==v2[b]):
            res.append(v1[a])
            a+=1
            b+=1
            count+=1 

        elif(v1[a]<v2[b]):
            res.append(v1[a])
            a+=1
            count+=1 

        else:
            res.append(v2[b])
            b+=1
            count+=1      
    return res

def operation_and(v1,v2):
    global count
    res=[]
    m=len(v1)
    n=len(v2)
    a=0
    b=0

    while((a!=m) and (b!=n)):
        if(v1[a]==v2[b]):
            res.append(v1[a])
            a+=1
            b+=1

        elif(v1[a]<v2[b]):
            a+=1

        else:
            b+=1
        count+=1
        
    return res    

def operation_and_not(v1,v2):
    global count
    value=operation_and(v1,v2)
    for i in value:
        v1.remove(i)
        count+=1  
    return v1    

def operation_or_not(v1,v2):
    global count
    value=operation_and_not(v2,v1)
    u=list(range(1,1401))
    for i in value:
        u.remove(i)
        count+=1
    return u




c=1
for i in range(0,len(f)):
    val=[]
    op=[]
    tok = nltk.word_tokenize(f[i])
    for j in range(0,len(tok)):
        if j%2==0:
            if tok[j] in a:
                val.append(a[tok[j]])
        else:
            op.append(tok[j])
    z=0
    v=[]
    while(len(val)!=1):
        val[0]=sorted(val[0])
        val[1]=sorted(val[1])
        if op[z]=="or":
            v=operation_or(list(val[0]),list(val[1]))

        elif op[z]=="and":
            v=operation_and(list(val[0]),list(val[1]))

        elif op[z]=="andnot":
            v=operation_and_not(list(val[0]),list(val[1]))

        elif op[z]=="ornot":
            v=operation_or_not(list(val[0]),list(val[1]))

        val.pop(0)
        val.pop(0)
        val.insert(0,set(v)) 
        z+=1
    nm=[]
    for j in val:
        j=sorted(j)
        for w in j:
            nm.append("cranfield"+f'{w:04}')
    print("Query %d : "%c,f[i])
    print("Number of documents retrieved for query %d: "%c,len(j))
    print("Names of documents retrieved for query %d: "%c,nm)     
    print("Number of comparisons required for query %d: "%c,count)
    count=0  
    c+=1
