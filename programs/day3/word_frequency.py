def wordfreq(sentence):
    words=sentence.lower().split()
    freq={}
    for w in words:
        if w in freq:
            freq[w]+=1
        else:
            freq[w]=1
    return freq        
