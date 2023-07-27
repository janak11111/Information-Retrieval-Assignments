import os
import nltk
import math
import numpy as np
import pandas as pd
import operator

path = "C:/Users/muska/OneDrive/Desktop/IR_ASS1/Preprocess_Dataset"
os.chdir(path)

corpus=[]
unique_words=[]
for file in os.listdir():
    with open(f"{path}\{file}", 'r') as f:
        data=f.read()
        tokens=nltk.word_tokenize(data)
        tokens=[x for x in tokens if not any(c.isdigit() for c in x)]
        corpus_np=np.array(tokens)
        corpus_np=np.unique(corpus_np)
        unique_words+= list(corpus_np)
        corpus.append(tokens)
        f.close()

corpus_np=np.array(unique_words)  
unique_words=np.unique(corpus_np)  
print(len(unique_words))  

dic={}
c=0
for u in unique_words:
    for l in corpus:
        if u in l:
            c+=1   
    dic[u]=c
    c=0            

idf={}
for i in dic:
    x=math.log((1400/dic[i])+1)
    idf[i]=x

def binary_count():
    b = [ [0]*1400 for i in range(len(unique_words))]
    for a,i in enumerate(unique_words):
        for j,k in enumerate(corpus):
            if i in k:
                b[a][j]=1
            else:
                b[a][j]=0 
    df=pd.DataFrame(b,index=unique_words) 
    #print(df) 
    return b          
#binary_count()          

def binary_count_tfidf():
    b = binary_count() 
    for a,i in enumerate(unique_words):
        for j,k in enumerate(corpus):
            b[a][j]=b[a][j]*idf[i]
    df=pd.DataFrame(b,index=unique_words)
    #print(df)
    return b
binary_count_tfidf()

def binary_query():
    query=unique_words
    b=binary_count_tfidf()
    doc={}
    for i,j in enumerate(corpus):
        val=0
        for k,q in enumerate(query):
            if q in j:
                val=val+b[k][i]
        doc[i]=val
    doc=dict(sorted(doc.items(),key=operator.itemgetter(1),reverse=True))
    show=dict(list(doc.items())[0:5])
    print(show)
binary_query()

def raw_count():
    b = [ [0]*1400 for i in range(len(unique_words))]
    for a,i in enumerate(unique_words):
        for j,k in enumerate(corpus): 
            b[a][j]=k.count(i)
    df=pd.DataFrame(b,index=unique_words) 
    print(df)
    return b
raw_count()

def raw_count_tfidf():
    b = raw_count() 
    for a,i in enumerate(unique_words):
        for j,k in enumerate(corpus):
            b[a][j]=b[a][j]*idf[i]
    df=pd.DataFrame(b,index=unique_words)
    print(df)
    return b
raw_count_tfidf()

def raw_query():
    query=unique_words
    b=raw_count_tfidf()
    doc={}
    for i,j in enumerate(corpus):
        val=0
        for k,q in enumerate(query):
            if q in j:
                val=val+b[k][i]
        doc[i]=val
    doc=dict(sorted(doc.items(),key=operator.itemgetter(1),reverse=True))
    show=dict(list(doc.items())[0:5])
    print(show)
raw_query()

def term_frequency():
    s=[]
    lis=[]
    for a,i in enumerate(corpus):
        for j in i:
            lis.append(i.count(j))
        s.append(sum(lis))
        lis=[]

    b = [ [0]*1400 for i in range(len(unique_words))]
    lis=[]
    for a,i in enumerate(unique_words):
        for j,k in enumerate(corpus): 
            m=s[j]-k.count(i)
            if(m==0):
                m=1
            b[a][j]=(k.count(i)/m)
            lis=[]
    df=pd.DataFrame(b,index=unique_words)
    print(df)
    return b
#term_frequency()

def term_frequency_tfidf():
    b = term_frequency() 
    for a,i in enumerate(unique_words):
        for j,k in enumerate(corpus):
            b[a][j]=b[a][j]*idf[i]
    df=pd.DataFrame(b,index=unique_words)
    print(df)
    return b
term_frequency_tfidf()

def frequency_query():
    query=unique_words
    b=term_frequency_tfidf()
    doc={}
    for i,j in enumerate(corpus):
        val=0
        for k,q in enumerate(query):
            if q in j:
                val=val+b[k][i]
        doc[i]=val
    doc=dict(sorted(doc.items(),key=operator.itemgetter(1),reverse=True))
    show=dict(list(doc.items())[0:5])
    print(show)
frequency_query()

def log_normalization():
    b = [ [0]*1400 for i in range(len(unique_words))]
    for a,i in enumerate(unique_words):
        for j,k in enumerate(corpus): 
            b[a][j]=math.log(1+k.count(i))
    print(b[7])
    df=pd.DataFrame(b,index=unique_words) 
    print(df)
    return b
# log_normalization()

def log_normalization_tfidf():
    b = log_normalization() 
    for a,i in enumerate(unique_words):
        for j,k in enumerate(corpus):
            b[a][j]=b[a][j]*idf[i]
    df=pd.DataFrame(b,index=unique_words)
    print(df)
    return b
#log_normalization_tfidf()

def normalize_query():
    query=unique_words
    b=log_normalization_tfidf()
    doc={}
    for i,j in enumerate(corpus):
        val=0
        for k,q in enumerate(query):
            if q in j:
                val=val+b[k][i]
        doc[i]=val
    doc=dict(sorted(doc.items(),key=operator.itemgetter(1),reverse=True))
    show=dict(list(doc.items())[0:5])
    print(show)
normalize_query()

def double_normalization():
    m_m = [ [0]*2 for i in range(1400)]
    lis=[]
    for a,i in enumerate(corpus):
        for j in i:
            lis.append(i.count(j))
        lis.sort()
        m_m[a][0]=lis[-1]
        if(len(lis)>1):
            m_m[a][1]=lis[-2]
        else:
            m_m[a][1]=1
        lis=[]
   
    b = [ [0]*1400 for i in range(len(unique_words))]
    lis=[]
    for a,i in enumerate(unique_words):
        for j,k in enumerate(corpus): 
            if k.count(i)==m_m[j][0]:
                m=m_m[j][1]
            else:
                m=m_m[j][0]
            b[a][j]=0.5+0.5*(k.count(i)/m)
            lis=[]
    df=pd.DataFrame(b,index=unique_words) 
    print(df)
    return b
double_normalization()

def double_normalization_tfidf():
    b = double_normalization() 
    for a,i in enumerate(unique_words):
        for j,k in enumerate(corpus):
            b[a][j]=b[a][j]*idf[i]
    df=pd.DataFrame(b,index=unique_words)
    print(df)
    return b
double_normalization_tfidf()

def double_query():
    query=unique_words
    b=double_normalization_tfidf()
    doc={}
    for i,j in enumerate(corpus):
        val=0
        for k,q in enumerate(query):
            if q in j:
                val=val+b[k][i]
        doc[i]=val
    doc=dict(sorted(doc.items(),key=operator.itemgetter(1),reverse=True))
    show=dict(list(doc.items())[0:5])
    print(show)
double_query()    