#DAY 1: SYNTAX, VARIABLES, DATA TYPES, INPUT & OUTPUT, AND TYPE CONVERSION

"""
What is Python? 

Python is a general purpose programming language used for web development, data analysis, 
automation, AI, and scripting.

"""

#SYNTAX. 
#Rules to follow so that the Python code actuall works. 
#First, Python is case sensitive 
Name = "Imani"
name = "Kosuowei"
print(Name) #Imani
print (name) #Kosuowei
#Notice the variable contents change with the case sensitivity even though it has the same "Name"

#COMMENTS
#One pound for a single comment
"""
Triple quotes for multi-line comments
"""

#INDENTATION
#Python uses indentation to define blocks of code. These blocks of code work together and belong to the same structure.
if True: #starts the conditional block
    print("This is indented") #these two indented lines inside the block belong to the "if" block 
    print("Still in the block")
print("Outside the block")#non-indented line called the global scope and it runs no matter what because it is not under the if statement

#VARIABLES
#a variable is a label that stores data
# can not use spaces, symbols, or python words like "if" "for" "def"
count = 28 #integer whole number
item = "book of life" #string (text) always in quotes
price = 9.99 #float (decimal)
is_inventory = True #boolean (true or false)

#PRINTING OUTPUT
#Print is a function that tells Python to display something
print("Hello, world!") #shows the text inside quotations of the parenthesis
print(5)#prints the number inside parenthesis
print("I am", 28) #prints multiple items with the comma being used a seperator. That comma will be shown as a space when it is printed.
#printing multiple items example
item_name = "toy trucks"
count = 43
price = 10.59
print("We have", count, item_name, "in our inventory and they cost", price, "each." )
print (5+6) #will print the sum

#TAKING INPUT
#input always returns a string (text)
favorite_number = input("What is your favortie number?")
print(favorite_number)
#sometimes we may need to convert to an integer
#let's calculate the age of the user in 12 years
age = int(input("How old are you?")) #int is short for integer. it will change "their inputed age" into a number to be used for math
print(age + 11)

price_of_papaya = float(input("enter the price: ")) #will convert to a float aka a decimal
print(price)

#DATA TYPES
"""
"INT" = Integer: 9
"FLOAT" = Decimal: 8.99
"STR" = String: "hello"
"BOOL" = Boolean: "true or false"
"""
print("iloveww")






