import find_my_zodiac

#Here we edit and make zodiac scoring
date_day1 = int(input("Day of your birth: "))
date_month1 = int(input("Month of your birth (digits): "))

date_day2 = int(input("Day of their birth: "))
date_month2 = int(input("Month of their birth (digits): "))

zodiac_sign1 = find_my_zodiac.zodiac_chk(date_month1, date_day1) #find zodiac for date 1
zodiac_sign2 = find_my_zodiac.zodiac_chk(date_month2, date_day2)#find zodiac for date 2

print(zodiac_sign1)
print(zodiac_sign2)
