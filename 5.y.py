poem = ['wibble', 'wobble', 'wibble', 'wobble', 'jelly', 'on', 'the', 'plate']

search = input()
num = int(input())

index = poem.index(search)

words = poem[index + 1 : index + 1 + num] 
print (" ".join(words))
