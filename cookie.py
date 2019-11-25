import enchant
from itertools import permutations

letters = []
print "Enter Done When You're Done"
i = ''
while (i.lower() != 'done'):
    i = raw_input("Enter a Letter: ")
    if (len(i) == 1):
        letters.append(i)
        print i.lower() + " added to the list"


print "these are your letters"
print letters

dc = enchant.Dict("en_US")

words = []
allPossible = list(permutations(letters,input("Number of Characters: ")))


for word in allPossible:
    mystring = ''
    for l in word:
        mystring += l
    if (dc.check(mystring)):
        words.append(mystring)

w2 = []

for word in words:
    l2 = letters[:]
    p = True
    for letter in word:
        if (letter in l2):
            l2.remove(letter)
        else:
            p = False
    if (p):
        w2.append(word)


print "Try these combinations - "
wordset = set(w2)
for w in wordset:
    print w
