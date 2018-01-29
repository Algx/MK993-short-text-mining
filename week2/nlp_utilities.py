
import nltk
from nltk.corpus import stopwords
import re
import string


PUNCTUATION = string.punctuation
STOPS = stopwords.words('english')

def remove_punct(wordlist):
    return [word for word in wordlist if word not in PUNCTUATION]


def remove_stops(wordlist):
    # takes a list of words and filters out stopwords after lowercasing
    lowercase = [word.lower() for word in wordlist]
    return [word for word in lowercase if word not in STOPS]


def remove_nonletters(wordlist):
    """ Checks for letters in the token - using a regex search.
    Strings that are just numbers or remaining punctuation will
    be removed! No more custom '--'. But ''s' will remain.
    """
    return [word for word in wordlist if re.search('[a-zA-Z]', word)]


def clean_tokens(tokens):
    """ Takes a list of tokens. Returns lowercased, minus punct
    and stopwords and digits.
    """
    words = remove_punct(tokens)
    words = remove_stops(words)
    words = remove_nonletters(words)
    return words


def stem_tokens(tokens):
    from nltk.stem.porter import PorterStemmer
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in tokens]


def print_counts(tokens, count=10):
    # Takes a list of words, counts, prints top "count" words.
    from collections import Counter
    mycounts = Counter(tokens)
    print("Word\tCount")
    for word,count in mycounts.most_common(count):
        print("%s\t%s" % (word,count))


def tokenize_text(path):
    # This takes a file path and word_tokenizes it, returning a list of words.
    words = None
    try:
        with open(path, encoding="utf8", errors="ignore") as handle:
            text = handle.read()
            text = text.replace("\n", " ")
            words = nltk.word_tokenize(text)
            return words
    except:
        return None


def tokenize_clean_stem(text):
    # takes an already read text and tokenizes stems and clean
    tokens = nltk.word_tokenize(text)
    tokens = clean_tokens(tokens)
    tokens = stem_tokens(tokens)
    return tokens


def tokenize_clean(text):
    # takes an already read text and tokenizes stems and clean
    tokens = nltk.word_tokenize(text)
    tokens = clean_tokens(tokens)
    return tokens


def remove_custom(wordlist, mylist):
    return [word for word in wordlist if word not in mylist]


def count_sentences(text):
    # Takes a full text, not tokens - because it tokenizes them.
    # Returns the count only
    return len(nltk.sent_tokenize(text))


def get_filenames(folder):
    # returns all the filenames in the folder.
    from os import listdir
    from os.path import isfile, join
    # because we want to return full paths, we need to make sure there is
    # a / at the end.
    # If this doesn't work on Windows, change the slash direction.
    if not folder.endswith("/"):
        folder = folder + "/"
    # this will return only the filenames, not folders inside the path
    return [folder + f for f in listdir(folder) if isfile(join(folder, f)) and f != ".DS_Store"]


def load_texts_as_string(filenames):
    """ Input is a list, output is a dict with filenames as keys """
    from collections import defaultdict
    loaded_text = defaultdict(str)  # each value is a string, the text
    for filename in filenames:
        with open(filename, errors="ignore") as handle:
            loaded_text[filename] = handle.read()
    return loaded_text

