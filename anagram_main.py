#anagram creator

def create_wordslist(text_file: str)->list:
    '''converts word file into list of words'''
    words_list = []
    words_file  = open(text_file, "r")
    for word in words_file.readlines():
        words_list.append(word.strip('\n'))
    words_file.close()
    return words_list

def word_matcher(word: str, pick: str)-> bool:
    '''checks if two words match through letters and length'''
    match = list(pick)
    if len(word) != len(pick):
        return False
    for letter in word:
        if letter in match:
            match.remove(letter)
        else:
            return False
    return True
    
def anagram_creator(gram_in: list, all_words: list)-> list:
    '''returns finalized anagram'''
    anagram_final = ''
    for word in gram_in:
        for pick in all_words:
            if pick == all_words[-1]:
                anagram_final += word + "* "
                break
            if word_matcher(word.lower(), pick.lower()):
                if pick.lower() != word.lower() or len(word) <= 2:
                    anagram_final += pick + " "
                    break
    return anagram_final.strip()

def start_program():
    trans = input("Enter an anagram: ").strip().split()
    #if trans == "kill":
    #    return "kill"
    #else:
    known_words = create_wordslist("words.txt")
    answer = anagram_creator(trans, known_words)
    print("Anagram: " + answer)
    print()

while True:
    x = start_program()
    #if x == "kill":
    #    break





                
            





