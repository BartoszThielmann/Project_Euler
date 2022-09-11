#! python3
# what is the sum of the digits of the number 2^1000?

while True:
    power = input('What power would you like to count? Your answer: ')
    try:
        number = 2**int(power)
    except ValueError:
        print('Please input an integer!')
    else:
        break

digit_sum = 0
for digit in str(number):
    digit_sum += int(digit)
print(f'The sum of digits of 2^{power} is {digit_sum}')
