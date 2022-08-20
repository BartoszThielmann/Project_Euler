#! python3
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

given_number='82166370484403199890008895243450658541227588666881'
largest_sum=0
for i in range(0,len(given_number)-4):
    mult4=1
    for j in range(0,4):
        mult4 = mult4 * int(given_number[i+j])
    if mult4>largest_sum:
        largest_sum = mult4
print(largest_sum)
