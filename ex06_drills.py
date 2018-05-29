# ex06: String and text

# define a variable call types_of_people, build a string based on the varibale
types_of_people = 10 
x = f"There are {types_of_people} types of people."

# build a string based on two string
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

# example shows how to use string.format()
hilarious = False
joke_evaluation = "Isn't that joke so funny ?!{}"

print(joke_evaluation.format(hilarious))

# + as concatenation
w = "this is the left side of..."
e = "a string with a right side."

print(w + e)
