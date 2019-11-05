# Variables
# data types: string, numbers
# \n = newLine, \" = qoutation mark
# character_name = "Tom" #string
# character_age = "50" #string
# character_ageNum = 50.5678213 #number
# isMale = True #boolean True or False
# phrase = "Giraffe Academy"

# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old. ")
# character_name = "Mike"
# print("He really liked the name " + character_name + ", ")
# print("but didn't like being " + character_age + ".")

# print(phrase + " is cool")
# print(phrase.lower()) #converts to lowercase
# print(phrase.upper()) #converts to uppercase
# print(phrase.isupper()) #true if entirely uppercase, false if not
# print(phrase.upper().isupper()) #returns true b/c isTrue
# print(len(phrase)) #returns length num of characters in string
# print(phrase[0]) #returns first character of string, 0 index
# print(phrase.index("Acad")) #returns first instance of index begins
# print(phrase.replace("Giraffe", "Elephant")) #replaces old_str with new_str

##### MATH #####
################
# print(-2.897)
# print(3 + 4.5) #addition
# print(3 - 4.5) #subtraction
# print(3 * 4.5) #multiplication
# print(10 % 3) #modulus, take 10 and divide it by 3 - return the remainder
# print(3 * (4 + 5)) #order of operations
# my_num = -5
# print(str(my_num) + " is my favorite number") #including numbers with strings
# print(abs(my_num)) #return absolute value of number
# print(pow(3, 2)) #3 to the power of 2
# print(max(4, 6)) #returns highest number
# print(min(4, 6)) #returns smallest number
# print(round(3.2)) #rounds number

##### IMPORT #####
##################
# from math import * #gives access to more math functions
# print(floor(3.7)) #rounds number down
# print(ceil(3.7)) #rounds number up
# print(sqrt(36)) #returns square root of number

##### INPUT #####
#################
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

##### CALCULATOR #####
######################
# num1 = input("Enter a number: ") #by default python converts input to a string
# num2 = input("Enter another number: ") #by default python converts input to a string
# result = float(num1) + float(num2) #int() can only work with whole numbers, float() is a decimal number4
# print(result)

##### MAD LIBS GAME #####
#########################
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

##### LISTS #####
#################
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"] #use [] to create array of values
# print(friends) #prints array
# print(friends[1]) #print index 1 of friends array, can use negatives to index from back of list
# print(friends[1:3]) #prints values at index 1 to index 3
# print(friends[1:]) #prints values at index 1 and after
# friends[1] = "Mike"
# print(friends[1])
# lucky_numbers = [4, 16, 8, 15, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
# print(friends)
# print(lucky_numbers)
# friends.extend(lucky_numbers) #extend values onto a list
# print(friends)
# friends.append("Creed") #adds value to end of list
# print(friends)
# friends.insert(1, "Kelly") #inserts value at index in list
# print(friends)
# friends.remove("Jim") #removes value from list
# print(friends)
# friends.clear() #removes all elements in list
# friends.pop() #removes last element in list
# print(friends)
# print(friends.index("Oscar")) #find index of value in list
# print(friends.count("Jim")) #count number of values in list
# friends.sort() #sort string list in ascending order
# print(friends)
# lucky_numbers.sort() #sorts number list in ascending order
# print(lucky_numbers)
# lucky_numbers.reverse() #sorts number list in reverse order
# friends2 = friends.copy() #copy list into new list
# print(friends2)

##### TUPLES #####
##################
#coordinates = (4, 5)  # tuples are inmutable - cannot be changed
#print(coordinates[0])  # index start at 0
#coordinates = [(4, 5), (6, 7), (80, 34)]  # array of tuples
#print(coordinates)
#print(coordinates[2])


##### FUNCTIONS #####
#####################
#def say_hi(name, age):  # define function with name sayhi, everything after : is the function
#    print("Hello " + name + ". My age is " + str(age))


#print("Top")
#say_hi("Mike", 35)  # executes function
#say_hi("Steve", 75)
#print("Bottom")


#def cube(num):
#    return num * num * num  # return value, cannot put code after return statement

#result = cube(14)  # stores value returned from 14*14*14
#print(result)

##### IF STATEMENT #####
########################
#is_male = False
#is_tall = True

#if is_male and is_tall:
#    print("You are male and tall")
#elif is_male and not(is_tall): #not(is_tall) returns opposite of value. If value is True, not() checks if False
#    print("You are male and short")
#elif not(is_male) and is_tall:
#    print("You are not a male but are tall")
#else:
#    print("You are neither male nor tall")


##### COMPARISONS #####
#######################
# >, >=, <, <=, ==, !=
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
#print(max_num(15,50,5)) #prints out 50 (num2) as max_num


##### CALCULATOR #####
######################
#num1 = float(input("Enter first number: "))
#op = input("Enter operator: ")
#num2 = float(input("Enter first number: "))

#if op == "+":
#    print(num1 + num2)
#elif op == "-":
#    print(num1 - num2)
#elif op == "/":
#    print(num1 / num2)
#elif op == "*":
#    print(num1 * num2)
#else:
#    print("Invalid operator")


##### DICTIONARIES #####
########################
# Jan -> January
# Mar - > March
#monthConversions = {
#    "Jan": "January",
#    "Feb": "February",
#    "Mar": "March",
#    "Apr": "April",
#    "May": "May",
#    "Jun": "June",
#    "Jul": "July",
#    "Aug": "August",
#    "Sept": "September",
#    "Oct": "October",
#    "Nov": "November",
#    "Dec": "December",
#}

#print(monthConversions["Apr"]) #returns April
#print(monthConversions.get("Dec")) #returns December
#print(monthConversions.get("Luv")) #invalid key, returns None
#print(monthConversions.get("Luv", "Not a valid Key")) #invalid key, returns Not a valid Key


##### WHILE LOOP #####
######################
#i = 1
#while condition / loop guard
#while i <= 10:
#    print("Number is: ", i)
#    i += 1 # same as i++ or i = i + 1

#print("Done with loop")


##### GUESSING GAME #####
#########################
#secret_word = "giraffe"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False

#while guess != secret_word and not(out_of_guesses):
#    if guess_count < guess_limit:
#        guess = input("Enter secret word: ")
#        guess_count += 1
#    else:
#        out_of_guesses = True

#if out_of_guesses:
#    print("Out of Guesses, YOU LOSE!")
#else:
#    print("You win!")


##### FOR LOOP #####
####################
#friends = ["Jim", "Karen", "Kevin"]

#for name in friends:
#    print(name)

#for letter in "ABCD":
#    print(letter)

#for index in range(10):
#    print(index)

#for index in range(3, 10):
    #    print(index)

#for index in range(len(friends)):
#    print(friends[index])

#for index in range(5):
#   if index == 0:
        #print("first Iteration")
    #else:
        #print("Not first")

#def raise_to_power(base_num, pow_num):
#    result = 1
#    for index in range(pow_num):
#        result = result * base_num
#    return result

#print(raise_to_power(2, 3))


##### 2D LISTS & NESTED LOOPS #####
###################################
#number_grid = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#    [0]
#]

#print(number_grid[0][1]) #number_grid[row number][column number]
#print(number_grid[2][2])

#for row in number_grid:
#    for col in row:
#        print(col)


##### BUILD A TRANSLATOR #####
##############################
#def translate(phrase):
#    translation = ""
#    for letter in phrase:
#        if letter.lower() in "aeiou":
#            if letter.isupper():
#                translation = translation + "G"
#            else:
#                translation = translation + "g"
#        else:
#            translation = translation + letter
#    return translation

#print(translate(input("Enter a phrase: ")))


##### COMMENTS #####
####################
'''
multiline
comments
'''
# single line comments


##### CATCHING ERRORS & EXCEPTIONS #####
#try:
#    answer = 10/0
#    number = int(input("Enter a number: "))
#    print(number)
#except ZeroDivisionError as err:
#    print(err)
#except ValueError:
#    print("Invalid Input")
'''
Traceback (most recent call last):
  File "C:/Users/Hunter/PycharmProjects/Giraffe/app.py", line 313, in <module>
    number = int(input("Enter a number: "))
ValueError: invalid literal for int() with base 10: 'a'
'''


##### READING FILES #####
#########################
# "r" = read, "w" = write, "a" = append, "r+" = read/write
# always close file after opening file
#employee_file = open("employees.txt", "r")

#print(employee_file.readable()) #returns boolean if file is readable
#print(employee_file.readline()) #reads first line
#print(employee_file.readline()) #reads second line

#for employee in employee_file.readlines():
#    print(employee) #puts all lines from file into array

#employee_file.close() #close file when done


##### WRITING TO FILES #####
############################
#employee_file = open("index.html", "w")
#employee_file.write("\n" + "<p>This is HTML</p>")
#employee_file.close()


##### MODULES & PIPS #####
##########################
#import useful_tools #useful_tools.py
#print(useful_tools.roll_dice(10))

# pip install python-docx
# pip uninstall python-docx
# located in site-packages folder


##### CLASSES & OBJECTS #####
#############################
# create data types
#from Student import Student #from Student.py import Student class

#student1 = Student("Jim", "Business", 3.1, False)
#student2 = Student("Pam", "Art", 2.5, True)

#print(student2.major)


##### MULTIPLE CHOICE QUIZ #####
################################
'''
from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer  == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
'''

##### OBJECT FUNCTIONS #####
############################
#from Student import Student
#student1 = Student("Oscar", "Accounting", 3.1)
#student2 = Student("Phyllis", "Business", 3.8)

#print(student2.on_honor_roll())


##### INHERITANCE #####
#######################
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()


##### PYTHON INTERPRETER #####
##############################
#Command Prompt > cd C:\ > python