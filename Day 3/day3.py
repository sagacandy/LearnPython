text=(input("Enter text:"))
# random=input("Enter 3 random letters: ")

word=text.split()         #splits a string into a list
wordcount=len(word)       #count number of items in list

print(wordcount)

#Find the first and last letter of sentence
first=text[0]
last=text[-1]
print(f"Entered firt word is {first} and last word is {last}")

inverted=reversed(text)

print(text[::-1])