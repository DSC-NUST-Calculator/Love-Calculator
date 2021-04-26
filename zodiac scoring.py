import find_my_zodiac

#Here we edit and make zodiac scoring
date_day1 = int(input("Day of your birth: ") or 29)
date_month1 = int(input("Month of your birth (digits): ") or 1)

date_day2 = int(input("Day of their birth: ") or 24)
date_month2 = int(input("Month of their birth (digits): ") or 10)

zodiac_sign1 = find_my_zodiac.zodiac_chk(date_month1, date_day1) #find zodiac for date 1
zodiac_sign2 = find_my_zodiac.zodiac_chk(date_month2, date_day2)#find zodiac for date 2

print(zodiac_sign1)
print(zodiac_sign2)

score = 2

if (zodiac_sign1 == 'Aquarius'):
    if (zodiac_sign2 == ('Aries' or 'Gemini')):
        score = 'Y'
    elif (zodiac_sign2 == ('Cancer' or 'Scorpio')):
        score = 'N'

elif (zodiac_sign1 == 'Pisces'):
    if (zodiac_sign2 == 'Cancer'):
        score += 1
    if (zodiac_sign2 == ('Aries' or 'Gemini' or 'Libra')):
        score -= 1

elif (zodiac_sign1 == 'Aries'):
    if (zodiac_sign2 == ('Aquarius' or  'Sagittarius')):
        score += 1
    if (zodiac_sign2 == ('Pisces' or 'Cancer')):
        score -= 1

elif (zodiac_sign1 == 'Taurus'):
    if (zodiac_sign2 == ('Cancer' or 'Virgo' or 'Capricorn')):
        score += 1
    if (zodiac_sign2 == ('Leo' or 'Scorpio')):
        score -= 1

elif (zodiac_sign1 == 'Gemini'):
    if (zodiac_sign2 == ('Aquarius' or 'Libra')):
        score += 1
    if (zodiac_sign2 == ('Scorpio' or 'Capricorn' or 'Pisces')):
        score -= 1

elif (zodiac_sign1 == 'Cancer'):
    if (zodiac_sign2 == ('Taurus' or 'Pisces' or 'Scorpio')):
        score += 1
    if (zodiac_sign2 == ('Aquarius' or 'Aries')):
        score -= 1

elif (zodiac_sign1 == 'Leo'):
    if (zodiac_sign2 == 'Sagittarius'):
        score += 1
    if (zodiac_sign2 == ('Taurus' or 'Capricorn')):
        score -= 1

elif (zodiac_sign1 == 'Virgo'):
    if (zodiac_sign2 == 'Taurus'):
        score += 1
    if (zodiac_sign2 == ('Libra' or 'Sagittarius')):
        score -= 1

elif (zodiac_sign1 == 'Libra'):
    if (zodiac_sign2 == 'Gemini'):
        score += 1
    if (zodiac_sign2 == ('Virgo' or 'Scorpio' or 'Pisces')):
        score -= 1

elif (zodiac_sign1 == 'Scorpio'):
    if (zodiac_sign2 == 'Cancer'):
        score += 1
    if (zodiac_sign2 == ('Aquarius' or 'Gemini' or ' Taurus' or 'Libra')):
        score -= 1

elif (zodiac_sign1 == 'Sagittarius'):
    if (zodiac_sign2 == 'Leo'):
        score += 1
    if (zodiac_sign2 == ('Virgo' or 'Capricorn')):
        score -= 1

elif (zodiac_sign1 == 'Capricorn'):
    if (zodiac_sign2 == 'Taurus'):
        score += 1
    if (zodiac_sign2 == ('Leo' or 'Sagittarius' or 'Gemini')):
        score -= 1
print(score)
if (score < 0):
    print("You are no match")
else:
    print("You are a match made in the stars")
