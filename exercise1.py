tasklist = [23,"Jane",["lesson 23",560,{"currency":"KES",}],987,(76,"John")]

#1.determine the type of variable in task list using an inbuilt function
a = print(type(tasklist))
#2. print KES-said
print(tasklist[2][2]["currency"])
#3. print 560- patricia
print(tasklist[2][1])
#4. length of task list
print(len(tasklist))

#5. rotate 987 to 789 using indexing only
z = tasklist [3]="789"
print (tasklist)
z = str(z)
#to rotate using indexing,we use as below
z = z[::-1]
print (z)


#6. change the name "John" to "jane"
#n/a. not applicable because its a tuple
