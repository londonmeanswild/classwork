#!/usr/bin/env python3
# (c) 2017 Landon A Marchant
# Find five letter palindromes

import re
pat = '^(.)(.).\\2\\1$'


d = open('/usr/share/dict/words')

for line in d:
    word = line.strip()
    if re.match(pat, word):
        print(word)
