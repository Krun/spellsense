import enchant
import context

def check(sentence):
    c = context.Context()
    corrected = ""
    d = enchant.Dict("en_US")
    words = sentence.split()
    for word in words:
        if d.check(word):
            c.addWord(word)
        else:
            c.addWord('')
    #print "[Context] red words are " 
    #print c.lastwords
    for i in range(len(words)):
        word=words[i]
        if len(corrected):
            corrected += " "
        if d.check(word):
            corrected += word
        else:
            possible = d.suggest(word)
            chosen = c.getBestWord(possible,i)
            c.addWord(chosen,i)
            corrected += chosen
    #print "[Context] final words are " 
    #print c.lastwords
    return corrected

def dumbcheck(sentence):
    c = context.Context()
    corrected = ""
    d = enchant.Dict("en_US")
    words = sentence.split()
    for word in words:
        if len(corrected):
            corrected += " "
        if d.check(word):
            corrected += word
        else:
            chosen = d.suggest(word)[0]
            corrected += chosen
    return corrected
