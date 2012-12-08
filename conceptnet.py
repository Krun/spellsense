import urllib2
import json
import re


__DATAURL = 'http://conceptnet5.media.mit.edu/data/concept/en/'
__CNETURL = 'http://conceptnet5.media.mit.edu/data'
__INEDGES_KEY = 'incoming_edges'
__PROPERTIES_KEY = 'properties'
__NAME_KEY = 'name'
__TASK_WORDS = ["buy","prepare","choose","reserve","decide","purchase","take","bring","find","go to","get"]

import urllib2
import json
import re


__DATAURL = 'http://conceptnet5.media.mit.edu/data/concept/en/'
__CNETURL = 'http://conceptnet5.media.mit.edu/data'
__INEDGES_KEY = 'incoming_edges'
__PROPERTIES_KEY = 'properties'
__NAME_KEY = 'name'
__TASK_WORDS = ["buy","prepare","choose","reserve","decide","purchase","take","bring","find","go to","get"]
__MAX_RETRIES = 5

def __getData(node, retries=0):
    node = urllib2.quote(node)
    graph = None
    try:
        graph = urllib2.urlopen(__DATAURL+node)
    except urllib2.URLError, e:
        if retries > __MAX_RETRIES:
            print "[Error] Can't connect to ConceptNet"
            return []
        else:
            return __getData(node, retries+1)

    jgraph = json.load(graph)
    edges = jgraph.get(__INEDGES_KEY)
    taskedges = []
    [taskedges.extend(__isATask(edge)) for edge in edges if __isATask(edge)]
    return taskedges
    
def __tryAllNames(node):
    tasks = []
    names = __getNames(node)
    for n in names:
        newtasks = __getData(n)
        [tasks.append(i) for i in newtasks if not tasks.count(i)] 
    return tasks
    

def __isATask(edge):
    start = None
    try:
        start = edge['start']
    except:
        return False
    params = start.split(',')
    params[0] = ''
    res = []
    for a in params:
        if re.match('.*concept.*',a):
            res.append(re.sub("]", "", a))
    return res
    
def __getNames(name):
    name = name.lower()
    alternatives = []
    alternatives.append(name)
    alt1 = re.sub("ing", "", name)
    if not alternatives.count(alt1):
        alternatives.append(alt1)
    return alternatives

def nodeProperties(url):
    node = urllib2.urlopen(__CNETURL + url)
    jgraph = json.load(node)
    edges = jgraph.get(__PROPERTIES_KEY)
    
def nodeName(url):
    realname = url.split('/')
    lastpart = realname[-2]
    lastpart = re.sub("_", " ", lastpart)
    #print "[ConceptNet] name for "+url+" is "+lastpart
    return lastpart
    #print "[ConceptNet] getting name for "+url
    #node = urllib2.urlopen(__CNETURL + url)
    #jgraph = json.load(node)
    #edges = jgraph.get(__PROPERTIES_KEY)
    #name = edges.get(__NAME_KEY)
    #return name
    
def tasks(node):
    taskedges = __tryAllNames(node)
    retList = []
    retList.append("Bring money")
    retList.append("Have fun")
    if len(taskedges):
        retList = [nodeName(url) for url in taskedges]
    return retList
            
def conceptsAbout(node):
    return tasks(node)

def wordsAbout(node):
    concepts = conceptsAbout(node)
    words = []
    [words.extend(concept.split()) for concept in concepts]
    return words
