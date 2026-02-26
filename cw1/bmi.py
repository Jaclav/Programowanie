#!/usr/bin/python3

m=float(input("Podaj masę ciała (w kilogramach): "))
h=float(input("Podaj wzrost (w metrach): "))
BMI=m/h**2

print("BMI =",BMI)

if BMI < 18.5:
    print("Niedowaga.")
elif BMI < 25:
    print("Waga prawidłowa.")
elif BMI < 30:
    print("Nadwaga.")
else:
    print("Otyłość.")

