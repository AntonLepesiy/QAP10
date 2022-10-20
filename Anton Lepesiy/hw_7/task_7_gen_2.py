# Необходимо составить список чисел которые указывают
# на длину слов в строке:
# sentence = " thequick brown fox jumps over the lazy dog",
# но только если слово не "the".


sentence = "the quick brown fox jumps over the lazy dog"

len_words = [len(i) for i in sentence.split() if i != 'the']
print(len_words)
