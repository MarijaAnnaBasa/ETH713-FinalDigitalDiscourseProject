relative_path = "Corpus(we)1copy.txt"

with open(relative_path, mode="r", encoding="utf-8") as file:
    text = file.read() 

print("Number of characters in the text:", len(text))

import re

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s.,!?;:]', '', text)  
    text = re.sub(r'\s+', ' ', text).strip() 
    return text

with open(relative_path, mode="r", encoding="utf-8") as file:
    text = file.read()

lower_text = text.lower()  

cleaned_text = clean_text(lower_text)  

print(f"CLEANED Length of cleaned text: {len(cleaned_text)}")

words = cleaned_text.split() 
print(f"Number of words: {len(words)}")

from collections import Counter 
word_counts = Counter(words) 
N = 10
most_common_words = word_counts.most_common(N) 
for word, count in most_common_words:
    print(f"{word}: {count}")


sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s', cleaned_text)

we_sentences = [sentence.strip() for sentence in sentences if re.search(r'\bwe\b|\bwe\'[a-z]+', sentence)]

print("\nSentences containing 'we' as a pronoun:\n")
for i, sentence in enumerate(we_sentences, start=1):  
    print(f"{i}. {sentence}")

print(f"The number of sentences containing 'we' is: {len(we_sentences)}")


