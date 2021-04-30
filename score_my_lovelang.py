def lovelang(zodiac_sign1, zodiac_sign2, loveLang):
    lovelang_score = 0
    #QUALITY TIME
    if loveLang == "quality time":
        if ((zodiac_sign1 == 'Gemini' or zodiac_sign1 == 'Sagittarius' or zodiac_sign1 == 'Pisces')
        and (zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Sagittarius' or zodiac_sign2 == 'Pisces')): #YY
            lovelang_score += 60

        elif ((zodiac_sign1 == 'Gemini' or zodiac_sign1 == 'Sagittarius' or zodiac_sign1 == 'Pisces')
        and (zodiac_sign2 == 'Taurus' or zodiac_sign2 == 'Scorpio')): #YM
            lovelang_score += 40

        elif ((zodiac_sign1 == 'Gemini' or zodiac_sign1 == 'Sagittarius' or zodiac_sign1 == 'Pisces')
        and (zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Virgo' or
                   zodiac_sign2 == 'Capricorn' or zodiac_sign2 == 'Aquarius')): #NN
            lovelang_score -= 60

        elif ((zodiac_sign1 == 'Gemini' or zodiac_sign1 == 'Sagittarius' or zodiac_sign1 == 'Pisces')
        and (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Aries')): #NM
            lovelang_score -= 40

    #WORDS OF AFFIRMATION
    if loveLang == "words of affirmation":
        if ((zodiac_sign1 == 'Leo' or zodiac_sign1 == 'Aries')
        and (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Aries')): #YY
            lovelang_score += 60

        elif ((zodiac_sign1 == 'Leo' or zodiac_sign1 == 'Aries')
        and (zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Virgo'
        or zodiac_sign2 == 'Capricorn' or zodiac_sign2 == 'Aquarius')): #YM
            lovelang_score += 40

        elif ((zodiac_sign1 == 'Leo' or zodiac_sign1 == 'Aries')
        and (zodiac_sign2 == 'Taurus' or zodiac_sign2 == 'Scorpio')): #NN
            lovelang_score -= 60

        elif ((zodiac_sign1 == 'Leo' or zodiac_sign1 == 'Aries')
        and (zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Sagittarius' or zodiac_sign2 == 'Pisces')): #NM
            lovelang_score -= 40

    #ACTS OF SERVICE
    if loveLang == "acts of service":
        if ((zodiac_sign1 == 'Cancer' or zodiac_sign1 == 'Libra' or zodiac_sign1 == 'Virgo'
        or zodiac_sign1 == 'Capricorn' or zodiac_sign2 == 'Aquarius')
        and (zodiac_sign2 == 'Cancer'or zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Virgo'
        or zodiac_sign2 == 'Capricorn'or zodiac_sign2 == 'Aquarius')): #YY
            lovelang_score += 60

        elif ((zodiac_sign1 == 'Cancer' or zodiac_sign1 == 'Libra' or zodiac_sign1 == 'Virgo'
         or zodiac_sign1 == 'Capricorn' or zodiac_sign1 == 'Aquarius')
         and (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Aries')): #YM
            lovelang_score += 40

        elif ((zodiac_sign1 == 'Cancer' or zodiac_sign1 == 'Libra' or zodiac_sign1 == 'Virgo'
        or zodiac_sign1 == 'Capricorn' or zodiac_sign1 == 'Aquarius')
        and (zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Sagittarius' or zodiac_sign2 == 'Pisces')): #NN
            lovelang_score -= 60

        elif ((zodiac_sign1 == 'Cancer' or zodiac_sign1 == 'Libra' or zodiac_sign1 == 'Virgo'
        or zodiac_sign1 == 'Capricorn' or zodiac_sign1 == 'Aquarius')
        and (zodiac_sign2 == 'Taurus' or zodiac_sign2 == 'Scorpio')): #NM
            lovelang_score -= 40

    #PHYSICAL TOUCH
    if loveLang == "physical touch":
        if ((zodiac_sign1 == 'Taurus' or zodiac_sign1 == 'Scorpio')
        and (zodiac_sign2 == 'Taurus' or zodiac_sign2 == 'Scorpio')): #YY
            lovelang_score += 60

        elif ((zodiac_sign1 == 'Taurus' or zodiac_sign1 == 'Scorpio')
        and (zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Sagittarius' or zodiac_sign2 == 'Pisces')): #YM
            lovelang_score += 40

        elif ((zodiac_sign1 == 'Taurus' or zodiac_sign1 == 'Scorpio')
        and (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Aries')): #NN
            lovelang_score -= 60

        elif ((zodiac_sign1 == 'Taurus' or zodiac_sign1 == 'Scorpio')
        and (zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Virgo'
         or zodiac_sign2 == 'Capricorn' or zodiac_sign2 == 'Aquarius')): #NM
            lovelang_score -= 40

    return lovelang_score
