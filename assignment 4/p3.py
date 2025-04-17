def is_pangram(sentence):
    
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    
    
    sentence_set = set(sentence.lower())
    
   
    if alphabet_set.issubset(sentence_set):
        return "pangram"
    else:
        return "not pangram"


sentence = input("Enter a sentence: ")
print(is_pangram(sentence))
