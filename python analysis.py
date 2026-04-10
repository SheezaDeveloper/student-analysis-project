import pandas as pd

# Load data
data = pd.read_csv("students.csv")

# Show data
print("Student Data:\n", data)

# Average marks
avg = data["Marks"].mean()
print("\nAverage Marks:", avg)

# Highest marks
max_marks = data["Marks"].max()
print("Highest Marks:", max_marks)

# Pass/Fail
data["Result"] = data["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("\nFinal Data:\n", data)