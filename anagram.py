import itertools

def generate_anagram(word):
    perms=[''.join(p) for p in itertools.permutations(word)]
    return perms

with open('password2.lst', 'r') as file:
    words = [line.strip() for line in file]

anagrams = []
for word in words:
    word_anagrams = generate_anagram(word)
    anagrams.extend(word_anagrams)

with open ('anagram.lst' ,'w') as file:
    for anagram in anagrams:
    	file.write(anagram+'\n')
