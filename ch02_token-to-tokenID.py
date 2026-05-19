
#Build a vocab to map tokens to token IDs
#each word and special character is mapped to an integer
import re

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

#started using variable more inline with book example
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
prelen = (len(preprocessed))



#create a list of all unique tokens and sort them alphabetically
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)

print(prelen)
if prelen == 4690:
    print("preprocessed length matches book")
else: 
    print("prelen does not match book value")

print(vocab_size)
if vocab_size == 1130:
    print("Vocab_Size matches book")
else: 
    print("vocab size does not match book value")



#creating a vocabulary
vocab = {token:integer for integer,token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break