
# print("Hello, This is the program")
# print('New Year', 2024, sep= '! ')
# fName = input("Enter your first name: ")
# lName = input("Enter your last name: ")
# email = input("Enter your email: ")
# address = input("Enter your address: ")
# gender = input("Enter your gender:  ")
# print("----------------------------------")
# print("My name is :" + fName + "" + lName)
# print("Email:"+ email + "", end =" ")
# print("Address:"+ address)
# print("Gender:" + gender)
# print("----------------------------------")
#special operator

# message = "Hello World "
# print("d"  in message)
# print("Hellow" in message)

# y1 = 5
# y2 = 5
# print(y1 is y2)
# print(y1 is not y2)

# number = float(input("Enter a number: "))
#
# if number >0:
#     print("Positive number")
# elif number==0:
#     print("Natural Number")
# elif number < 0:
#     print("Negative number")
# else:
#     print("Not found ")
#     if number >= 0:
#         if number == 0:
#             print("Zero")
#         else:
#             print("Number is positive")


# def main():
#     i = int(input("Enter a number: "))
#     max= 100
#     while (i < max):
#         print(i)
#         i = i+2
# main()

# age = input("Enter your age: ")
# if int(age) < 18:
#     print("Your age is less than 18")
# elif int(age) >= 18:
#     print("Your age is greater than 18")
# else:
#     print("Your age is less than 18")

# price = input("Enter your price: ")
# if float(price) >= 10:
#     ticket_price = 10
# else:
#     ticket_price = 5
#     print(f"Your price is {ticket_price}")

# price = input("Enter the price: ")
# ticket_price = 20 if float(price) >= 100 else 30
# print(f" this price is {ticket_price}")


# for index in range(500):
#     print(index)
# loop with start and stop
# for index in range(20,40):
#     print(index)

# for index in range(0,12,5):
#     print(index)

# sum = 1
# for index in range(1000):
#     sum += index
#     print(sum)

# number = 1000
#
# sum = number * ( number-1)/2
# print(sum)


#using while loop in code
# max = 40
# counter = 0
# while counter < max:
#     print(counter)
#     counter += 4

#using while loop to input string
while True:
       command = input('>')
       print(command)
       if command.lower() == 'stop':
           break
