import stanza

N=3
f=open("cats.txt","r")
text=f.read()

pipeline = stanza.Pipeline(lang='en', processors='tokenize') #,mwt,pos,lemma,depparse')
doc = pipeline(text)



ngram=[]
vocabulary=[]
n=0

for i , sentence in enumerate(doc.sentences):
    for token in sentence.words:
        t=token.text.lower()
        if len(ngram) < N:
            ngram.append(t)
        else:
            print(ngram)
        
        
print(n)

print(vocabulary)
print("Verbs: "+str(len(vocabulary)))





# List the distinct words in the text/corpus of cats.txt

# vocabulary=[]
# n=0

# for i , sentence in enumerate(doc.sentences):
#     for token in sentence.words:
#         t=token.text.lower()
#         if not t in vocabulary:
#             vocabulary.append(t)
#         n+=1
        
# print(n)

# print(vocabulary)
# print("Verbs: "+str(len(vocabulary)))


