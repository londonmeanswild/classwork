#!/usr/bin/env python3
# (c) 2017 Landon A Marchant

"""
This collection of utilities is useful for manipulating a faculty database,
stored in CSV format.  

We thank the Dean of Faculty's office for providing this information.
The fields of this database are:
  0: Member's name.  e.g. "Nolan Jr., James L."
  1: Member's title. e.g. "Professor of Sociology"
  2: Member's department. e.g. "Anthropology and Sociology"
  3: Member's bachelor's degree: year, degree, granting institution.
     e.g. "1984, B.A., University of California, Davis"
  4. Member's master's degree.
  5. Member's doctorate degree.
Missing degrees are represented by empty strings.

When the database is loaded, it is represented as a list of
member lists.  Each member list describes the faculty member, with the
following items:
  0. Member's name: ['James', 'L.', 'Nolan Jr.']
  1: Member's title: "Professor of Sociology"
  2: Member's department: "Anthropology and Sociology"
  3: Bachelor's degree: [1984, 'B.A.', 'University of California, Davis']
  4. Master's degree: similar to Bachelor's.
  5. Doctorate doctorate degree: similar to Bachelor's.
"""
import csv
__all__ = [ 'readDB', 'uniq', 'uniqCount', 'parseMember']

def parseDegree(d):
    """Given a comma-separated degree, converts it to a 3-element list.
       
    Args:
        d: string containing comma separated details about a degree.
        Year, Type, School

    Returns:
        List containing parsed details. Empty list ([]) if degree is empty.

    Assumes all faculty have at least one first and one last name."""

    if not d:  #if no degree, short-circuit to return empty list
      return []  # return the empty list
    degree = d.split(',', 2)  # split degree on comma, max of 3 elements
    degree [0] = int(degree[0])  # year is converted to int from string
    return degree

def parseName(n):
    """Given a comma-separated name, converts it to a 3-element list of names. 
      Last element is last name, which possibly contains spaces and suffices. 

      Args:
        n: Comma separated string of "last name, first [middle]". Middle name is optional.
        Middle name is optional.  

      Returns:
        List of two or more elements. "First name, [middle], last". 
        Index 0 is first name
        Index 1 could be first or middle
        Index 2, if it exists, is always last. 
      """
    names = n.split(',',1)
    last_name = names[0] #last name is the first index
    first_middle = names[1]
    first_middle = first_middle.split(maxsplit=1) #split into a list of first and optional middle 
    full_name = first_middle + [last_name]
    return(full_name)

def parseMember(l):
    """Converts a CSV row into a member list, as described above.

    Args: 
      l: List or CSV row elements

    Returns: 
      List of parsed member details. 
        0: List. 2 or 3 names, first [middle] last.
        1: String. Title. 
        2: String. Department. 
        3: List. Bachelor degree. Year, Type, School.
        4. List. Masters degree. Year, Type, School.
        5: List. Doctorate degree. Year, Type, School. 

    """
    first_name_last_name = parseName(l[0])
    title = l[1]
    department = l[2]
    bachelor_degree = parseDegree(l[3])
    master_degree = parseDegree(l[4])
    doctorate_degree = parseDegree(l[5])

    return [first_name_last_name,title, department, bachelor_degree, master_degree, doctorate_degree]

def readDB(database='faculty.csv'):
    """Reads data from a CSV database (in Dean of Faculty-specified format)
       and returns a list of member descriptions.
    
    """
    results = []
    import csv

    with open(database, 'r', newline='') as f:  # r means read only
        csvf = csv.reader(f)
        for row in csvf:
            professor = parseMember(row)  # professor = parsed value of row
            results.append(professor)  # saved to results list
    return results



def uniq(l):  
    """Returns a copy of list l with adjacent duplicate values removed.
      Args:
        l: list. 
           uniq([1,1,2,-3,-3,-3,1,2])
      Returns: 
        returns [1,2,-3,1,2]

      l does not contain None values
    """

    result = []
    counts = uniqCount(l)  # use uniqCount rather than parsing list again
    for i in counts:  # i is value, count
      result.append(i[0])  # only saved value from i, did not save count
    return result

def uniqCount(l):
    """Like uniq, removes duplicate non-None values.
       Unlike uniq, each result entry is a list containing the original value
       and its count.

       For example:
          uniqCount([1,1,2,-3,-3,-3,1,2])
          returns [[1,2], [2,1], [-3,3], [1,1], [2,1]]
    """
    lastItem = None
    result = []
    for value in l:
        if value != lastItem:
          result.append([value, 1]) 
          lastItem = value
        else:
          result[-1][1] += 1 
    return result 
    pass


# The suite associated with this if is only executed if faculty.py is 
# directly interpreted by python.  It is not executed during import.
if __name__ == '__main__':
  from doctest import testmod
  testmod()
  db = readDB()
  # readDB() tests parseMember 
  # parseMember tests parseName, parseDegree
  
  print(uniq([3, 4, 5, 6, 2, 2, 2, 3, 4, 6]))


