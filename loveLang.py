import zodiac_scoring

loveLang = input("What is your Love Language:\nQuality Time, Words of Affirmation, "
                 "Acts of Service or Physical Touch?\n")
loveLang = loveLang.lower()

while loveLang not in {"quality time", "words of affirmation", "acts of service", "physical touch"}:
    input("What is your Love Language:\nQuality Time, Words of Affirmation, "
          "Acts of Service or Physical Touch?\n")
    loveLang = loveLang.lower()

# score:
# YY (Most Definately)  = +60
# YM (Yes-Maybe)        = +40
# NN (Definately Not)   = -60
# NM (No-Maybe)         = -40

#QUALITY TIME
if loveLang == "quality time":
    if ((zodiac_scoring.zodiac_sign1 == 'Gemini' or zodiac_scoring.zodiac_sign1 == 'Sagittarius' or zodiac_scoring.zodiac_sign1 == 'Pisces')
            and (zodiac_scoring.zodiac_sign2 == 'Gemini' or zodiac_scoring.zodiac_sign2 == 'Sagittarius' or zodiac_scoring.zodiac_sign2 == 'Pisces')): #YY
        main.score += int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Gemini' or zodiac_scoring.zodiac_sign1 == 'Sagittarius' or zodiac_scoring.zodiac_sign1 == 'Pisces')
          and (zodiac_scoring.zodiac_sign2 == 'Taurus' or zodiac_scoring.zodiac_sign2 == 'Scorpio')): #YM
        main.score += int(((40/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Gemini' or zodiac_scoring.zodiac_sign1 == 'Sagittarius' or zodiac_scoring.zodiac_sign1 == 'Pisces')
          and (zodiac_scoring.zodiac_sign2 == 'Cancer' or zodiac_scoring.zodiac_sign2 == 'Libra' or zodiac_scoring.zodiac_sign2 == 'Virgo' or
               zodiac_scoring.zodiac_sign2 == 'Capricorn' or zodiac_scoring.zodiac_sign2 == 'Aquarius')): #NN
        main.score -= int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Gemini' or zodiac_scoring.zodiac_sign1 == 'Sagittarius' or zodiac_scoring.zodiac_sign1 == 'Pisces')
          and (zodiac_scoringe.zodiac_sign2 == 'Leo' or zodiac_scoring.zodiac_sign2 == 'Aries')): #NM
        main.score -= int(((40/200)*20)) #final score out of 20%

#WORDS OF AFFIRMATION
if loveLang == "words of affirmation":
    if ((zodiac_scoring.zodiac_sign1 == 'Leo' or zodiac_scoring.zodiac_sign1 == 'Aries')
            and (zodiac_scoring.zodiac_sign2 == 'Leo' or zodiac_scoring.zodiac_sign2 == 'Aries')): #YY
        main.score += int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Leo' or zodiac_scoring.zodiac_sign1 == 'Aries')
          and (zodiac_scoring.zodiac_sign2 == 'Cancer' or zodiac_scoring.zodiac_sign2 == 'Libra' or zodiac_scoring.zodiac_sign2 == 'Virgo' or
               zodiac_scoring.zodiac_sign2 == 'Capricorn' or zodiac_scoring.zodiac_sign2 == 'Aquarius')): #YM
        main.score += int(((40/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Leo' or zodiac_scoring.zodiac_sign1 == 'Aries')
          and (zodiac_scoring.zodiac_sign2 == 'Taurus' or zodiac_scoring.zodiac_sign2 == 'Scorpio')): #NN
        main.score -= int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Leo' or zodiac_scoring.zodiac_sign1 == 'Aries')
          and (zodiac_scoring.zodiac_sign2 == 'Gemini' or zodiac_scoring.zodiac_sign2 == 'Sagittarius' or zodiac_scoring.zodiac_sign2 == 'Pisces')): #NM
        main.score -= int(((40/200)*20)) #final score out of 20%

#ACTS OF SERVICE
if loveLang == "acts of service":
    if ((zodiac_scoring.zodiac_sign1 == 'Cancer' or zodiac_scoring.zodiac_sign1 == 'Libra' or zodiac_scoring.zodiac_sign1 == 'Virgo' or
         zodiac_scoring.zodiac_sign1 == 'Capricorn' or zodiac_scoring.zodiac_sign2 == 'Aquarius')
            and (zodiac_scoring.zodiac_sign2 == 'Cancer' or zodiac_scoring.zodiac_sign2 == 'Libra' or zodiac_scoring.zodiac_sign2 == 'Virgo' or
                 zodiac_scoring.zodiac_sign2 == 'Capricorn' or zodiac_scoring.zodiac_sign2 == 'Aquarius')): #YY
        main.score += int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Cancer' or zodiac_scoring.zodiac_sign1 == 'Libra' or zodiac_scoring.zodiac_sign1 == 'Virgo' or
           zodiac_scoring.zodiac_sign1 == 'Capricorn' or zodiac_scoring.zodiac_sign1 == 'Aquarius')
          and (zodiac_scoring.zodiac_sign2 == 'Leo' or zodiac_scoring.zodiac_sign2 == 'Aries')): #YM
        main.score += int(((40/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Cancer' or zodiac_scoring.zodiac_sign1 == 'Libra' or zodiac_scoring.zodiac_sign1 == 'Virgo' or
           zodiac_scoring.zodiac_sign1 == 'Capricorn' or zodiac_scoring.zodiac_sign1 == 'Aquarius')
          and (zodiac_scoring.zodiac_sign2 == 'Gemini' or zodiac_scoring.zodiac_sign2 == 'Sagittarius' or zodiac_scoring.zodiac_sign2 == 'Pisces')): #NN
        main.score -= int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Cancer' or zodiac_scoring.zodiac_sign1 == 'Libra' or zodiac_scoring.zodiac_sign1 == 'Virgo' or
           zodiac_scoring.zodiac_sign1 == 'Capricorn' or zodiac_scoring.zodiac_sign1 == 'Aquarius')
          and (zodiac_scoring.zodiac_sign2 == 'Taurus' or zodiac_scoring.zodiac_sign2 == 'Scorpio')): #NM
        main.score -= int(((40/200)*20)) #final score out of 20%

#PHYSICAL TOUCH
if loveLang == "physical touch":
    if ((zodiac_scoring.zodiac_sign1 == 'Taurus' or zodiac_scoring.zodiac_sign1 == 'Scorpio')
            and (zodiac_scoring.zodiac_sign2 == 'Taurus' or zodiac_scoring.zodiac_sign2 == 'Scorpio')): #YY
        main.score += int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Taurus' or zodiac_scoring.zodiac_sign1 == 'Scorpio')
          and (zodiac_scoring.zodiac_sign2 == 'Gemini' or zodiac_scoring.zodiac_sign2 == 'Sagittarius' or zodiac_scoring.zodiac_sign2 == 'Pisces')): #YM
        main.score += int(((40/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Taurus' or zodiac_scoring.zodiac_sign1 == 'Scorpio')
          and (zodiac_scoring.zodiac_sign2 == 'Leo' or zodiac_scoring.zodiac_sign2 == 'Aries')): #NN
        main.score -= int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Taurus' or zodiac_scoring.zodiac_sign1 == 'Scorpio')
          and (zodiac_scoring.zodiac_sign2 == 'Cancer' or zodiac_scoring.zodiac_sign2 == 'Libra' or zodiac_scoring.zodiac_sign2 == 'Virgo' or
               zodiac_scoring.zodiac_sign2 == 'Capricorn' or zodiac_scoring.zodiac_sign2 == 'Aquarius')): #NM
        main.score -= int(((40/200)*20)) #final score out of 20%
