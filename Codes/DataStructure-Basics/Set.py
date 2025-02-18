unique_numbers = {10,10,20,30,50}

print(unique_numbers)
print(10 in unique_numbers)

unique_numbers.add(50)
print(unique_numbers)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1 & set2)
print(set1,set2)
print(set2 and set1)
print(set1 | set2)

duplicate_list = [1,2,3,4,5,3,4,5,6]
dupicate_list = set(duplicate_list)
print(dupicate_list)