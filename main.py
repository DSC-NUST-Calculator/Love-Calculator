#Dont change these codes
print("Welcome to the DSC Love Calculaor")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Your code goes below
#NAME TRUE TEST worth: 20%
name_chk_true = 0
name_chk_love = 0
name_str = name1+name2            #combine both names
name_str = name_str.lower()       #make comined name string into lower case.
name_chk_true += name_str.count("t")
name_chk_true += name_str.count("r")   #count in comined name string for "r"
name_chk_true += name_str.count("u")
name_chk_true += name_str.count("e")

name_chk_love += name_str.count("l")
name_chk_love += name_str.count("o")
name_chk_love += name_str.count("v")
name_chk_love += name_str.count("e")

score = int(str(name_chk_true)+str(name_chk_love))


if score < 10:
    print("You go together like coke and mint")
elif score > 90:
    print("You go together like coke and mint")
elif score >= 40:
    print("you are alright together")
elif score <= 40:
    print("you are alright together")
else:
    print(score)
