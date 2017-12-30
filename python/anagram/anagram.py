import collections

def detect_anagrams(word, candidates):
    items = []

    for words in candidates:
        if(word.lower() != words.lower() and collections.Counter(word.lower()) == collections.Counter(words.lower())):
            items.append(words)

    return items
