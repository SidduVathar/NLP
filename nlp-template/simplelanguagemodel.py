import stanza
import random

N = 3
f = open("cats.txt", "r")
txt = f.read()

pipeline = stanza.Pipeline(lang='en', processors='tokenize')
doc = pipeline(txt)

# print(doc)

vocabulary = []
ngrams = {}
n = 0;

ngram = []
for i, sentence in enumerate(doc.sentences):
    for token in sentence.words:
        t = token.text.lower()
        if len(ngram) < N:
            ngram.append(t)
        else: 
            # print(ngram)
            key = '_'.join(ngram)
            print(key)
            if not key in ngrams:
                ngrams[key] = {}

            if not t in ngrams[key]:
                ngrams[key][t] = 1
            else:
                ngrams[key][t] += 1
 
            ngram = ngram[1:]
            # print(ngram)
            ngram.append(t)

        if not t in vocabulary:
            vocabulary.append(t)
        n += 1

# print(n)

# print(vocabulary)
# print(str(len(vocabulary)))
# print(ngrams)

def getNextToken(ngram):
    key = '_'.join(ngram)
    frequencies = ngrams[key]
    
    sum = 0
    for token in frequencies:
        sum += frequencies[token]

    if sum == 1:
        for token in frequencies:
            return token
    
    r = random.randrange(1,sum)
    sum = 0
    for token in frequencies:
        sum += frequencies[token]
        if r <= sum:
            return token        

    return '.'


random.seed()
prompt = ['a','black','cat','tears']
print(' '.join(prompt))
for i in range(0,30):
    t = getNextToken(prompt)
    print(' '+t)
    prompt = prompt[1:]
    prompt.append(t)
