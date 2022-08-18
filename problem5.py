#! python3
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

number = 0
check = False
while not check:
    number +=1
    for i in range(1,21):
        if number%i!=0:
            break
        elif (i==20 and number%i==0):
            check = True
            print(number)
            break
print('Found')
# Tutaj pisz swój kod, młody padawanie ;-)
