import nltk
import pickle
import os
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


path = "C:/Users/kbm60/OneDrive/Desktop/CSE508_Winter2023_Dataset"
os.chdir(path)

d={}
count=0
for file in os.listdir():
    count=count+1
    with open(f"{path}\{file}", 'r') as f:
        data=f.read()
        tokens=nltk.word_tokenize(data)
        f.close()
    for i in tokens:
        if i not in d:
            d[i]={count}
        else:
            d[i].add(count)    

p="C:/Users/kbm60/OneDrive/Desktop/Unigram.txt"
fi=open(p,"wb")
pickle.dump(d,fi,protocol=pickle.HIGHEST_PROTOCOL)
fi.close()

fil=open(p,"rb")
a=pickle.load(fil)
print(a)
fil.close()