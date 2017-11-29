#This program says hello and asks for my name

print('Hello mang')
print('What is your name?')

myName = input()
print('Pleased to meet you ' + myName)
print(len(myName))

print('Age?')
age = input()
print('You will be ' + str(int(age) + 1) + ' in a year.')