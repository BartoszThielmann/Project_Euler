#! python3
# largest palindrome made from the product of two 3-digit numbers
k=0
for i in range(100,1000):
    for j in range(100,1000):
        if (str(i*j)[0]==str(i*j)[-1] and str(i*j)[1]==str(i*j)[-2] and str(i*j)[2]==str(i*j)[-3] and i*j>int(k)):
            k=str(i*j)
print(k)
