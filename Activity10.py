#Logical Operators

# and : &&
# or : !! 
# not : ! 

# Order of operators without parenthesis is

# not - 1st
# and - 2nd
# or - 3rd

a = 10
b = 8
c = 13


print(a > b or c < a)

print((a > b or c < a) and c==b)
print(not((a > b or c < a) and c==b))

# Use parenthesis for a much more cleaner code