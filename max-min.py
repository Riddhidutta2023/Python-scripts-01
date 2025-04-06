#create an empty list
numbers = []
print("This program will ask for a number and append it to a list until you type 0")
ask_for_input=int(input("type a number: "))
#append the input to the list
numbers.append(ask_for_input)
#ask for input until the user types 0

while ask_for_input != 0:
    ask_for_input=int(input("type a number: "))
    numbers.append(ask_for_input)
numbers.remove(0)
print("The numbers you entered are:")
for number in numbers:
    print(number)

print(max(numbers))
print(min(numbers))