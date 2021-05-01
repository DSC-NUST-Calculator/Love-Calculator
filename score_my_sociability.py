def sociability(zodiac_sign1, zodiac_sign2, sociability_input):
    sociability_score = 0
    #For Introverts, YY w/ Omniverts, NN w/ Extroverts, YM w/ Introverts and NM w/ Ambiverts
    if sociability == "Introvert":
        if ((zodiac_sign1 == 'Capricorn' or zodiac_sign1 == 'Aquarius' or zodiac_sign1 == 'Taurus')
            and (zodiac_sign2 == 'Pisces' or zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Virgo')): #YY
            sociability_score += 60 #final score out of 20%

        elif ((zodiac_sign1 == 'Capricorn' or zodiac_sign1 == 'Aquarius' or zodiac_sign1 == 'Taurus')
              and (zodiac_sign2 == 'Capricorn' or zodiac_sign2 == 'Aquarius' or
              zodiac_sign2 == 'Taurus')): #YM
            sociability_score += 40 #final score out of 20%

        elif ((zodiac_sign1 == 'Capricorn' or zodiac_sign1 == 'Aquarius' or zodiac_sign1 == 'Taurus')
              and (zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Sagittarius')): #NN
            sociability_score -= 60 #final score out of 20%

        elif ((zodiac_sign1 == 'Capricorn' or zodiac_sign1 == 'Aquarius' or zodiac_sign1 == 'Taurus')
              and (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Aries' or zodiac_sign2 == 'Scorpio')): #NM
            sociability_score -= 40 #final score out of 20%

    #For Extroverts, YY w/ AmbiVerts, NN w/ Introverts, YM w/ Omniverts and NM w/ Extroverts
    if sociability == "Extrovert":
        if ((zodiac_sign1 == 'Gemini' or zodiac_sign1 == 'Libra' or zodiac_sign1 == 'Sagittarius')
            and (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Aries' or zodiac_sign2 == 'Scorpio')): #YY
            sociability_score += 60 #final score out of 20%

        elif ((zodiac_sign1 == 'Gemini' or zodiac_sign1 == 'Libra' or zodiac_sign1 == 'Sagittarius')
              and (zodiac_sign2 == 'Pisces' or zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Virgo')): #YM
            sociability_score += 40 #final score out of 20%

        elif ((zodiac_sign1 == 'Gemini' or zodiac_sign1 == 'Libra' or zodiac_sign1 == 'Sagittarius')
              and (zodiac_sign2 == 'Capricorn' or zodiac_sign2 == 'Aquarius' or
              zodiac_sign2 == 'Taurus')): #NN
            sociability_score -= 60 #final score out of 20%

        elif ((zodiac_sign1 == 'Gemini' or zodiac_sign1 == 'Libra' or zodiac_sign1 == 'Sagittarius')
              and (zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Sagittarius')): #NM
            sociability_score -= 40 #final score out of 20%

    #For Ambiverts, YY w/ Extroverts, YM w/ Omniverts , NM w/ Introverts, and NN Ambiverts
    if sociability == "Ambivert":
        if ((zodiac_sign1 == 'Leo' or zodiac_sign1 == 'Aries' or zodiac_sign1 == 'Scorpio')
            and (zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Sagittarius')): #YY
            sociability_score += 60 #final score out of 20%

        elif ((zodiac_sign1 == 'Leo' or zodiac_sign1 == 'Aries' or zodiac_sign1 == 'Scorpio')
              and (zodiac_sign2 == 'Pisces' or zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Virgo')): #YM
            sociability_score += 40 #final score out of 20%

        elif ((zodiac_sign1 == 'Leo' or zodiac_sign1 == 'Aries' or zodiac_sign1 == 'Scorpio')
              and (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Aries' or zodiac_sign2 == 'Scorpio')): #NN
            sociability_score -= 60 #final score out of 20%

        elif ((zodiac_sign1 == 'Leo' or zodiac_sign1 == 'Aries' or zodiac_sign1 == 'Scorpio')
              and (zodiac_sign2 == 'Capricorn' or zodiac_sign2 == 'Aquarius' or
              zodiac_sign2 == 'Taurus')): #NM
            sociability_score -= 40 #final score out of 20%

    #For Omniverts, YY w/ Introvert, YM w/ Ambiverts, NM w/ Omniverts, NN w/ Extroverts
    if sociability == "Omnivert":
        if ((zodiac_sign1 == 'Pisces' or zodiac_sign1 == 'Cancer' or zodiac_sign1 == 'Virgo')
            and (zodiac_sign2 == 'Capricorn' or zodiac_sign2 == 'Aquarius' or
              zodiac_sign2 == 'Taurus')): #YY
            sociability_score += 60 #final score out of 20%

        elif ((zodiac_sign1 == 'Pisces' or zodiac_sign1 == 'Cancer' or zodiac_sign1 == 'Virgo')
              and (zodiac_sign2 == 'Leo' or zodiac_sign2 == 'Aries' or zodiac_sign2 == 'Scorpio')): #YM
            sociability_score += 40 #final score out of 20%

        elif ((zodiac_sign1 == 'Pisces' or zodiac_sign1 == 'Cancer' or zodiac_sign1 == 'Virgo')
              and (zodiac_sign2 == 'Gemini' or zodiac_sign2 == 'Libra' or zodiac_sign2 == 'Sagittarius')): #NN
            sociability_score -= 60 #final score out of 20%

        elif ((zodiac_sign1 == 'Pisces' or zodiac_sign1 == 'Cancer' or zodiac_sign1 == 'Virgo')
              and (zodiac_sign2 == 'Pisces' or zodiac_sign2 == 'Cancer' or zodiac_sign2 == 'Virgo')): #NM
            sociability_score -= 40 #final score out of 20%

    return sociability_score
