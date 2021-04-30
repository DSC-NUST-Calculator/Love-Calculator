import zodiac_scoring

sociability = input("How Social Are you? Are you an: \n Introvert, Extrovert, Ambivert, or Omnivert?")
sociability = sociability.lower()

while sociability not in {"Introvert", "Extrovert", "Ambivert", "Omnivert"}:
    sociability = input("How Social Are you? Are you an: \n Introvert, Extrovert, Ambivert, or Omnivert?")
    sociability =sociability.lower()

# score:
# YY (Most Definitely)  = +60
# YM (Yes-Maybe)        = +40
# NN (Definitely Not)   = -60
# NM (No-Maybe)         = -40

#For Introverts, YY w/ Omniverts, NN w/ Extroverts, YM w/ Introverts and NM w/ Ambiverts
if sociability == "Introvert":
    if ((zodiac_scoring.zodiac_sign1 == 'Capricorn' or zodiac_scoring.zodiac_sign1 == 'Aquarius' or zodiac_scoring.zodiac_sign1 == 'Taurus')
            and (zodiac_scoring.zodiac_sign2 == 'Pisces' or zodiac_scoring.zodiac_sign2 == 'Cancer' or zodiac_scoring.zodiac_sign2 == 'Virgo')): #YY
        main.score += int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Capricorn' or zodiac_scoring.zodiac_sign1 == 'Aquarius' or zodiac_scoring.zodiac_sign1 == 'Taurus')
          and (zodiac_scoring.zodiac_sign2 == 'Capricorn' or zodiac_scoring.zodiac_sign2 == 'Aquarius' or
          zodiac_scoring.zodiac_sign2 == 'Taurus')): #YM
        main.score += int(((40/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Capricorn' or zodiac_scoring.zodiac_sign1 == 'Aquarius' or zodiac_scoring.zodiac_sign1 == 'Taurus')
            and (zodiac_scoring.zodiac_sign2 == 'Gemini' or zodiac_scoring.zodiac_sign2 == 'Libra' or zodiac_scoring.zodiac_sign2 == 'Sagittarius')): #NN
        main.score -= int(((60/200)*20)) #final score out of 20%

    elif (((zodiac_scoring.zodiac_sign1 == 'Capricorn' or zodiac_scoring.zodiac_sign1 == 'Aquarius' or zodiac_scoring.zodiac_sign1 == 'Taurus')
            and (zodiac_scoring.zodiac_sign2 == 'Leo' or zodiac_scoring.zodiac_sign2 == 'Aries' or zodiac_scoring.zodiac_sign2 == 'Scorpio')): #NM
        main.score -= int(((40/200)*20)) #final score out of 20%

#For Extroverts, YY w/ AmbiVerts, NN w/ Introverts, YM w/ Omniverts and NM w/ Extroverts
if sociability == "Extrovert":
    if ((zodiac_scoring.zodiac_sign1 == 'Gemini' or zodiac_scoring.zodiac_sign1 == 'Libra') or
    zodiac_scoring.zodiac_sign1 == 'Sagittarius')
            and (zodiac_scoring.zodiac_sign2 == 'Leo' or zodiac_scoring.zodiac_sign2 == 'Aries' or zodiac_scoring.zodiac_sign2 == 'Scorpio')): #YY
        main.score += int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Gemini' or zodiac_scoring.zodiac_sign1 == 'Libra') or
    zodiac_scoring.zodiac_sign1 == 'Sagittarius')
          and (zodiac_scoring.zodiac_sign2 == 'Pisces' or zodiac_scoring.zodiac_sign2 == 'Cancer' or zodiac_scoring.zodiac_sign2 == 'Virgo')): #YM
        main.score += int(((40/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Gemini' or zodiac_scoring.zodiac_sign1 == 'Libra') or
    zodiac_scoring.zodiac_sign1 == 'Sagittarius')
          and (zodiac_scoring.zodiac_sign2 == 'Capricorn' or zodiac_scoring.zodiac_sign2 == 'Aquarius' or
          zodiac_scoring.zodiac_sign2 == 'Taurus')): #NN
        main.score -= int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Gemini' or zodiac_scoring.zodiac_sign1 == 'Libra') or
    zodiac_scoring.zodiac_sign1 == 'Sagittarius')
          and (zodiac_scoring.zodiac_sign2 == 'Gemini' or zodiac_scoring.zodiac_sign2 == 'Libra' or zodiac_scoring.zodiac_sign2 == 'Sagittarius')): #NM
        main.score -= int(((40/200)*20)) #final score out of 20%

#For Ambiverts, YY w/ Extroverts, YM w/ Omniverts , NM w/ Introverts, and NN Ambiverts
if sociability == "Ambivert":
    if ((zodiac_scoring.zodiac_sign1 == 'Leo' or zodiac_scoring.zodiac_sign1 == 'Aries' or zodiac_scoring.zodiac_sign1 == 'Scorpio')
            and (zodiac_scoring.zodiac_sign2 == 'Gemini' or zodiac_scoring.zodiac_sign2 == 'Libra' or zodiac_scoring.zodiac_sign2 == 'Sagittarius')): #YY
        main.score += int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Leo' or zodiac_scoring.zodiac_sign1 == 'Aries' or zodiac_scoring.zodiac_sign1 == 'Scorpio')
          and (zodiac_scoring.zodiac_sign2 == 'Pisces' or zodiac_scoring.zodiac_sign2 == 'Cancer' or zodiac_scoring.zodiac_sign2 == 'Virgo')): #YM
        main.score += int(((40/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Leo' or zodiac_scoring.zodiac_sign1 == 'Aries' or zodiac_scoring.zodiac_sign1 == 'Scorpio')
          and (zodiac_scoring.zodiac_sign2 == 'Leo' or zodiac_scoring.zodiac_sign2 == 'Aries' or zodiac_scoring.zodiac_sign2 == 'Scorpio')): #NN
        main.score -= int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Leo' or zodiac_scoring.zodiac_sign1 == 'Aries' or zodiac_scoring.zodiac_sign1 == 'Scorpio')
          and (zodiac_scoring.zodiac_sign2 == 'Capricorn' or zodiac_scoring.zodiac_sign2 == 'Aquarius' or
          zodiac_scoring.zodiac_sign2 == 'Taurus')): #NM
        main.score -= int(((40/200)*20)) #final score out of 20%

#For Omniverts, YY w/ Introvert, YM w/ Ambiverts, NM w/ Omniverts, NN w/ Extroverts
if sociability == "Omnivert":
    if ((zodiac_scoring.zodiac_sign1 == 'Pisces' or zodiac_scoring.zodiac_sign1 == 'Cancer') or
    zodiac_scoring.zodiac_sign1 == 'Virgo')
            and (zodiac_scoring.zodiac_sign2 == 'Capricorn' or zodiac_scoring.zodiac_sign2 == 'Aquarius' or
          zodiac_scoring.zodiac_sign2 == 'Taurus')): #YY
        main.score += int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Pisces' or zodiac_scoring.zodiac_sign1 == 'Cancer') or
    zodiac_scoring.zodiac_sign1 == 'Virgo')
          and (zodiac_scoring.zodiac_sign2 == 'Leo' or zodiac_scoring.zodiac_sign2 == 'Aries' or zodiac_scoring.zodiac_sign2 == 'Scorpio')): #YM
        main.score += int(((40/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Pisces' or zodiac_scoring.zodiac_sign1 == 'Cancer') or
    zodiac_scoring.zodiac_sign1 == 'Virgo')
          and (zodiac_scoring.zodiac_sign2 == 'Gemini' or zodiac_scoring.zodiac_sign2 == 'Libra' or zodiac_scoring.zodiac_sign2 == 'Sagittarius')): #NN
        main.score -= int(((60/200)*20)) #final score out of 20%

    elif ((zodiac_scoring.zodiac_sign1 == 'Pisces' or zodiac_scoring.zodiac_sign1 == 'Cancer') or
    zodiac_scoring.zodiac_sign1 == 'Virgo')
          and (zodiac_scoring.zodiac_sign2 == 'Pisces' or zodiac_scoring.zodiac_sign2 == 'Cancer' or zodiac_scoring.zodiac_sign2 == 'Virgo')): #NM
        main.score -= int(((40/200)*20)) #final score out of 20%
