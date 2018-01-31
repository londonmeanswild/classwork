#!/usr/local/bin/python3
# A text-generating Oracle.
# (c) 2017 by Landon A Marchant
"""Oracle class generates 'readable' random text from a text file.

    Source file is tomsawyer.txt
"""
import random
from pprint import pprint

__all__ = ['Oracle']

class Oracle(object):
    """This doc string describes the class."""
    __slots__ = ["_window", "_distribution"]
    # _window: number of letters. Default specified in __init__
    # _distribution: How frequently certain letters appear

    def __init__(self, window=5):
        """Create an oracle with sliding window size with flat distribution.

        Args:
            window: how many letters at a time the oracle reads a text file.

         """
        self._window = window
        self._distribution = dict()

    def __str__(self):
        return "An oracle with window size {} & distribution based on {} strings.".format(
            self._window, len(self._distribution))

    def intern(self, string):
        """Incorporates substrings of string into the distribution.

        This iterates over the list string, and creates a dictionary containing the first two
        letters and the most common third. All strings are passed throughlower(), in case input
        text has uppercase.

        Args:
            string: the input corpus
        """

        for i in range(len(string) - self._window + 1):
            substring = string[i:i + self._window].lower()  # i is set to 0. sets to lower.
            front = substring[:-1]  # first half of the substring
            back = substring[-1]  # second half of the substring
            if front not in self._distribution:
                self._distribution[front] = dict() #  adding to dictionary
            if back not in self._distribution[front]:
                self._distribution[front][back] = 1  # initialize counter
            else:
                self._distribution[front][back] += 1  # if already in dict(), increment


    def follows(self, string):
        """ Returns random character likely to follow 'string' based on window_size.
        All strings are passed throughlower(), in case input text has uppercase.

            Args:
                string: character sequence of at least window_length - 1

            Returns:
                a character picked by random from the dictionary or None if no matching characters
                found
            """

        assert(len(string) >= self._window - 1), "Must be greater than window_size minus one"

        random_character = None
        string = string.lower()
        string = string[-(self._window - 1):]
        #TODO: Fix this so that it doens't need to create new lists each time
        if string in self._distribution:
            char_list = []
            # expand into list of characters so choice probability is based on frequency
            # iterate over keys to build char_list
            # self._distribution and elements contained are dicts()
            for subkey in self._distribution[string].keys():
                char_list.extend(subkey * self._distribution[string][subkey]) # extend adds to list

            random_character = random.choice(char_list)

        return random_character

    def generate(self, seed, output_length=80):
        """Produces a string by calling follows.

        All strings are passed throughlower(), in case seed text has uppercase.
        """
        seed = seed.lower()
        seed_length = len(seed)
        for _ in range(output_length): # does the next step 'number' times.
            seed = seed + self.follows(seed) # new seed is starting seed + one following
        return seed[seed_length:] # trims seed off string

def main():
    """ Creates an oracle instance, filename default is tomsawyer.txt
    """
    # o changed to oracle_reader
    oracle_reader = Oracle()
    text = ' '.join([line.strip() for line in open('tomsawyer.txt')])
    oracle_reader.intern(text)
    print(oracle_reader)

    output = ['fences']
    for i in range(25):
        new_line = oracle_reader.generate(output[-1])
        output.append(new_line)
        seed = new_line
    print('\n'.join(output))
    # TODO make fences part of the paragraph?

if __name__ == '__main__':
    main()
