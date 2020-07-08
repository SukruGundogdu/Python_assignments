Assignment - 3 (Is it Armstrong Number?)

Task:

Find out if a given number is an "Armstrong Number".

An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. Examples :
371 = 33 + 73 + 13;
9474 = 94 + 44 + 74 + 44;
93084 = 95 + 35 + 05 + 85 + 45.

Write a Python program that;
takes a positive integer number from the user,
checks the entered number if it is Armstrong,
consider the negative, float and any entries other than numeric values then display a warning message to the user.

____________________________________________________________

number = input("Bir sayı giriniz: ")
while not number.isdigit():
    print("it is an invalid entry. Don't use non-numeric, float or negative values!")
    number = input("Lütfen tekrar bir sayı giriniz: ")

number_list = list(str(number))
basamak_sayısı = len(list(str(number)))

print(number_list)
print(basamak_sayısı)


i = 0
toplam = 0
while i < basamak_sayısı:
    toplam += int(number_list[i])**basamak_sayısı
    i+=1
if toplam == int(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not Armstrong number")
