#! python3
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_squares=0
i_sum=0

#sum_of_squares
for i in range(1,101):
    sum_of_squares = sum_of_squares + (i*i)

#square_of_sum
for i in range(1,101):
    i_sum= i_sum+i
    square_of_sum = i_sum*i_sum

print(square_of_sum-sum_of_squares)
# Tutaj pisz swój kod, młody padawanie ;-)
