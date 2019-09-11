name = 'patricia wanjiku'
age = "56"
location = "Kenya"





person1 = [10.0,"patricia wanjiku", "kenya","56" ,True]
print (person1)

front_row_students = ["said","patricia","steve"]
#print(front_row_students)
#we use indexing to access various items
first = front_row_students[0:2]
#list slicing
#in indexing the integer at the left of the colon is normally the strarting point
#the integer on the right of the colon is normally the last list item but exclusive

#list operations
#concatenating
form1east = ["Howard"]
form1west = ["melvin"]
form1 = form1east + form1west
print(form1)
print(len(form1))
#determining membership in a list
is_melvin = "melvin" in form1
print(is_melvin)
print(first)

#assignment
form1.count("Howard")
form1.append()
form1. pop()
