## Faça um programa que imprima as tabuadas dos números de 1 a 10.

num = 0

while num<10:
    num += 1
    for n in range(1,11):
        print(num,"x",n,"=",num*n)
