#!/usr/bin/env python3
# (c) 2017 Landon Marchant
# STUDENTS: search for "pass" statements that require your attention.

"""
This module provides utilities for grabbing course descriptions from the
Williams College 16-17 course catalog website.
To run this, you must have the following installed:
   requests
   cython
   matplotlib
   wordcloud
"""
import re
import time
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# These are common words we avoid in the word cloud
stopwords = {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'can', 'for', 'from','how', 'in', 'is', 'it', 'of', 'on', 'that', 'the', 'this', 'to', 'will', 'with'}
def subjDict(subj="CSCI", term=1173):
    """Returns a dictionary of dictionaries describing courses in a subject during a term.
    Entries in the course dictionary include:
        'subj' - the course subject
        'number' - the course number
        'title' - the course title
        'cid' - the PeopleSoft ID for the course
        'term' - the PeopleSoft term ID
        'url' - the url of page containing course description.
    """
    # a regular expression for getting department course offerings:
    url = 'http://catalog.williams.edu/1617/catalog.php?strm={}&subj={}'.format(term, subj)

    # Grab the course page.
    # This loop is typical of what's needed to interact with the peoplesoft-generated pages
    # if there's an oracle error, back off and retry a second later.later
    while True:
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception('Invalid request')
        if r.text.find('Error:ORA') == -1:
            break  # removed ;
        time.sleep(1)

    # Find all the course entries on the departmental page, dropping courses into a dictionary
    t = r.text
    d = dict()
    # a regular expression for finding course links. cpat is course pattern
    cpat = '<a title="(.*)" href="(/1617/catalog.php\?&strm=([0-9]+)&subj=([A-Z]+)&cn=([0-9]+)&sctn=(.+)&crsid=([0-9]+))">.*?</a>'
    # each field below corresponds with () above
    for (title, url, trm, dept, course, sect, cid) in re.findall(cpat, t):
        course = int(course)
        trm = int(trm)
        url2 = 'http://catalog.williams.edu/1617/catalog.php?strm={}&crsid={}'.format(trm, cid)
        if course not in d:
            d[course] = {'subj':dept, 'number':course, 'title':title, 'cid':cid, 'url':url2, 'term':trm}
    if len(d) == 0:
        raise Exception('No courses found.  Bad subject ({}) or term ({})?'.format(subj, term))
    return d

def courseDescr(subj='CSCI', term=1173, number=135, subjdict=None):
    """Return the course description.
        Description is ssociated with a course number (number) in a subject (subj)
        during a particular semester (term). Makes use
        of pre-computed subject course dictionary (subjdict) if present."""
    if subjdict is None:
        subjdict = subjDict(subj, term)
    if not subjdict:
        raise Exception('Invalid subject ({}) or term ({}).'.format(subj, term))
    if number not in subjdict:
        raise Exception('No such course: {} {}'.format(subj, number))
    courseURL = subjdict[number]['url']
    while True:
        r = requests.get(courseURL)
        if r.status_code != 200:
            raise Exception('Invalid request')
        if r.text.find('Error:ORA') == -1:
            break  # removed ;
        time.sleep(1)
    t = r.text
    cdpat = '<div class="catalogdesc">(.*?)</div>'
    for description in re.findall(cdpat, t):
        return description
        # with open("description.txt", "w") as text_file:
         #   text_file.write("description {}, {}, {}".format(subj, term, description))

#def cloudify():
def cloudify(subj='CSCI', term=1173, number=135):
    """Generate word cloud associated with a subject (subj) during a term (term).
    Writes output to <subj>Cloud.png. (e.g. csciCloud.png)"""
    text = courseDescr(subj=subj, term=term, number=number)
    # text = courseDescr('description.txt')
    text = open(path.join(d, 'description.txt.')).read()

# generate a WordCloud object from text not including stopwords
    wordcloud = WordCloud(width=1000, height=800,stopwords=stopwords)
    wordcloud.generate(text)
# use matplotlib.pyplot to save the image
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig('{}.png'.format(subj))

"""
Only used in lab:
def missionCloud():
    #Write a word cloud based on the College mission statement.
    text = courseDescr('mission.txt')
    # generate a WordCloud object from text not including stopwords
    wordcloud = WordCloud(width=1000, height=800,stopwords = stopwords)
    wordcloud.generate(text)
    # use matplotlib.pyplot to save the image
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig('mission.png')
"""

if __name__ == "__main__":
    from sys import argv
    #missionCloud()
    print(courseDescr(subj='CSCI', term=1173, number=135))