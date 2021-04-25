#Dont change these codes
print("Welcome to the DSC Love Calculaor")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Your code goes below
#NAME TRUE TEST
name_str = name1+name2            #combine both names
name_str = name_str.lower()       #make comined name string into lower case.
name_chk += name_str.count("t")   #count in comined name string for "t"
name_chk += name_str.count("r")   #count in comined name string for "r"
name_chk += name_str.count("u")   #count in comined name string for "u"
name_chk += name_str.count("e")   #count in comined name string for "e"
score += name_chk                 #add to final score

#ZODIC

#EYE COLOR

#HAIR COLOR

#AGE DIFFERENCE



#SCORE OUTPUT (please verify)
if score < 10: #0-9
    print("You go together like coke and mint.")
elif score > 90: #91-100
    print("You go together like coke and mint.")
elif score >= 40: #40-90
    print("You are alright together.")
elif score <= 50: #10-49
    print("You are alright together.")
else:
    print(f"The score: {score}")
