# Usage: python get_sentiment_words.py [filepath]
# requires python3 

import json
import sys
import nltk
import pprint

NEGWORDS = "sentiment_wordlists/negative-words.txt"
POSWORDS = "sentiment_wordlists/positive-words.txt"

def load_words(path):
    with open(path, encoding='utf-8', errors='replace') as handle:
        words = handle.readlines()
    words = [w.strip() for w in words if w[0] != ';']
    words = [word for word in words if word]  # get rid of empty string
    return words

negwords = load_words(NEGWORDS)
poswords = load_words(POSWORDS)

def read_lowercase(filename):
    """ Read and lowercase the text of the source file """
    with open(filename) as debate:
        text = debate.readlines()  # doesn't scale, should do with generator
        text = [t.lower() for t in text] # lowercase it all
        alltext = ' '.join(text)
    return alltext

def get_chunks(filetext):
    """ Breaks up the file into chunks of size words """
    from nltk import tokenize
    filewords = tokenize.word_tokenize(filetext)
    return [filewords]

def get_overlap(list1, list2):
    from collections import Counter
    list1_multiset = Counter(list1)
    list2_multiset = Counter(list2)
    overlap = list((list1_multiset & list2_multiset).elements())
    totals = []
    for word in overlap:
        totals.append((word, list1_multiset[word]))
    return totals

def get_sentiment_counts(chunks, poswords=poswords, negwords=negwords):
    from collections import Counter
    counts = []
    for i, chunk in enumerate(chunks):
        overlap_pos = get_overlap(chunk, poswords)
        overlap_neg = get_overlap(chunk, negwords)
        counts.append({
                "positive total": sum(Counter(dict(overlap_pos)).values()),
                "positive words": list(overlap_pos),
                "negative total": sum(Counter(dict(overlap_neg)).values()),
                "negative words": list(overlap_neg),
                "word count": len(chunk)
            })
    for count in counts:
        count['net score'] = count['positive total'] - count['negative total']
    return counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python get_sentiment_words [filepath] ")
        return
    input_file = sys.argv[1]
    text = read_lowercase(input_file)
    chunks = get_chunks(text)
    jsonversion = get_sentiment_counts(chunks)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(jsonversion)

if __name__ == "__main__":
    main()

