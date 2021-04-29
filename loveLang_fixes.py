loveLang = input('What is your Love Language:\n"Quality Time", "Words of Affirmation", '    #added quotations for clearer understanding
                 '"Acts of Service" or "Physical Touch"?\n')                                #added quotations for clearer understanding
loveLang = loveLang.lower()

while loveLang not in {"quality time", "words of affirmation", "acts of service", "physical touch"}:
    loveLang = input('What is your Love Language:\n"Quality Time", "Words of Affirmation", '    #added quotations for clearer understanding
                     '"Acts of Service" or "Physical Touch"?\n')                                #added quotations for clearer understanding
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
