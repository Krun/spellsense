import commonsense
class Context:
    lastwords = []
    related = {}

    def __init__(self):
        self.lastwords = []
        self.related = {}

    def addWord(self,word,pos=0):
        word = word.lower()
        if word not in self.related:
            if len(word) >= 3:
                self.related[word] = commonsense.relatedWords(word)
            else:
                self.related[word] = []
        if pos:
            self.lastwords.reverse()
            self.lastwords.pop(pos)
            self.lastwords.insert(pos,word)
            self.lastwords.reverse()
            return
        self.lastwords.insert(pos,word)

    def __shift(self, seqo, n):
        seq = list(seqo)
        seq.reverse()
        if n:
            n = n % len(seq)
            l1 = seq[:n]
            l1.reverse()
            l2 = seq[n:]
            return l1 + l2
        else:
            return seq

    def getBestWord(self,words, pos = 0):
        last = list(self.lastwords)
        last = self.__shift(last,pos)
        for cword in last:
            for word in words:
                if word in last or word in self.related[cword]:
                    return word
        return words[0]
    
    def printContext(self):
        print self.related

