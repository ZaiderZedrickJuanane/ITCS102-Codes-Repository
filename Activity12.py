#Importing excluded commands
import getpass

#Conditional Statement / Selection Statement

# FORMAT
# if [condition] :


#ex

user = "admin"
password = "admin123"

u = input("Please enter your username -----> ")
p = getpass.getpass("Please enter your password -----> ")




if user == u and password == p :
	print("ACCESS GRANTED")
else :
	print("ACCESS DENIED, PLEASE TRY AGAIN")
	