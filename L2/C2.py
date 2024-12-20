"""
The library heard how successful the username program was and have asked you to create 
one for coding all their books. 
The program should ask some simple questions and then output a code that is assigned to 
books to make them easier to find.
The convention for the book code is as follows:
[first 3 letters of the author][full year it was published][first 3 letters of the book title][-][first ketter of the genere]
"""

"""
This code include contents generated by a computer
"""

author = input("Enter the author's name: ")
year_published = input("Enter the year the book was published (e.g., 2024): ")
title = input("Enter the book's title: ")
genre = input("Enter the book's genre (e.g., fiction): ")

book_code = author[:3].upper() + year_published + title[:3].upper() + "-" + genre[0].upper()
print("Generated book code:", book_code)