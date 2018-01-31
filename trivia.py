#!/usr/bin/env python3
# (c) 2017 Landon A Marchant

"""
This file answers trivia questions about Williams faculty members.
Imports faculty API. Faculty API uses faculty.csv 

Questions Answered:
	q1. How many members are on the faculty at Williams?
	q2. How many members of the faculty hold a doctorate?
	q3. What faculty member(s) hold the oldest degrees?
	q4. How many members of the faculty received some degree 10 years ago, in 2007?
	q5. How many departments are there?
	q6. Which department has the most faculty?
	q7. What is the most popular type of master's degree?
	q8. What is the most popular undergraduate institution?
	q9. What school has granted the most degrees (all forms) to Williams faculty?
	q10. Who has the longest isogram last name? Ignore Jr.-like su xes, if necessary.

All functions call Args: 
						db. Parsed CSV from faculty.readDB()
"""
import faculty
db = faculty.readDB()

def q1(db):
    """Answers: How many faculty are there at Williams?
    	Args: 
    		db: parsed CSV file from faculty.read(DB)
    	Returns: 
    		faculty_count in int
    """
    faculty_count = len(db)
    print("Question 1: There are {} faculty.".format(faculty_count))

q1(db)
def q2(db):
	"""Answers: How many faculty hold a doctorate?
		Args: 
			db. Parsed CSV from faculty.readDB()
		Returns: 
			Count in integer. 
		"""
	count = 0
	for professor in db:
		if professor[5]:
			count +=1

	print("Question 2: {} members of the factory hold a doctorate degree.".format(count))
q2(db)	
def q3(db):
	"""Answers: What faculty member(s) hold the oldest degrees?
		Args: 
			db. Parsed CSV from faculty.readDB():
		Returns: 
			A formatted list of professor names. 
	"""

	oldest_professors = []
	oldest_degree = 9999  # Always in the future

	for professor in db:
		name = professor[0]  # first element from CSV. Professor name
		# find degrees for professor. 
		bachelor = professor[3] 
		masters = professor[4]
		doctorate = professor[5]
		degree_years = []

		# find years of each degree
		if bachelor:
			degree_years.append(bachelor[0])
		if masters:
			degree_years.append(masters[0])
		if doctorate:
			degree_years.append(doctorate[0])
			# Find oldest degree
			degree_years.sort()
			degree = degree_years[0]
			if degree < oldest_degree: 
				oldest_degree = degree
				oldest_professors = [name] #discard existing list of younger names
				if degree == oldest_degree: # if multiple graduates in same year
					oldest_professors.append(name)  # create list of multiple names
													# oldest professor is a list of lists. Convert to list of strings
	professor_names = []
	for professor in oldest_professors:
		professor_names = ' '.join(professor)  # turn these names into strings
		#professor_names.join(professor_names)  # list of strings from prof_name
	all_names = ''.join(professor_names)


	print("Question 3: The faculty member(s) with the oldest degrees are {}.".format(all_names))
	# this takes a list of names, creates one comma separated list of multiple names. Substitute in that format
q3(db)
def q4(db):
	"""Answers: How many members of the faculty received some degree 10 years ago, in 2007?
		
		Args: 
			db. Parsed CSV from faculty.readDB():
		
		Raises:
			save_count = False 
				Assumes the professor does not have a 2007 degree in order to prevent double counting

		Returns:
			Members of the faculty who received a degree in 2007. 
	"""
	count = 0 
	for professor in db:  # look at professor degrees
		bachelor = professor[3]
		masters = professor[4]
		doctorate = professor[5]
		save_count = False  # assume the professor does not have a 2007 degree

		if bachelor:
			year = bachelor[0]
			if year == 2007:
				save_count = True  # if degree was 2007, count
		if masters:
			year = masters[0]
			if year == 2007:
				save_count = True  # if degree was 2007, count
		if doctorate:
			year = doctorate[0]
			if year == 2007:
				save_count = True # if degree was 2007, count
		if save_count:  # 1 or more degrees from 2007. Count them. Prevents double-counting of professors.
			count +=1	
	print("Question 4: {} faculty members received a degree in 2007.".format(count))
q4(db)
def q5(db):
	"""Answers: How many departments are there?
		Args: 
			db. Parsed CSV from faculty.readDB():
		Returns:
			How many departments there are. Sorted to find greatest and unique. 
	"""
	departments = []
	for professors in db:
		departments.append(professors[2])
	departments.sort()
	unique_departments = len(faculty.uniq(departments))

	print("Question 5: There are {} unique departments at Williams College.".format(unique_departments)) 
q5(db)
def q6(db):
	""" Answers: Which department has the most faculty?
		Args: 
			db. Parsed CSV from faculty.readDB():
			uniqCount is a list containing original value and how many times it appears
		Returns:
			A string explaining which department has the most faculty. 

	"""
	departments = []
	for professor in db:
		departments.append(professor[2])
	departments.sort()
	size_departments = faculty.uniqCount(departments)

	largest_departments = []
	largest_size = 0
	for dept in size_departments:  # dept is academic departments. size_department is list of size of each
		dept_name = dept[0]
		dept_size = dept[1]
		if dept_size > largest_size:
			largest_size = dept_size # largest is current
			largest_departments = [dept_name]
		elif dept_size == largest_size:
			largest_departments.append(dept_name)  # largest departments, format this list to string
	
	#most_faculty = largest_departments.append(dept_name)
	print("Question 6: The {} department has the most faculty.".format(largest_departments[0]))
q6(db)

def q7(db):
	"""Answers: What is the most popular type of master's degree?
		Args: 
			db. Parsed CSV from faculty.readDB():
			Searches db by masters degrees

		Returns:
			the most popular type of master's degrees.
	"""
	master_types = []

	for professor in db:
		master = professor[4]
	if master: # year, type, school
			master_types.append(master[1])
			master_types.sort()
			master_counts = faculty.uniqCount(master_types) # [[type, count]]

	most_pop_degree = []
	most_pop_count = 0

	for degree in master_counts: 
		type_name = degree[0]
		type_size = degree[1]
		
		if type_size > most_pop_count:
			most_pop_count = type_size
			most_pop_type = [type_name]
		elif type_size == most_pop_count:
			most_pop_type.append(type_name)
			
	#most_masters = most_pop_type.append(type_name)

	print("Question 7: The most popular type of master's degree is {}.".format(most_pop_type[0]))
q7(db)

def q8(db):
	"""Answers: What is the most popular undergraduate institution?
		Args:
			db. Parsed CSV from faculty.readDB():

		Returns:
			the most popular undergraduate institution

	""" 
	undergraduate = []

	for professor in db:
		undergraduate_degree = professor[3]

		if undergraduate_degree:
			undergraduate.append(professor[3][-1])
		
	undergraduate.sort()
	faculty_undergraduate = faculty.uniqCount(undergraduate)

	most_popular = []
	largest_size = 0

	for institution in faculty_undergraduate:
		institution_name = institution[0]
		institution_number = institution[1]
		if institution_number > largest_size:
			largest_size = institution_number
			most_popular = [institution_name]
		elif institution_number == largest_size:
			most_popular.append(institution_name)
	#greatest_undergraduate_degrees = most_popular.append(institution_name)
	print("Question 8:{} is the most popular undergraduate institution.".format(most_popular[0]))
q8(db)
def q9(db):
	"""Answers:  What school has granted the most degrees (all forms) to Williams faculty?
		Args:
			db. Parsed CSV from faculty.readDB():

		Returns:
			A sorted string of the most common degree granting institution. 
	"""
	school = []

	for professor in db:
		bachelor = professor[3]
		masters = professor[4]
		doctorate = professor[5]

		if bachelor:
			school.append(bachelor[-1])
		if masters:
			school.append(masters[-1])
		if doctorate:
			school.append(doctorate[-1])
		
	school.sort()
	most_popular = faculty.uniqCount(school)


	most_pop_count = 0

	for institution in most_popular: 
		school_name = institution[0]
		school_size = institution[1]
		
		if school_size > most_pop_count:
			most_pop_count = school_size
			most_pop_school = [school_name]
		elif school_size == most_pop_count:
			most_pop_school.append(school_name)
	print("Question 9:{} is the most popular overall institution.".format(most_pop_school[0]))



q9(db)

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

def q10(db):
	"""Answers: Who has the longest isogram last name? Ignore Jr.-like su xes, if necessary.

		Args:
			db. Parsed CSV from faculty.readDB():

		Returns: 
			the longest isogram name(s) in the faculty database. 

		An isogram is a word that has no repeating letters.
	"""

longest_isogram_names = []
longest_isogram_len = 0
name_list = []
iso_list = []

for professor in db:
	name = professor[0]
	last_name = name[-1]
	last_name = last_name.split()
	last_name = last_name[0]

	name_list.append(last_name)

iso_list = isograms(name_list)

length = 0
longest_isograms = []

for name in iso_list:
	
	if len(name) > length:
		length = len(name)
		longest_isograms = [name]
	elif len(name) == length:
		longest_isograms.append(name)
	
print("Question 10: Professor {} and Professor {} have the longest isogram last names.".format(longest_isograms[0], longest_isograms[1]))

q10(db)






