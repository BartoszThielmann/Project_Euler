#! python3
# even fibonacci numbers
list_of_numbers = [1,2]
even_sum = 0
while True:
    if list_of_numbers[-1]<=4000000:
        list_of_numbers.append(list_of_numbers[-2]+list_of_numbers[-1])
    else:
        break
for index, item in enumerate(list_of_numbers):
    if item%2==0:
        even_sum = even_sum + item
print(even_sum)
