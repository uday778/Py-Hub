numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_number_count= 0

for even in numbers:
    if even > 0:
        positive_number_count+=1
print("final count of pos numbers: ",positive_number_count)
