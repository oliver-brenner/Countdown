from timeit import default_timer
import re

def is_match(scramble, word):
    word = list(word)
    
    for letter in scramble:
        if letter in word:
            word.remove(letter)
        
        if len(word) == 0:
            return True            
    
    return False

def parse_dictionary(filename, scramble):
    anagrams = list(list() for i in range(len(scramble) - 1))
    
    with open(filename) as dictionary:
        for word in dictionary:
            word = word.rstrip()
            
            if len(scramble) >= len(word):
                if is_match(scramble, word):
                    anagrams[len(word) - 2].append(word)
    
    return anagrams

def main():
    scramble = input("Enter up to nine letters: ")
    
    if not scramble.isalpha():
        print("Enter letters only.")
        return
    
    if len(scramble) > 9:
        print("Enter up to nine letters only.")
        return
    
    start = default_timer()
    anagrams = parse_dictionary("dictionary.txt", scramble)
    end = default_timer()
    
    j = 0
    for i in range(len(anagrams) - 1, -1, -1):
        if j < 3:
            if anagrams[i]:
                j += 1
                print(i + 2, "letter words:", ', '.join(anagrams[i]))
    
    if j == 0:
        print("There were no anagrams found for those letters.")
    else:
        print("Time taken: {}{}".format(end - start, 's')) 

if __name__ == "__main__":
    main()