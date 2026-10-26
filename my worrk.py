marks = [75,82,90,68,55]
print(marks[1:4]) #prints 82-68, leaving out 55
print(marks[:]) #full copy of the list
print(marks[::2]) #every second item ie 75,90,55

numbers = [12,2,31,4,5,7,6,2]
numbers.remove(2) #only removes the first 2 since it's repeated
print(numbers)
numbers.pop(3)
print(numbers)



marks = []
n = int(input("How many marks? "))

for i in range(n):
    value = int(input("Enter mark: "))
    marks.append(value)

if len(marks) > 0:
    average = sum(marks) / len(marks)
    print("Average:", average)
    print("Highest:", max(marks))
    print("Lowest:", min(marks))
else:
    print("No marks entered.")

def above_fifty(numbers):
    count = 0
    for number in numbers:
        if number > 50:
            count += 1
    return count
my_list = [23,75,48,90,50,62]
result = above_fifty(my_list)
print("numbers above 50: , result")     
