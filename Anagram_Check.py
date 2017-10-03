# Anagram Check
# Compares 2 Strings for Anagram

def strdict(word):
    word = word.replace(' ',"")
    word = list(word)    
    res = {}
    for w in word:
        try:
            res[w] = res[w] + 1
        except:
            res[w] = 1
    return res    
   

def anag(check1, check2):   
    if(len(strdict(check1).items() & strdict(check2).items()) == len(strdict(check1).items() | strdict(check2).items())):
        return True
    else:
        return False