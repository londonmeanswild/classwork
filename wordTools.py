#!/usr/bin/env python3
# (c) Landon A Marchant
"""A module of word manipulation tools. See guess.py for an example application.

Some parameter names violate the Python style guides. They are also not descriptive and in some cases very similar. https://www.python.org/dev/peps/pep-0008/#names-to-avoid 
    pydoc3 wordTools
"""

# When this module is imported with from wordTools import * 
# this list keeps track of all the symbols you want the importer to receive:
# __all__ = ['canon', 'chars', 'sized', 'words', 'within', 'rev', 'pal', 'isogram', 'isograms', 'match']

def canon(w):
    """Returns a canonical version of user input word:
    Args: #argument
    w: word to process.
    
    Raises:
    ValueError
    
    Returns: 
    String containing canonical version of the imput word. Lower cases, in alphabetical order, no spaces. 
    """
    
    w = w.lower()
    w = ''.join(sorted(w))
    w = w.strip()
    return input_word

def words(dfile='/usr/share/dict/words'):
    """Reads words from a dictionary, dfile. 
    Args:
        dfile: input file. default =/usr/share/dict/words
        
    Raises: 
        OSError
        
    Returns: 
        list of lines contained in input file. """
    # dfile does not close the file. Can I use the following:
    # open(dfile) as f: 
    # return [line.strip() for line in f] ? 
    # http://preshing.com/20110920/the-python-with-statement-by-example/
    
    return [line.strip() for line in open(dfile)]

def sized(l,n=4):
    """Returns elements of the list that are of specified length.
    Args:
        l: list of words 
        n: length of words to match. default = 4. 
    Returns:
        list containing all words in l of length n. """

    results = []
    for word in l:
        if len(word) == n:
            results.append(word)
    return results
    
def within(w,cs):
    """Returns true if and only if the letters of 'w' appear in the string of characters. 
    Args:
        cs: characters 
        w: word
    
    Returns:
        True/False result."""
    for character in w:
        if not character in cs:
            return False
    return True


def chars(l,cs = 'abcdefghijklmnopqrstuvwxyz'):
    """ Returns the words of a list 'l' whose letters all appear in 'cs'.
    Args: 
        l: list
        word: words of list whose letters appear in cs
        cs: selected characters
    
    Returns:
        words in list. """

    return [word for word in l if within(word,cs)]

def rev(s):
    """Function rev(s) that returns string s, reversed.
    
    Args: 
        s: string input
        new_s: new string
        
    Returns:
       reversed string."""

    new_s = []
    index = len(s)
    for i in range(len(s), 0, -1):
        new_s.append(s[i -1])
    return ''.join(new_s)

def pal(s):
    """ A Function pal(s) that returns True if a word s is a palindrome. 

    A palindrome is the same written backwards or forwards. e.g., 'racecar'
    
    Args: 
        s: string
    
    Return:
        True if s is palindrome. """

def pal(s):
    return (s == rev(s))

def isogram(w):
    """ Determine if a word is an isogram. 

    Args: 
        w: word
        
    Returns: 
        Word stripped to lowercase, characters are counted.
        False if word has repeating characters.
        True if word is an isogram. 
        Isograms have no repeating characters. 
        E.g., "Dab" is an isogram. "Dad" is not."""

    w = w.lower() #strip to lowercase
    for char in w: #for characters in word
        if w.count(char) > 1: #if word counts characters more than once
            return False
    return True

def isograms(l):
    """returns only words of list l that are isograms.
    
    Args:
        l: list 
        word: word in list
    
    Returns:
        iso_list: list of isograms."""

    iso_list = []
    for word in l:
        if isogram(word):
            iso_list.append(word)
    return iso_list

def match(a, b):
    """ Find characters in the same positions that match in equal length strings. 

    Args: 
        'a': first string to match
        'b': second string to match

    Raises: 
        ValueError if strings are different lengths. 

    Returns:
        A tuple of two integers. The first value is the number of characters that matach at the same position. The second is the number of characters that do not match. """

    if len(a) != len(b):
        raise ValueError
    bull = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            bull += 1
    return (bull, len(a)-bull)

"""Testing definitions and functions"""

if __name__ == "__main__":
    print(rev("BUUUUUUUULLL"))
    x = input("Testing isogram: ")
    print (isogram(x))
    s = input("Testing palindrome: ")
    print(pal(s))
    w = input("words comma separated: ")
    words = w.split(",")
    print(chars(words))
    
    
