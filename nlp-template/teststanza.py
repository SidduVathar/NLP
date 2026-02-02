import stanza
txt="Well, I wouldn’t really call it a 'date' – at least not if I don’t want to end up as a coat for Miss Piggy. Y’see, I just gave Lady Gaga a ride to the VMAs, and when Lady Gaga lefther credentials in the limo, I had to bring them to her. (On the off-chance security didn t recognize her. Hey, it could happen.) Of course, after Lady Gaga and I were seen on the red carpet together, well Miss Piggy got a little jealous. But I definitely did get a ride home – in the trunk"
txt=txt.replace("n’t"," not")
txt=txt.replace("didn t","did not")
# print(txt)


pipeline = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
doc = pipeline(txt)

#Output to see
for i, sentence in enumerate(doc.sentences):
    print(f'====== Sentence {i+1} tokens =======')
    for token in sentence.words:
        if token.deprel=="nsubj":
            subj=token.lemma
            # print(token.lemma)  #Print the subject of the sentence
            for prop in sentence.words:
                if prop.head==token.id and prop.upos=="PROPN":  #Proper Noun
                    subj=subj+prop.lemma
            print(subj)

        if token.deprel=="root":
            verb=token.lemma
            for prop in sentence.words:
                if prop.head==token.id and prop.upos=="AUX":   #Auxiliary verb
                    verb= prop.lemma + verb
                if prop.head==token.id and prop.lemma=="not" and prop.deprel=="advmod":
                    verb=verb + prop.lemma
            print(verb)

        if token.deprel=="obj":
            obj=token.lemma
            for prop in sentence.words:
                if prop.head==token.id and prop.upos=="PROPN":
                    obj= obj + prop.lemma
            print(obj)
    # print(*[f'{token}' for token in sentence.tokens], sep='\n')




    # for i, sentence in enumerate(doc.sentences):
    # print(f'====== Sentence {i+1} tokens =======')
    # for token in sentence.words:
    #     if token.deprel=="nsubj":
    #         subj=token.lemma
    #         # print(token.lemma)  #Print the subject of the sentence
    #         for prop in sentence.words:
    #             if prop.head==token.id and prop.upos=="PROPN":
    #                 subj=subj+prop.lemma
    #         print(subj)
    # # print(*[f'{token}' for token in sentence.tokens], sep='\n')