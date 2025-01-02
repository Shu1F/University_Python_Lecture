# numXs = int(input("How many times should I print the letter X?"))
# toPrint = ""

# while numXs != 0:
#     toPrint = toPrint + "X"
#     numXs = numXs - 1

# print(toPrint)

number = input("Please type 10 integer").split()

number = [int(num) for num in number]

odd_Numbers = []

for num in number:
    if num % 2 == 1:
        odd_Numbers.append(num)

if odd_Numbers:
    max_number = max(odd_Numbers)
    print(f"The largest odd number is: {max_number}")
else:
    print("There are no odd numbers in the input.")
