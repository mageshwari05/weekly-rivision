import pandas as pd

print("PANDAS DATA HANDLING")

# Create DataFrame
data = {
    "Name": ["Ram", "Sam", "Raj", "Ravi"],
    "Marks": [80, 90, 85, 70],
    "Age": [20, 21, 22, 23]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("------")

# Select column
print("Names:")
print(df["Name"])

print("------")

# Filter data (Marks > 80)
print("Marks > 80:")
print(df[df["Marks"] > 80])

print("------")

# Add new column
df["Grade"] = ["A", "A", "B", "C"]
print("After adding column:")
print(df)

print("------")

# Basic info
print("Info:")
print(df.info())
