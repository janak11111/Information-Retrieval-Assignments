import re
import os
import nltk
import string
from nltk.corpus import stopwords
nltk.download('stopwords')



path = "C:/Users/muska/OneDrive/Desktop/CSE508_Winter2023_Dataset"

os.chdir(path)

def in_range(s, a, b):
    try:
        r = rf'{a}(.*?){b}'
        return re.findall(r, s)
    except ValueError:
        return -1

def print_5_sample():
    i=0
    for doc in os.listdir():
        if(i>4):
            break
        i=i+1
        with open(f"{path}\{doc}", 'r') as f:
            print("File ",i)
            print("\n")
            print(f.read())
            print("\n")

def relevant_text_extraction():
    for file in os.listdir():
        with open(f"{path}\{file}", 'r') as f:
            data =f.read()
            data=' '.join(data.splitlines())
            f1 = in_range(data,"<TITLE>", "</TITLE>")
            f2 = in_range(data,"<TEXT>", "</TEXT>")
            contain=f1[0]+f2[0]
            f.close()
            f = open(f"{path}\{file}","w")
            f.seek(0)
            f.truncate()
            f.write(contain)
            f.close()

def lower_case():
    for file in os.listdir():
        with open(f"{path}\{file}", 'r+') as f:
            data=f.read()
            data=data.lower()
            f.seek(0)
            f.truncate()
            f.write(data)
            f.close()

def tokenize():
    i=1 
    for file in os.listdir():
        with open(f"{path}\{file}", 'r+') as f:
            data=nltk.word_tokenize(f.read())
            if(i<6):
                print("\nFile ",i)
                print("\n")
                print(data)
            i=i+1
            f.close()
            

def remove_stop_word():
    for file in os.listdir():
        with open(f"{path}\{file}", 'r+') as f:
            word = set(stopwords.words('english'))
            tok = nltk.word_tokenize(f.read())
            rw=[]
            for w in tok:
                if w not in word:
                    rw.append(w)
            sen=''        
            for x in rw:
                sen += x+' '
            f.seek(0)
            f.truncate()
            f.write(sen)
            f.close()    

def remove_punctuations():   
    for file in os.listdir():
        with open(f"{path}\{file}", 'r+') as f:
            p=str(f.read())
            p = p.translate(str.maketrans('', '', string.punctuation))
            f.seek(0)
            f.truncate()
            f.write(p)
            f.close()

def remove_blank_space():
    for file in os.listdir():
        with open(f"{path}\{file}", 'r+') as f:
            b=str(f.read())
            b= re.sub(r"\s+", " ", b, flags=re.UNICODE)
            f.seek(0)
            f.truncate()
            f.write(b)
            f.close()


def main():
    #print("Before Operations\n")
   # print_5_sample()
    #relevant_text_extraction()
   # print("\nAfter Operations\n\n")        
    #print_5_sample()
    print("\nBefore Lowercase\n")
    print_5_sample()
    lower_case()
    print("\nAfter Lowercase the text\n\n")  
    print_5_sample()
    print("\nBefore Tokenization\n")
    print_5_sample()
    tokenize()
    print("\nAfter Performing Tokenization\n\n") 
    print("\nBefore removing stop words\n")
    print_5_sample()
    remove_stop_word()
    print("\nAfter Removing Stop Words\n\n") 
    print_5_sample()
    print("\nBefore removing punctuations\n")
    print_5_sample()
    remove_punctuations()
    print("\nAfter Removing Punctuations\n\n") 
    print_5_sample()
    print("\nBefore removing blank space\n")
    print_5_sample()
    remove_blank_space()
    print("\nAfter Removing blank space\n\n") 
    print_5_sample()


main()