number = int(input("Enter the number:"))
if number % 2 == 0:
    oddnumber = number - 1
    formulanumber = (oddnumber+1)/2
else:
    formulanumber = (number+1)/2

sumodd = formulanumber**2
print("Sum of odd numbers:", str(sumodd))

evennumbers = range(2,number,2)
sumeven = 0
a = 0
for i in evennumbers:
    sumeven = i + sumeven
    a+=1
average = sumeven/a
print("average of even numbers:", str(average))

