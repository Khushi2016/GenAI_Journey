fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])

fruits.append("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

numbers = [5,1,8,3]
numbers.sort()
print(numbers)

mylist = ['mango','apple','strawberry','watermelon']

for i in mylist:
    print(i.upper())


# Print only divisible by 5 and 3

list = [5,10,15,18,25]
for i in list:
    if i%5==0 and i%3==0:
        print(i)


# Count all values in list.

list1 = [10, 20, 30, 40]
count = 0
for i in list1:
    count += 1
print("Count:", count)

# Print square values of each values . [1,2,3,4] == [1,4,9,16]

list2 = [1,2,3,4]
for i in list2:
   print(i * i)

