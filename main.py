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
score = name_chk*1.2              #add to final score

print(f"Score now: {score}") #debug display


#ZODIC (only affect end percentage not points)
import find_my_zodiac
import zodiac_scoring

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

    zodiac_score = zodiac_scoring.match_zodiacs(zodiac_sign1, zodiac_sign2)#match the zodiacs

    print(zodiac_sign1) #debug display
    print(zodiac_sign2) #debug display
    print(zodiac_score) #debug display

#EYE COLOR




#score += eye_result

#HAIR COLOR






#AGE DIFFERENCE







#Zodiac Dominate SCORE
if (zodiac_rqst == 'y'):
    if (zodiac_score == 'Y'):
        score += score*1.5
    elif (zodiac_score == 'YY'):
        score += score*1.8
    elif (zodiac_score == 'YM'):
        score += score*1.2
    elif (zodiac_score == 'N'):
        score -= score*0.5
    elif (zodiac_score == 'NN'):
        score -= score*0.2
    elif (zodiac_score == 'NM'):
        score -= score*0.8
    elif (zodiac_score == 'error'):
        print("ERROR in zodiac_scoring")

#SCORE OUTPUT (please verify)
if score < 10: #0-9
    print("Sorry, the universe said no...")
    print('''
    ─────────────███████████████────────────
──────────████▒▒▒▒▒▒▒▒▒▒▒▒▒████─────────
────────███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███───────
───────██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███─────
──────██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒███████▒▒▒██────
─────██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒██▒▒▒██───
────██▒▒██▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒██──
───██▒▒▒▒▒████▒▒▒▒██▒▒▒██▒▒▒▒▒▒▒▒██▒▒█──
───█▒▒▒▒▒▒▒▒▒▒▒███░█▒▒▒█░███▒▒▒▒▒▒▒▒▒█──
───█▒▒▒▒▒██████░░░░█▒▒▒█░░░░██████▒▒▒█──
───█▒▒▒▒▒▒▒█░░░░▓▓██▒▒▒██▓▓░░░░█▒▒▒▒▒█──
───█▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒██████▒█▒▒▒▒█──
───█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒█──
───█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░█▒▒▒█──
───██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░█▒▒██──
────██▒▒▒▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒██▒▒██───
─────██▒▒▒▒▒▒█████▒▒▒▒▒▒█████▒▒▒▒▒██────
──────██▒▒▒███▒▒▒▒▒████▒▒▒▒▒███▒▒██─────
───────███▒▒▒▒▒▒▒▒█▒▒▒▒█▒▒▒▒▒▒▒▒██──────
─────────███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███───────
───────────█████▒▒▒▒▒▒▒▒▒██████─────────
───────────────████████████─────────────

''')
    print("Here, first one's for free")
elif score > 90: #91-100
    print("Your relationship is the fire, the one desire")
    print('''
    ──────────────────▒
─────────────────░█
────────────────███
───────────────██ღ█
──────────────██ღ▒█──────▒█
─────────────██ღ░▒█───────██
─────────────█ღ░░ღ█──────█ღ▒█
────────────█▒ღ░▒ღ░█───██░ღღ█
───────────░█ღ▒░░▒ღ░████ღღღ█
───░───────█▒ღ▒░░░▒ღღღ░ღღღ██─────░█
───▓█─────░█ღ▒░░░░░░░▒░ღღ██─────▓█░
───██─────█▒ღ░░░░░░░░░░ღ█────▓▓██
───██────██ღ▒░░░░░░░░░ღ██─░██ღ▒█
──██ღ█──██ღ░▒░░░░░░░░░░ღ▓██▒ღღ█
──█ღღ▓██▓ღ░░░▒░░░░░░░░▒░ღღღ░░▓█
─██ღ▒▒ღღ░░ღღღღ░░▒░░░░ ღღღღ░░ღღღ██
─█ღ▒ღღ█████████ღღ▒░ღ██████████ღ▒█░
██ღღ▒████████████ღღ████████████░ღ█▒
█░ღღ████████████████████████████ღღ█
█▒ღ██████████████████████████████ღ█
██ღღ████████████████████████████ღ██
─██ღღ██████████████████████████ღ██
──░██ღღ██████████████████████ღღ██
────▓██ღ▒██████████████████▒ღ██
───░──░███ღ▒████████████▒ღ███
────░░───▒██ღღ████████▒ღ██
───────────▒██ღ██████ღ██
─────────────██ღ████ღ█
───────────────█ღ██ღ█
────────────────█ღღ█
────────────────█ღ█░
─────────────────██░
''')
elif score >= 40: #40-90
    print("Maybe... you have a nice personality?")
    print('''
    ´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´´´´´´¶¶¶´´´´´´´´´´´´´´´´´
´´´´´´´´´´´´¶´´´´´´´´´´´´¶´´´´´´´´´´´´´´´´
´´´´´´´´´´¶¶´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´
´´´´´´´´´´¶´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´´
´´´´´´´´´¶´´´´´´´´´´´´´´´´´´¶´´´´´´´´´´´´´
´´´´´´´´¶´´´´´´´´´´´´´´´´´´´´¶´´´´´´´´´´´´
´´´´´´´´¶¶¶¶¶¶´´´¶¶¶¶¶¶´´´´´´´¶´´´´´´´´´´´
´´´´´´´¶´¶¶¶´´´´´´¶¶¶¶´´´´´´´´¶´´´´´´´´´´´
´´´´´´´¶´¶¶¶´´´´´´¶¶¶¶´´´´´´´´¶´´´´´´´´´´´
´´´´´´´´´¶¶¶´´´´´´¶¶¶¶´´´´´´´´´¶´´´´´´´´´´
´´´´´´¶´´¶¶¶´´´´´´¶¶¶´´´´´´´´¶¶¶´´´´´´´´´´
´´´´´´¶´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
´´´´´´¶´´´´´´´´´´´´¶¶¶¶´´´´´´´´¶´´´´´´´´´´
´´´´´´¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶´´´´´´´´´´
´´´´´´´¶´´´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´´´¶´´´´´´´´´
´´´´´´´¶´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶´´´´´´´´´´
´´´´´´´¶´´´´´¶¶¶¶¶¶¶¶¶¶´´¶´´´´´¶´´´´´´´´´´
´´´´´´´´¶´´´´´´´¶¶¶¶¶¶¶´¶´´¶´¶¶´´´´´´´´´´´
´´´´´´´´¶´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
´´´´´´´´´¶´´´´´´´´´´´´´´´´´´¶´´´´´´´´´´´´´
´´´´´´´´´´¶´´´´´´´´´´´´´´´´¶´´´´´´´´´´´´´´
´´´´´´´´´´´¶´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´
´¶¶´´´´´´´´´¶¶´´´´´´´´´´´¶¶¶¶´´´´¶¶¶¶¶¶¶¶´
´¶¶¶¶¶´´´´´´´´¶¶´´´´´´¶¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶
´´´¶¶¶¶¶¶¶´´´´´´´´¶¶´´´´´´´¶¶¶¶¶´´´´´´´´´´
´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´
´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´´¶¶¶¶¶¶´
´´´´´´´´´´´´´´´´´´´´´´´´´´´¶´´´´¶´´´´´´´¶¶
´´´´´´´´´´´´´´´´´´´´´´´´´´´¶´´´´¶¶´´´´´¶´´
´´´´´´´´´´´´´´´´´´´´´´´´´´´¶´´´´´¶´´´´´¶´¶
´´´´´´´´´´´´´´´´´´´´´´´´´´´¶´´´´´¶¶´´´´¶´¶
´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´¶´´´¶¶´´´´¶´¶
´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´¶¶¶¶¶´¶¶´´´´¶¶¶
´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´¶´¶
¶¶¶¶¶¶¶¶´´´´´´´´´´¶´´¶¶¶¶¶¶´´¶¶¶¶¶¶¶´´´¶´¶
´´´´´´´´´´´´´´´´´´´¶´´´´´´´´¶´´´´´¶¶¶¶´¶´¶
´´´´´´´´´´´´´´´´´´´´¶´´´´´´¶´´´´´´´´¶¶¶¶´¶
´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´¶¶¶¶´
''')
elif score <= 50: #10-49
    print("Maybe its best you see someone else...")
    print('''
    ──▄▀▀▀▀▄▄▄▀▀▀▀▀▀▀▀▀▄
▄▀──────────────────▀▀▄
█─────────────────────▀▀▄
█───▄▀▀▀▀▀▀▄────────────█
█─▄▀────────▀▀▀▄───▄▀▀▀▀▀▀▄
█─█─────────────▀▀▄▀─▀▀▄───▀▄
█─█─▀▀▄──▄████▄───█──────────█
█─█──────██████▄──█─▀▀▀▄──────█
█─█─▄▄▄──███████──█────────────█
█─█▄─────▀██████──█───▄█████▄──█
█──█──▄▄▀─▀████▀──█───███████──█
█──▀▄───────────▄▀█───███████──█
█────▀▀▄▄▄▄▄▄▄▄▀▀─█▄──▀█████▀──█
█──────────────▄───█───────────█
█──────────▄────▀▄─▀█▄▄▄▄▄▄▄▀▀▀
█───────────▀▄───█──▄▄▄▄▀
█────────────█───█──█
█────────────█───█──█
█───────────▄▀──█───█
█─────────▄▀───█────█
█─────────█───█─────█
█─────────▀█▄▄▀─────█
█──────────────────▄▀
█─────▄▀▀▀▄▄───────▀▄
█─────█────▀▀▀▀▄▄▄▄▄▀
█─────▀▀▄
█────────▀▀▄
█─────▄▄▄▄▄▀
█─▀▄─█
█─▀──█
█────█
''')
    print("Like my friend Lenny, for instance")
else:
    print(f"The score: {score}")

print(f"The score end: {score}") #debug display
