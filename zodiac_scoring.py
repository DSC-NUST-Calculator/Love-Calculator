#This file only contain the function to match the zodiac signs (please dont edit!)
def match_zodiacs(zodiac_sign1, zodiac_sign2):
    if (zodiac_sign1 == 'Aquarius'):
        if (zodiac_sign2 == 'Aries' or zodiac_sign2 == 'Gemini'):
            zodiac_scoring = 'Y'
        elif (zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Scorpio'):
            zodiac_scoring = 'N'
        elif (zodiac_sign2 == 'Aquarius'):
            zodiac_scoring = 'N' #too egoistic when they’re in a romantic relationship

    elif (zodiac_sign1 == 'Pisces'):
        if (zodiac_sign2 == 'Cancer'):
            zodiac_scoring = 'Y'
        elif (zodiac_sign2 == 'Aries' or zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Libra'):
            zodiac_scoring = 'N'
        elif (zodiac_sign2 == 'Pisces'):
            zodiac_scoring = 'YY' #most perfect couples of the zodiac

    elif (zodiac_sign1 == 'Aries'):
        if (zodiac_sign2 == 'Aquarius' or zodiac_sign2 == 'Sagittarius'):
            zodiac_scoring = 'Y'
        elif (zodiac_sign2 == 'Pisces' or zodiac_sign2 == 'Cancer'):
            zodiac_scoring = 'N'
        elif (zodiac_sign2 == 'Aries'):
            zodiac_scoring = 'NM' #first time, they will be extremely attracted && Quarrels and misunderstandings are inevitable

    elif (zodiac_sign1 == 'Taurus'):
        if (zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Virgo' or zodiac_sign2 == 'Capricorn'):
            zodiac_scoring = 'Y'
        elif (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Scorpio'):
            zodiac_scoring = 'N'
        elif (zodiac_sign2 == 'Taurus'):
            zodiac_scoring = 'YY' #stable and long-term

    elif (zodiac_sign1 == 'Gemini'):
        if (zodiac_sign2 == 'Aquarius' or zodiac_sign2 == 'Libra'):
            zodiac_scoring = 'Y'
        elif (zodiac_sign2 == 'Scorpio' or zodiac_sign2 == 'Capricorn' or zodiac_sign2 == 'Pisces'):
            zodiac_scoring = 'N'
        elif (zodiac_sign2 == 'Gemini'):
            zodiac_scoring = 'YM' #Good, but unstable in the long run

    elif (zodiac_sign1 == 'Cancer'):
        if (zodiac_sign2 == 'Taurus' or zodiac_sign2 == 'Pisces' or zodiac_sign2 == 'Scorpio'):
            zodiac_scoring = 'Y'
        elif (zodiac_sign2 == 'Aquarius' or zodiac_sign2 == 'Aries'):
            zodiac_scoring = 'N'
        elif (zodiac_sign2 == 'Cancer'):
            zodiac_scoring = 'YY'

    elif (zodiac_sign1 == 'Leo'):
        if (zodiac_sign2 == 'Sagittarius'):
            zodiac_scoring = 'Y'
        elif (zodiac_sign2 == 'Taurus' or zodiac_sign2 == 'Capricorn'):
            zodiac_scoring = 'N'
        elif (zodiac_sign2 == 'Leo'):
            zodiac_scoring = 'M'

    elif (zodiac_sign1 == 'Virgo'):
        if (zodiac_sign2 == 'Taurus'):
            zodiac_scoring = 'Y'
        elif (zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Sagittarius'):
            zodiac_scoring = 'N'
        elif (zodiac_sign2 == 'Virgo'):
            zodiac_scoring = 'YY'

    elif (zodiac_sign1 == 'Libra'):
        if (zodiac_sign2 == 'Gemini'):
            zodiac_scoring = 'Y'
        elif (zodiac_sign2 == 'Virgo' or zodiac_sign2 == 'Scorpio' or zodiac_sign2 == 'Pisces'):
            zodiac_scoring = 'N'
        elif (zodiac_sign2 == 'Libra'):
            zodiac_scoring = 'M' # can be either very good or extremely bad combination, no in-between

    elif (zodiac_sign1 == 'Scorpio'):
        if (zodiac_sign2 == 'Cancer'):
            zodiac_scoring = 'Y'
        elif (zodiac_sign2 == 'Aquarius' or zodiac_sign2 == 'Gemini' or zodiac_sign2 == ' Taurus' or zodiac_sign2 == 'Libra'):
            zodiac_scoring = 'N'
        elif (zodiac_sign2 == 'Scorpio'):
            zodiac_scoring = 'NM' #intense relationship

    elif (zodiac_sign1 == 'Sagittarius'):
        if (zodiac_sign2 == 'Leo'):
            zodiac_scoring = 'Y'
        elif (zodiac_sign2 == 'Virgo' or zodiac_sign2 == 'Capricorn'):
            zodiac_scoring = 'N'
        elif (zodiac_sign2 == 'Sagittarius'):
            zodiac_scoring = 'NM' #little chance of success

    elif (zodiac_sign1 == 'Capricorn'):
        if (zodiac_sign2 == 'Taurus'):
            zodiac_scoring = 'Y'
        elif (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Sagittarius' or zodiac_sign2 == 'Gemini'):
            zodiac_scoring = 'N'
        elif (zodiac_sign2 == 'Capricorn'):
            zodiac_scoring = 'YY'

    else:
        zodiac_scoring = 'error'

    return zodiac_scoring


    #Y      YES                 +50
    #YY     Mostdefinitly YES   +80
    #YM     YES maybe           +20
    #N      NO                  -50
    #NN     NEVER               -80
    #NM     NO maybe            -20
