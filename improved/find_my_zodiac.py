#This file only contain the function to find the zodiac sign (please dont edit!)
def zodiac_chk(month, day):
    #print(f"\n{day}-{month}-2021")
    zodiac_sign = ''
    if (month == 1):
        if (day >= 20):
            zodiac_sign = 'Aquarius'
        elif (day < 20):
            zodiac_sign = 'Capricorn'

    elif (month == 2):
        if (day >= 19):
            zodiac_sign = 'Pisces'
        elif (day < 19):
            zodiac_sign = 'Aquarius'

    elif (month == 3):
        if (day >= 21):
            zodiac_sign = 'Aries'
        elif (day < 21):
            zodiac_sign = 'Pisces'

    elif (month == 4):
        if (day >= 21):
            zodiac_sign = 'Taurus'
        elif (day < 21):
            zodiac_sign = 'Aries'

    elif (month == 5):
        if (day >= 21):
            zodiac_sign = 'Gemini'
        elif (day < 21):
            zodiac_sign = 'Taurus'

    elif (month == 6):
        if (day >= 21):
            zodiac_sign = 'Cancer'
        elif (day < 21):
            zodiac_sign = 'Gemini'

    elif (month == 7):
        if (day >= 23):
            zodiac_sign = 'Leo'
        elif (day < 23):
            zodiac_sign = 'Cancer'

    elif (month == 8):
        if (day >= 23):
            zodiac_sign = 'Virgo'
        elif (day < 23):
            zodiac_sign = 'Leo'

    elif (month == 9):
        if (day >= 23):
            zodiac_sign = 'Libra'
        elif (day < 23):
            zodiac_sign = 'Virgo'

    elif (month == 10):
        if (day >= 23):
            zodiac_sign = 'Scorpio'
        elif (day < 23):
            zodiac_sign = 'Libra'

    elif (month == 11):
        if (day >= 22):
            zodiac_sign = 'Sagittarius'
        elif (day < 22):
            zodiac_sign = 'Scorpio'

    elif (month == 12):
        if (day >= 22):
            zodiac_sign = 'Capricorn'
        elif (day < 22):
            zodiac_sign = 'Sagittarius'

    else:
        print("date error")

    return zodiac_sign
