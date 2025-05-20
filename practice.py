count = 0
for num in range(1,10):
   if num % 2 == 0:
      count += 1
      print(num)
print(f"We have {count} even numbers.")





def multiply(*numbers):
   total = 1
   for number in numbers:
      total *= number
   return total


print(multiply(2,3,4))