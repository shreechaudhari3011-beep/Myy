# Project Title: Marks Average Analyzer
# Level: Beginner (No ML)
# Technology: Python, Lists, Basic Math

# Step 1: Input marks
n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

# Step 2: Calculate average
total = 0
for m in marks:
    total = total + m

average = total / n

# Step 3: Find highest & lowest
highest = marks[0]
lowest = marks[0]

for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m

# Step 4: Display result
print("\n===== Marks Analysis Result =====")
print("Marks:", marks)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
