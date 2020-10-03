
# retrieves the entire contents

from bs4 import BeautifulSoup        
import urllib 
from nltk.corpus import names
from nltk.tokenize import sent_tokenize
#content=urllib.request.urlopen("http://shakespeare.mit.edu/allswell/full.html")
#soup= BeautifulSoup(content,features="html.parser")
count=0

"""x=open("shakespeare.txt","wt")
x.write(soup.text)
x.close()"""
all_names=set(names.words())
print("DONE")
x=open("shakespeare.txt","r")

r=x.read()
x.close()
l=[ [i for i in x.split()]  for x in sent_tokenize(r) ]
print(l)
for i,a in enumerate(l):
    print("{ "+str(i)+" } "  ,sep=" ")
    print(a)
    print()
for a in l:
    if a[0]=="BERTRAM":
        count=count+1
print(count) 

#97       
      
