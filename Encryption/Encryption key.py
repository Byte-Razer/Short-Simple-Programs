abc="abcdefghijklmnopqrstuvwxyz"
word=input("Enter word u want to encrypt and send:")
key= int(input("Enter value by which u want to encrypt the text. "))  #:)
encrypted_word=""
for letter in (word):
    i=abc.index(letter)
    newi=i+key
    encrypted_word= encrypted_word +abc[newi]
print(encrypted_word)
