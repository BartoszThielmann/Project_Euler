#! python3
# What is the 10 001st prime number?

list_of_primes=[]
number_checked=1
while len(list_of_primes)<10001:
    number_checked +=1
    print('Number checked:' + str(number_checked))
    pierwsza = True
    for i in range(2,number_checked-1):
        if number_checked%i==0:
            pierwsza = False
            break
    if pierwsza == True:
        list_of_primes.append(number_checked)
print(list_of_primes[-1])
