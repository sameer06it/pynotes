# Define a function that takes a word as an argument, returns a list of
# truth values i.e., True for a vowel in the word, False for a non-vowel.

def find_vowels(word):
    """ Return a list containing a True for a vowel in the word,
        a False for a non-vowel.
    
    >>> find_vowels('detestable')
    >>> [False, True, False, True, False, False, True, False, False, True]
    """

    # your code here
def find_vowels(word):
    # word= raw_input('enter a word:')
    list = ['a','i','e','o','u']
    for i in word:
        if i not in list:
            print False
        else:
            print True

find_vowels(word='sameer')
