Assignment - 1 (if-Statements)

TASK
Lets say you left a message in the past that prints a password you need. To see the password you wrote, you need to enter your name and the program should recognize you.
Write a program that 

Takes the first name from the user and compares it to yours,
Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12",
If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later."
______________________________________________________________________________



name = "Sukru"

your_password = "W@12"

info = input("ilk harfi buyuk digerleri kucuk olacak sekilde isminizi giriniz: ")

if info == name:

    print(f"Hello, {info}! The password is : {your_password}")

else:

    print(f"Hello, {info}! See you later.")
