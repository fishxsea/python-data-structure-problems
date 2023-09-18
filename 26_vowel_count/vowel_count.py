def is_vowel(letter):
    vowels = 'aeiou'
    if letter in vowels:
        return True
    

def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    
    phrase = phrase.lower()
    vowel_dict = {}
    for letter in phrase:
        if is_vowel(letter):
            if letter not in vowel_dict.keys():
                vowel_dict[letter] = 1
                print(letter)
                continue
            vowel_dict[letter] += 1
    return vowel_dict
