#Dont change these codes
print("Welcome to the DSC Love Calculaor")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Your code goes below
#NAME TRUE TEST
name_chk = 0
name_str = name1+name2            #combine both names
name_str = name_str.lower()       #make comined name string into lower case.
name_chk += name_str.count("t")   #count in comined name string for "t"
name_chk += name_str.count("r")   #count in comined name string for "r"
name_chk += name_str.count("u")   #count in comined name string for "u"
name_chk += name_str.count("e")   #count in comined name string for "e"
score = name_chk                 #add to final score

#ZODIC
import find_my_zodiac
zodiac_rqst = input("Do you want to also find your match in the stars?(Y or N): ") or 'n'

if (zodiac_rqst == 'y'):
    date_day1 = 0
    while 1 > date_day1 or 31 < date_day1: #check if day is between 1 - 31
        try:
            date_day1 = int(input("Day of your birth: "))
        except ValueError:
            date_day1 = int(input("Day of your birth: 1 to 31"))
    date_month1 = 0
    while 1 > date_month1 or 12 < date_month1: #check if month is between 1 - 12
        try:
            date_month1 = int(input("Month of your birth (digits): "))
        except ValueError:
            date_month1 = int(input("Month of your birth 1 to 12: "))
    date_day2 = 0
    while 1 > date_day2 or 31 < date_day2: #check if day is between 1 - 31
        try:
            date_day2 = int(input("Day of your birth: "))
        except ValueError:
            date_day2 = int(input("Day of your birth: 1 to 31"))
    date_month2 = 0
    while 1 > date_month2 or 12 < date_month2: #check if month is between 1 - 12
        try:
            date_month2 = int(input("Month of their birth (digits): "))
        except ValueError:
            date_month2 = int(input("Month of their birth 1 to 12: "))

    zodiac_sign1 = find_my_zodiac.zodiac_chk(date_month1, date_day1) #find zodiac for date 1
    zodiac_sign2 = find_my_zodiac.zodiac_chk(date_month2, date_day2)#find zodiac for date 2

    print(zodiac_sign1)
    print(zodiac_sign2)

#EYE COLOR

#HAIR COLOR

#AGE DIFFERENCE



#SCORE OUTPUT (please verify)
if score < 10: #0-9
    print("You go together like coke and mint.1")
elif score > 90: #91-100
    print("You go together like coke and mint.2")
elif score >= 40: #40-90
    print("You are alright together.1")
elif score <= 50: #10-49
    print("You are alright together.2")
else:
    print(f"The score: {score}")
