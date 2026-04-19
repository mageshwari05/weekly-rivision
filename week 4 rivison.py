string = input("Enter sentence: ")
count = 1
for i in string:
    if i == " ":
        count = count + 1
print("Word count:", count)
string = input("Enter string: ")
count = 0
for i in string:
    if i.lower() in "aeiou":
        count = count + 1
print("Vowel count:", count)
string = input("Enter string: ")
print("Reverse:", string[::-1])
data = input("Enter text: ")
file = open("data.txt", "w")
file.write(data)
file.close()
print("Data written to file")
file = open("data.txt", "r")
print(file.read())
file.close()
import numpy as np
a = np.array([10,20,30,40])
print("Array:", a)
print("Sum:", np.sum(a))
print("Maximum:", np.max(a))
import pandas as pd
data = {
    "Name":["Ram","Sam","Raj"],
    "Marks":[80,90,85]
}
df = pd.DataFrame(data)
print(df)
print("Name column:")
print(df["Name"])
