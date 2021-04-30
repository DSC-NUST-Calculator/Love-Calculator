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

#ZODIC
date_day1 = int(input("Day of your birth: 1 to 31"))
date_month1 = int(input("Month of your birth 1 to 12: "))

date_day2 = int(input("Day of their birth: 1 to 31"))
date_month2 = int(input("Month of their birth 1 to 12: "))

#Find my zodiac 1
zodiac_sign1 = ''
if (date_month1 == 1):
    if (date_day1 >= 20):
        zodiac_sign1 = 'Aquarius'
    elif (date_day1 < 20):
        zodiac_sign1 = 'Capricorn'

elif (date_month1 == 2):
    if (date_day1 >= 19):
        zodiac_sign1 = 'Pisces'
    elif (date_day1 < 19):
        zodiac_sign1 = 'Aquarius'

elif (date_month1 == 3):
    if (date_day1 >= 21):
        zodiac_sign1 = 'Aries'
    elif (date_day1 < 21):
        zodiac_sign1 = 'Pisces'

elif (date_month1 == 4):
    if (date_day1 >= 21):
        zodiac_sign1 = 'Taurus'
    elif (date_day1 < 21):
        zodiac_sign1 = 'Aries'

elif (date_month1 == 5):
    if (date_day1 >= 21):
        zodiac_sign1 = 'Gemini'
    elif (date_day1 < 21):
        zodiac_sign1 = 'Taurus'

elif (date_month1 == 6):
    if (date_day1 >= 21):
        zodiac_sign1 = 'Cancer'
    elif (date_day1 < 21):
        zodiac_sign1 = 'Gemini'

elif (date_month1 == 7):
    if (date_day1 >= 23):
        zodiac_sign1 = 'Leo'
    elif (date_day1 < 23):
        zodiac_sign1 = 'Cancer'

elif (date_month1 == 8):
    if (date_day1 >= 23):
        zodiac_sign1 = 'Virgo'
    elif (date_day1 < 23):
        zodiac_sign1 = 'Leo'

elif (date_month1 == 9):
    if (date_day1 >= 23):
        zodiac_sign1 = 'Libra'
    elif (date_day1 < 23):
        zodiac_sign1 = 'Virgo'

elif (date_month1 == 10):
    if (date_day1 >= 23):
        zodiac_sign1 = 'Scorpio'
    elif (date_day1 < 23):
        zodiac_sign1 = 'Libra'

elif (date_month1 == 11):
    if (date_day1 >= 22):
        zodiac_sign1 = 'Sagittarius'
    elif (date_day1 < 22):
        zodiac_sign1 = 'Scorpio'

elif (date_month1 == 12):
    if (date_day1 >= 22):
        zodiac_sign1 = 'Capricorn'
    elif (date_day1 < 22):
        zodiac_sign1 = 'Sagittarius'

else:
    print("date error")

#Find my zodiac 2
zodiac_sign2 = ''
if (date_month2 == 1):
    if (date_day2 >= 20):
        zodiac_sign2 = 'Aquarius'
    elif (date_day2 < 20):
        zodiac_sign2 = 'Capricorn'

elif (date_month2 == 2):
    if (date_day2 >= 19):
        zodiac_sign2 = 'Pisces'
    elif (date_day2 < 19):
        zodiac_sign2 = 'Aquarius'

elif (date_month2 == 3):
    if (date_day2 >= 21):
        zodiac_sign2 = 'Aries'
    elif (date_day2 < 21):
        zodiac_sign2 = 'Pisces'

elif (date_month2 == 4):
    if (date_day2 >= 21):
        zodiac_sign2 = 'Taurus'
    elif (date_day2 < 21):
        zodiac_sign2 = 'Aries'

elif (date_month2 == 5):
    if (date_day2 >= 21):
        zodiac_sign2 = 'Gemini'
    elif (date_day2 < 21):
        zodiac_sign2 = 'Taurus'

elif (date_month2 == 6):
    if (date_day2 >= 21):
        zodiac_sign2 = 'Cancer'
    elif (date_day2 < 21):
        zodiac_sign2 = 'Gemini'

elif (date_month2 == 7):
    if (date_day2 >= 23):
        zodiac_sign2 = 'Leo'
    elif (date_day2 < 23):
        zodiac_sign2 = 'Cancer'

elif (date_month2 == 8):
    if (date_day2 >= 23):
        zodiac_sign2 = 'Virgo'
    elif (date_day2 < 23):
        zodiac_sign2 = 'Leo'

elif (date_month2 == 9):
    if (date_day2 >= 23):
        zodiac_sign2 = 'Libra'
    elif (date_day2 < 23):
        zodiac_sign2 = 'Virgo'

elif (date_month2 == 10):
    if (date_day2 >= 23):
        zodiac_sign2 = 'Scorpio'
    elif (date_day2 < 23):
        zodiac_sign2 = 'Libra'

elif (date_month2 == 11):
    if (date_day2 >= 22):
        zodiac_sign2 = 'Sagittarius'
    elif (date_day2 < 22):
        zodiac_sign2 = 'Scorpio'

elif (date_month2 == 12):
    if (date_day2 >= 22):
        zodiac_sign2 = 'Capricorn'
    elif (date_day2 < 22):
        zodiac_sign2 = 'Sagittarius'

else:
    print("date error")

#Zodiac zodiac_score
if (zodiac_sign1 == 'Aquarius'):
    if (zodiac_sign2 == 'Aries' or zodiac_sign2 == 'Gemini'):
        zodiac_score = 'Y'
    elif (zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Scorpio'):
        zodiac_score = 'N'
    elif (zodiac_sign2 == 'Aquarius'):
        zodiac_score = 'N' #too egoistic when they’re in a romantic relationship
    else:
        zodiac_score = 'Z'

elif (zodiac_sign1 == 'Pisces'):
    if (zodiac_sign2 == 'Cancer'):
        zodiac_score = 'Y'
    elif (zodiac_sign2 == 'Aries' or zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Libra'):
        zodiac_score = 'N'
    elif (zodiac_sign2 == 'Pisces'):
        zodiac_score = 'YY' #most perfect couples of the zodiac
    else:
        zodiac_score = 'Z'

elif (zodiac_sign1 == 'Aries'):
    if (zodiac_sign2 == 'Aquarius' or zodiac_sign2 == 'Sagittarius'):
        zodiac_score = 'Y'
    elif (zodiac_sign2 == 'Pisces' or zodiac_sign2 == 'Cancer'):
        zodiac_score = 'N'
    elif (zodiac_sign2 == 'Aries'):
        zodiac_score = 'NM' #first time, they will be extremely attracted && Quarrels and misunderstandings are inevitable
    else:
        zodiac_score = 'Z'

elif (zodiac_sign1 == 'Taurus'):
    if (zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Virgo' or zodiac_sign2 == 'Capricorn'):
        zodiac_score = 'Y'
    elif (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Scorpio'):
        zodiac_score = 'N'
    elif (zodiac_sign2 == 'Taurus'):
        zodiac_score = 'YY' #stable and long-term
    else:
        zodiac_score = 'Z'

elif (zodiac_sign1 == 'Gemini'):
    if (zodiac_sign2 == 'Aquarius' or zodiac_sign2 == 'Libra'):
        zodiac_score = 'Y'
    elif (zodiac_sign2 == 'Scorpio' or zodiac_sign2 == 'Capricorn' or zodiac_sign2 == 'Pisces'):
        zodiac_score = 'N'
    elif (zodiac_sign2 == 'Gemini'):
        zodiac_score = 'YM' #Good, but unstable in the long run
    else:
        zodiac_score = 'Z'

elif (zodiac_sign1 == 'Cancer'):
    if (zodiac_sign2 == 'Taurus' or zodiac_sign2 == 'Pisces' or zodiac_sign2 == 'Scorpio'):
        zodiac_score = 'Y'
    elif (zodiac_sign2 == 'Aquarius' or zodiac_sign2 == 'Aries'):
        zodiac_score = 'N'
    elif (zodiac_sign2 == 'Cancer'):
        zodiac_score = 'YY'
    else:
        zodiac_score = 'Z'

elif (zodiac_sign1 == 'Leo'):
    if (zodiac_sign2 == 'Sagittarius'):
        zodiac_score = 'Y'
    elif (zodiac_sign2 == 'Taurus' or zodiac_sign2 == 'Capricorn'):
        zodiac_score = 'N'
    elif (zodiac_sign2 == 'Leo'):
        zodiac_score = 'M'
    else:
        zodiac_score = 'Z'

elif (zodiac_sign1 == 'Virgo'):
    if (zodiac_sign2 == 'Taurus'):
        zodiac_score = 'Y'
    elif (zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Sagittarius'):
        zodiac_score = 'N'
    elif (zodiac_sign2 == 'Virgo'):
        zodiac_score = 'YY'
    else:
        zodiac_score = 'Z'

elif (zodiac_sign1 == 'Libra'):
    if (zodiac_sign2 == 'Gemini'):
        zodiac_score = 'Y'
    elif (zodiac_sign2 == 'Virgo' or zodiac_sign2 == 'Scorpio' or zodiac_sign2 == 'Pisces'):
        zodiac_score = 'N'
    elif (zodiac_sign2 == 'Libra'):
        zodiac_score = 'M' # can be either very good or extremely bad combination, no in-between
    else:
        zodiac_score = 'Z'

elif (zodiac_sign1 == 'Scorpio'):
    if (zodiac_sign2 == 'Cancer'):
        zodiac_score = 'Y'
    elif (zodiac_sign2 == 'Aquarius' or zodiac_sign2 == 'Gemini' or zodiac_sign2 == ' Taurus' or zodiac_sign2 == 'Libra'):
        zodiac_score = 'N'
    elif (zodiac_sign2 == 'Scorpio'):
        zodiac_score = 'NM' #intense relationship
    else:
        zodiac_score = 'Z'

elif (zodiac_sign1 == 'Sagittarius'):
    if (zodiac_sign2 == 'Leo'):
        zodiac_score = 'Y'
    elif (zodiac_sign2 == 'Virgo' or zodiac_sign2 == 'Capricorn'):
        zodiac_score = 'N'
    elif (zodiac_sign2 == 'Sagittarius'):
        zodiac_score = 'NM' #little chance of success
    else:
        zodiac_score = 'Z'

elif (zodiac_sign1 == 'Capricorn'):
    if (zodiac_sign2 == 'Taurus'):
        zodiac_score = 'Y'
    elif (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Sagittarius' or zodiac_sign2 == 'Gemini'):
        zodiac_score = 'N'
    elif (zodiac_sign2 == 'Capricorn'):
        zodiac_score = 'YY'
    else:
        zodiac_score = 'Z'

else:
    zodiac_score = 'error'

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

#Love Language
loveLang = input('What is your Love Language:\n"Quality Time", "Words of Affirmation", "Acts of Service" or "Physical Touch"?\n')                                #added quotations for clearer understanding
loveLang = loveLang.lower()

#QUALITY TIME
if loveLang == "quality time":
    if ((zodiac_sign1 == 'Gemini' or zodiac_sign1 == 'Sagittarius' or zodiac_sign1 == 'Pisces')
    and (zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Sagittarius' or zodiac_sign2 == 'Pisces')): #YY
        score += 60

    elif ((zodiac_sign1 == 'Gemini' or zodiac_sign1 == 'Sagittarius' or zodiac_sign1 == 'Pisces')
    and (zodiac_sign2 == 'Taurus' or zodiac_sign2 == 'Scorpio')): #YM
        score += 40

    elif ((zodiac_sign1 == 'Gemini' or zodiac_sign1 == 'Sagittarius' or zodiac_sign1 == 'Pisces')
    and (zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Virgo' or
               zodiac_sign2 == 'Capricorn' or zodiac_sign2 == 'Aquarius')): #NN
        score -= 60

    elif ((zodiac_sign1 == 'Gemini' or zodiac_sign1 == 'Sagittarius' or zodiac_sign1 == 'Pisces')
    and (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Aries')): #NM
        score -= 40

#WORDS OF AFFIRMATION
if loveLang == "words of affirmation":
    if ((zodiac_sign1 == 'Leo' or zodiac_sign1 == 'Aries')
    and (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Aries')): #YY
        score += 60

    elif ((zodiac_sign1 == 'Leo' or zodiac_sign1 == 'Aries')
    and (zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Virgo'
    or zodiac_sign2 == 'Capricorn' or zodiac_sign2 == 'Aquarius')): #YM
        score += 40

    elif ((zodiac_sign1 == 'Leo' or zodiac_sign1 == 'Aries')
    and (zodiac_sign2 == 'Taurus' or zodiac_sign2 == 'Scorpio')): #NN
        score -= 60

    elif ((zodiac_sign1 == 'Leo' or zodiac_sign1 == 'Aries')
    and (zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Sagittarius' or zodiac_sign2 == 'Pisces')): #NM
        score -= 40

#ACTS OF SERVICE
if loveLang == "acts of service":
    if ((zodiac_sign1 == 'Cancer' or zodiac_sign1 == 'Libra' or zodiac_sign1 == 'Virgo'
    or zodiac_sign1 == 'Capricorn' or zodiac_sign2 == 'Aquarius')
    and (zodiac_sign2 == 'Cancer'or zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Virgo'
    or zodiac_sign2 == 'Capricorn'or zodiac_sign2 == 'Aquarius')): #YY
        score += 60

    elif ((zodiac_sign1 == 'Cancer' or zodiac_sign1 == 'Libra' or zodiac_sign1 == 'Virgo'
     or zodiac_sign1 == 'Capricorn' or zodiac_sign1 == 'Aquarius')
     and (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Aries')): #YM
        score += 40

    elif ((zodiac_sign1 == 'Cancer' or zodiac_sign1 == 'Libra' or zodiac_sign1 == 'Virgo'
    or zodiac_sign1 == 'Capricorn' or zodiac_sign1 == 'Aquarius')
    and (zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Sagittarius' or zodiac_sign2 == 'Pisces')): #NN
        score -= 60

    elif ((zodiac_sign1 == 'Cancer' or zodiac_sign1 == 'Libra' or zodiac_sign1 == 'Virgo'
    or zodiac_sign1 == 'Capricorn' or zodiac_sign1 == 'Aquarius')
    and (zodiac_sign2 == 'Taurus' or zodiac_sign2 == 'Scorpio')): #NM
        score -= 40

#PHYSICAL TOUCH
if loveLang == "physical touch":
    if ((zodiac_sign1 == 'Taurus' or zodiac_sign1 == 'Scorpio')
    and (zodiac_sign2 == 'Taurus' or zodiac_sign2 == 'Scorpio')): #YY
        score += 60

    elif ((zodiac_sign1 == 'Taurus' or zodiac_sign1 == 'Scorpio')
    and (zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Sagittarius' or zodiac_sign2 == 'Pisces')): #YM
        score += 40

    elif ((zodiac_sign1 == 'Taurus' or zodiac_sign1 == 'Scorpio')
    and (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Aries')): #NN
        score -= 60

    elif ((zodiac_sign1 == 'Taurus' or zodiac_sign1 == 'Scorpio')
    and (zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Virgo'
     or zodiac_sign2 == 'Capricorn' or zodiac_sign2 == 'Aquarius')): #NM
        score -= 40














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
