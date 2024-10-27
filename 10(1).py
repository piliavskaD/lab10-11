file = open("filesn.txt", "r")

numbers = []

for i in file:
    word = i.split(",")
    #print(word)
    for num in word:
        numbers.append(num[3:])
    #print(numbers)

numbers.sort()
print(f"Sorted list: {numbers}")


kyivstar_num = []
other_num = []

for num in numbers:
    if num.startswith("097"):
        kyivstar_num.append(num)
    else:
        other_num.append(num)

print()
print(f"Kyivstar operators which part starts with '097': {kyivstar_num}")
print(f"Numbers of Kyivstar with part of '097': {len(kyivstar_num)}")
print()
print(f"Other operators: {other_num}")


sorted_file = open("sorted_list.txt", "w")
sorted_file.write("\n".join(numbers))

kyivstar_num_file = open("kyivstar_list.txt", "w")
kyivstar_num_file.write("\n".join(kyivstar_num))

other_num_file = open("other_num_list.txt", "w")
other_num_file.write("\n".join(other_num))

file.close()
