"""
Check membership
"""

import re

def checkLuhn(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
        if (isSecond == True):
            d = d * 2
        nSum += d // 10
        nSum += d % 10
        isSecond = not isSecond
    if (nSum % 10 == 0):
        return True
    else:
        return False

dsi_rooms = {
    "single": [8, 60],
    "double": [10, 75],
    "suite": [2, 105]
}

dsi_addon = {
    "parking": 20,
    "breakfast": 12,
    "p+b": 25,
    "member_breakfast": 1,
    "member_parking": 0.5
}

elite_free_night_threshold = 5

print("Welcome to Diddly Squat Inn!")
for k, v in dsi_rooms.items():
    room_type = k
    room_available = v[0]
    room_price = v[1]
    print("We have ", room_available, room_type, " available at the cost of £", room_price, " each.")

reservation_room = input("Which room do you want? ").lower()
while reservation_room not in dsi_rooms.keys():
    print("Input not recognised. Please try again.")
    reservation_room = input("Which room do you want? ").lower()
reservation_rate = float(dsi_rooms.get(reservation_room)[1])

reservation_nights = input("How many nights do you want to stay in the room? ")
while not reservation_nights.isnumeric():
    print("Input not recognised. Please try again.")
    reservation_nights = input("How many nights do you want to stay in the room? ")

while int(reservation_nights)<1:
    print("Input not recognised. Please try again.")
    reservation_nights = input("How many nights do you want to stay in the room? ")
reservation_nights = int(reservation_nights)

print("Do you want to add parking? Parking is £", dsi_addon.get("parking"), " extra per day.")
reservation_parking = input("Enter Y or N ")
while not(reservation_parking == "Y" or reservation_parking == "N"):
    print("Input not recognised. Please try again.")
    reservation_parking = input("Do you want to add parking? Enter Y or N ")
if reservation_parking == "Y":
    reservation_parking = True
else:
    reservation_parking = False

print("Do you want to add breakfast? Breakfast is £", dsi_addon.get("breakfast"), " extra per day regardless of number of guests.")
reservation_breakfast = input("Enter Y or N ")
while not(reservation_breakfast == "Y" or reservation_breakfast == "N"):
    print("Input not recognised. Please try again.")
    reservation_breakfast = input("Do you want to add breakfast? Enter Y or N ")
if reservation_breakfast == "Y":
    reservation_breakfast = True
else:
    reservation_breakfast = False

membership = input("Are you a member with us? Enter Y or N ")
while not(membership == "Y" or membership == "N"):
    print("Input not recognised. Please try again.")
    membership = input("Are you a member with us? Enter Y or N ")

breakfast_rate = 1
parking_rate = 1

if membership == "Y":
    breakfast_rate = breakfast_rate - dsi_addon.get("member_breakfast")
    parking_rate = parking_rate - dsi_addon.get("member_parking")
    membership_status = input("What's your membership status? Enter Basic or Elite. ").lower()
    while not (membership_status == "basic" or membership_status == "elite"):
        print("Input not recognised. Please try again.")
        membership_status = input("What's your membership status? Enter Basic or Elite. ").lower()
    if membership_status == "elite":
        free_nights = reservation_nights // elite_free_night_threshold
        reservation_nights = reservation_nights - free_nights

if reservation_parking:
    if reservation_breakfast:
        reservation_rate = reservation_rate + min(dsi_addon.get("p+b"), dsi_addon.get("parking") * parking_rate + dsi_addon.get("breakfast") * breakfast_rate)
    else:
        reservation_rate = reservation_rate + dsi_addon.get("parking") * parking_rate
else:
    if reservation_breakfast:
        reservation_rate = reservation_rate + dsi_addon.get("breakfast") * breakfast_rate

reservation_price = reservation_rate * reservation_nights
print("That would be £", reservation_price)

reservation_name = input("What's your name? ")
reservation_card = input("What's your card number? ")
while not checkLuhn(reservation_card):
    print("Card number invalid. Please try again.")
    reservation_card = input("What's your card number? ")

reservation_email = input("What's your email address? ")
while not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', reservation_email):
    print("Email address invalid. Please try again.")
    reservation_email = input("What's your email address? ")

print("Thank you for your reservation!")