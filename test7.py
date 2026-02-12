#FOR LOOP
import time
for i  in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("HAPPY NEW YEAR!")

# LIST [ ] 
fruits = ["apple", "mango", "orange", "banana", "kiwi"]

print(fruits[3])

fruits.append("coconut")

fruits.remove("apple")

fruits.pop(3)

fruits.clear()


for fruit in fruits:
    print(fruit, end= ",")

#TUPLE ()
fruits = ("apple", "orange", "kiwi","mango")



