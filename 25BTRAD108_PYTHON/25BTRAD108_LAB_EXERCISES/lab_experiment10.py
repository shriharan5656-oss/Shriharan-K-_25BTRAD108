# Frequency Counter Using Dictionaries

def count_word_frequency(sentence):
    # Convert sentence to lowercase and split into words
    words = sentence.lower().split()
    frequency_dict = {}
    
    for word in words:
        # Using .get() method to safely count occurrences
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
        
    return frequency_dict

# Test input sentence
sample_sentence = "Python programming is fun and programming in Python is powerful"

result = count_word_frequency(sample_sentence)

print("--- Word Frequency Counter ---")
print(f"Sentence: '{sample_sentence}'\n")
print("Word Frequencies:")
for word, count in result.items():
    print(f"'{word}': {count}")
