#DAY 2: OPERATORS, CONDITIONS, AND LOOPS

#OPERATORS 
#They are the building blocks of expressions and logic in python
#An expression is any combination of values, variables, operatprs, and function calls that Python can evaluate to a single value
"""
1. Arithmetic operators
They are used for basic math. 

+   Addition
-   Subtraction
*   Multiplication
/   Division  (always returns a float)
//  Floor Division (rounds down to the nearest whole number)
%   Remainder (Modulus only returns the remainder when 2 numbers are divided)
**  Exponentation
"""
print(8+15)
print(10-3)
print(4*8)
print(25/7)
print(25//7)
print(20%5)
print(3**4)

"""
2. Assignment Operators
They are used to reassign variables using operations for math/algebra to get a new value

=     means      x = 5     "Assign 5 to X. Or create a variable named x and give it the value 5" 
+=    means      x += 3    "X equals X+3. Or Take the current value of X and add 3"
-=    means      x -= 2    "X equals X-2. Or subtract 2 from the current value."
*=    means      x *= 2    "X equals X*2. Or multiply 2 by the original value"
/=    means      x /= 2    "X equal X/2. Or divide current value by 2"
//=   means      x //= 2   "X equals X/2. Or divide current value by 2 and round down"
%=    means      x %= 2    "X equals X/2. Or divide the current value by 2 and only keep the remainder
**=   means      x **= 2   "X equals X^2. Or raise the power of the current value to 2
"""

x = 5 
print(x)
x += 3 #Take 5 and add 3
print(x)

a = 3
a **=4 #Take 3 to the power of 4
print(a)

"""
3. Comparison Operators
They are used to compare two values and the result is always Boolean (True or False)

==     a == b     equal
!=     a != b     not equal to
>      a > b      a is greater than b
<      a < b      a is less than b
>=     a >= b     a is greater than or equal to b
<=     a <= b     a is less than b
"""

c = 10
d = 15
print(c==d)
print(c!=d)
print(c>d)
print(c<d)
print(c>=d)
print(c<=20)
print(d>=15)


