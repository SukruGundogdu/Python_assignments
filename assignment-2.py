Assignment - 2 (Covid-19)


Problem :

Task : Estimating the risk of death from coronavirus. Write a program that;

Takes "Yes" or "No" from the user as an answer to the following questions :

Are you a cigarette addict older than 75 years old? Variable → age

Do you have a severe chronic disease? Variable → chronic

Is your immune system too weak? Variable → immune

Set a logical algorithm using boolean logic operators (and/or) and use if-statements with the given variables in order to print out us a message : "You are in risky group"(if True ) or "You are not in risky group" (if False).

_______________________________________________

<<<<<<< HEAD
age = str(input("Are you a cigarette addict older than 75 years old? (Yes/No) : ")).title().strip()
=======
    age = str(input("Are you a cigarette addict older than 75 years old? (Yes/No) : ")).title().strip()
>>>>>>> 0709d6842e28e43c19d2a4df61d3dfa62abdb611

chronic = str(input("Do you have a severe chronic disease? (Yes/No): ")).title().strip()

immune = str(input("Is your immune system too weak? (Yes/No): ")).title().strip()

risk = age or chronic or immune
if risk == "Yes":

    print("You are in risky group")

else:

    print("You are not in risky gorup")
