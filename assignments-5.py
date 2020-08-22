Assignment - 5 (Fibonacci Numbers)

Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

The desired output is like :

fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

______________________________________________________________________________

fibo = [1,1]

j = 1

for i in range(1,56):

    if i == fibo[j] + fibo[j-1]:

        fibo.append(i)

        j+=1

print(fibo)
