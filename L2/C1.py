"""
The school would like a program that automatically creates usernames for students when 
they join year 7.
The program will ask some simple questions before generating the username and displaying 
it on the screen.
The username convention is below:
[surname][initial of firstname][last 2 digits of the year of birth]
"""

"""
This code include contents generated by a computer
"""

surname = input("Enter the student's surname: ")
first_name = input("Enter the student's first name: ")
year_of_birth = input("Enter the student's year of birth (e.g., 2017): ")

username = surname[0].upper() + first_name[0].upper() + year_of_birth[-2:]
print("Generated username:", username)