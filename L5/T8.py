"""
Temperature
This code include contents generated by a computer
"""

temperature = float(input("What's the temperature? "))
if temperature < 0 or temperature > 34:
    print("Not a habitable temperature")
elif 0 <= temperature <= 5:
    print("Its Freezing!")
elif 6 <= temperature <= 10:
    print("Pretty Chilly!")
elif 11 <= temperature <= 12:
    print("Could be warmer")
elif 13 <= temperature <= 20:
    print("It is bearable")
elif 21 <= temperature <= 25:
    print("Is this summer?")
elif 26 <= temperature <= 31:
    print("Where is the suntan oil?")
else:
    print("Tropical and lazy")