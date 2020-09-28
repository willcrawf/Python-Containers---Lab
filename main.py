## Question 1 ##
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.
names = ['Will Crawford', 'Semore Johnson', 'Reed Voeks', 'Olivia Balkcum', 'Jackson Brown']
print('Question 1:')
print(f'Second name in list: {names[1]}')
print(f'Last name in list: {names[-1]}')
print('')

## Question 2 ##
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".
foods = ['Pie', 'Melons', 'Rice', 'Stromboli', 'Pizza']
print('Question 2:')
for food in foods:
  print(f'{food} is a good food')
print('')

## Question 3 ##
# Last two foods from foods list
print('Question 3:')
print('Last two items:')
for x in range(-2, 0):
  print(foods[x])
print('')

## Question 4 ##
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"
print('Question 4:')
home_town = {
  'city': 'Charleston',
  'state': 'SC',
  'population': '130,000'
}
print('I was born in ' + home_town['city']+', '+home_town['state']+ ' which has a population of ' + home_town['population']+'.')
print('')

## Question 5 ##
#Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"
print('Question 5:')
for key, item in home_town.items():
  print(f'{key} = {item}')
print('')

## Question 6 ##
print('Question 6:')
cohort = [
]
counter = -1
for name in names:
  counter += 1
  cohort.append({'Name': name, 'Favorite food' : foods[counter]})
  print('Name: ' + name)
  print('Favorite Food: ' + foods[counter])
  print('')
print('')

## Question 7 ##
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.
print('Question 7:')
awesome_students = []
for name in names:
  awesome_students.append(f'{name} is an awesome student!')

for student in awesome_students:
  print(student)
print('')
## Question 8 ##
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.
print('Question 8:')
x = -1
for name in names:
  x += 1
  if "a" in name:
    print(name)
  if "a" in foods[x]:
    print(foods[x])
