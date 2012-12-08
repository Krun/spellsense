import conceptnet
import pickle

__CACHE = "cache.dat"

cache = None

def relatedWords(word):
    global cache
    if cache == None:
        try:
            pF = open(__CACHE)
            cache = pickle.load(pF)
            pF.close()
        except:
            print "[CommonSense] unable to load from "+__CACHE
            cache = {}
    if word in cache:
        return cache[word]
    else:
        data = conceptnet.wordsAbout(word)
        cache[word] = data
        try:
            pF = open(__CACHE, 'w')
            pickle.dump(cache, pF)
            pF.close()
        except:
            print "[CommonSense] unable to save cache"
        return data
            
