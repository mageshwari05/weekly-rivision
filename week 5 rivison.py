# Function
def add(a,b):
    return a+b
print("Sum:", add(5,3))

print("------")

# List
a = [1,2,3,4]
print("Sum of list:", sum(a))

print("Max:", max(a))

print("------")

# Dictionary
student = {"name":"Ram","age":20}
for key in student:
    print(key, student[key])

print("------")

# String
s = "learn python"

print("Length:", len(s))
print("Upper:", s.upper())

# Reverse
print("Reverse:", s[::-1])

# Vowel count
count = 0
for i in s:
    if i in "aeiou":
        count += 1
print("Vowels:", count)
