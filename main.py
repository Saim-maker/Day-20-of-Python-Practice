numbers = [10, 20, 30, 40, 50]
input = int(input("Enter the number: "))
for number in numbers:
    if input == number:
        print(f"The number {number} exists in the list!")
        break
else:
    print("The entered number is not in the list!")

numbers = [-5, 10, -2, 8, 0, -7, 12]
count_positive_numbers = 0
count_negative_numbers = 0
count_zeros = 0
for number in numbers:
    if number > 0:
        count_positive_numbers += 1
    elif number == 0:
        count_zeros += 1
    elif number < 0:
        count_negative_numbers = count_negative_numbers + 1
    else:
        print("Number out of range")

print(count_positive_numbers)
print(count_zeros)
print(count_negative_numbers)


numbers = [3,4,5,6,7,8,9]
sum = 0
for number in numbers:
    if number % 3 == 0:
        sum = sum + number
print(sum)

numbers = [1, 2, 3, 4, 5]
reverse_list =[]
for number in range(4,-1,-1):
    reverse_list.append(numbers[number])
print(reverse_list)

