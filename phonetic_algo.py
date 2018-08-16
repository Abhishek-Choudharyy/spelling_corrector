#Phonetic Algorithm
import phonetics 

def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1
 
    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
    return d[lenstr1-1,lenstr2-1]

def word_to_phonetic_distance(word1,word2):
    code_distance = dict()
    # weights
    weight = {  
        "soundex": 0.3,
        "metaphone": 0.5,
        "nysiis": 0.2
    }
    edit_distance = 0
    try:
        code_distance['soundex'] = weight['soundex'] * damerau_levenshtein_distance(phonetics.soundex(word1),phonetics.soundex(word2))
        code_distance['metaphone'] = weight['metaphone'] * damerau_levenshtein_distance(phonetics.metaphone(word1),phonetics.metaphone(word2))
        code_distance['nysiis'] = weight['nysiis'] * damerau_levenshtein_distance(phonetics.nysiis(word1),phonetics.nysiis(word2))
        # Edit distance according to weight vector
        edit_distance = code_distance['soundex'] + code_distance['metaphone'] + code_distance['nysiis']
    except:

        pass

    return(edit_distance)
    
print(word_to_phonetic_distance("smith","smyth"))

    

        
    