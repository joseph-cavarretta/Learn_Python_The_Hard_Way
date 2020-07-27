# Exercise 6 "Strings and text"

types_of_ppl = 10
x = f"there are {types_of_ppl} types of people"

binary = "binary"
do_not = "don't"

y = f"those who know {binary} and those who {do_not}"

print (x)
print (y)

print (f"I said: {x}")
print (f"I also said: '{y}'")

hilarious = False

joke_evaluation = "Isnt't that joke so funny?! {}"

print (joke_evaluation.format(hilarious))

w = "This is the left side of .."
e = "a string with a right side."

print (w + e)
