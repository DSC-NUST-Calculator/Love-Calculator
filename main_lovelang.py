#Dont change these codes
print("Welcome to the DSC Love Calculaor")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Your code goes below
#NAME TRUE TEST worth: 20%
name_chk = 0
name_str = name1+name2            #combine both names
name_str = name_str.lower()       #make comined name string into lower case.
name_chk += name_str.count("t")   #count in comined name string for "t"
name_chk += name_str.count("r")   #count in comined name string for "r"
name_chk += name_str.count("u")   #count in comined name string for "u"
name_chk += name_str.count("e")   #count in comined name string for "e"

score = (name_chk/20)*100         #add to final score

print(f"Score now: {score}") #debug display


#ZODIC (only affect end percentage not points)
import find_my_zodiac
import zodiac_scoring

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
        date_day2 = int(input("Day of their birth: "))
    except ValueError:
        date_day2 = int(input("Day of their birth: 1 to 31"))
date_month2 = 0
while 1 > date_month2 or 12 < date_month2: #check if month is between 1 - 12
    try:
        date_month2 = int(input("Month of their birth (digits): "))
    except ValueError:
        date_month2 = int(input("Month of their birth 1 to 12: "))

zodiac_sign1 = find_my_zodiac.zodiac_chk(date_month1, date_day1) #find zodiac for date 1
zodiac_sign2 = find_my_zodiac.zodiac_chk(date_month2, date_day2)#find zodiac for date 2

print(zodiac_sign1) #debug display
print(zodiac_sign2) #debug display

zodiac_score = zodiac_scoring.match_zodiacs(zodiac_sign1, zodiac_sign2)#match the zodiacs

print(zodiac_score) #debug display

if (zodiac_score == 'Y'):
    score += 50
elif (zodiac_score == 'YY'):
    score += 80
elif (zodiac_score == 'YM'):
    score += 20
elif (zodiac_score == 'Z'):
    pass
elif (zodiac_score == 'N'):
    score -= 50
elif (zodiac_score == 'NN'):
    score -= 20
elif (zodiac_score == 'NM'):
    score -= 80

print(f"Score now: {score}") #debug display

#Love Language
import score_my_lovelang

loveLang = input('What is your Love Language:\n"Quality Time", "Words of Affirmation", "Acts of Service" or "Physical Touch"?\n')                                #added quotations for clearer understanding
loveLang = loveLang.lower()

while loveLang not in {"quality time", "words of affirmation", "acts of service", "physical touch"}: #input error handler
    loveLang = input('What is your Love Language:\n"Quality Time", "Words of Affirmation", "Acts of Service" or "Physical Touch"?\n')                                #added quotations for clearer understanding
    loveLang = loveLang.lower()                                                                 #moved it into while loop.

print("loveLang: " + loveLang) #debug display

score += score_my_lovelang.lovelang(zodiac_sign1, zodiac_sign2, loveLang)

print(f"Score now: {score}") #debug display

#score += eye_result

#HAIR COLOR






#AGE DIFFERENCE







#SCORE OUTPUT (please verify)
score = (score/300)*100

if (score < -100):
    print("A Holy war is apon us")
elif (score < -80):
    print("-80%")
elif (score < -60):
    print("-60%")
elif (score < -40):
    print("-40%")
elif (score < -20):
    print("-20%")
elif (score == 0):
    print("Not gonna happen")
elif (score < 20):
    print("20%")
elif (score < 40):
    print("40%")
elif (score < 60):
    print("60%")
elif (score < 80):
    print("80%")
elif (score < 100):
    print("A match made in the stars")

print(f"The Final score {score}") #debug display
