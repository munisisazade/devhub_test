# Initialize an empty dictionary
grades = {}

# Add students
add_student(grades, "Alice", 85)
add_student(grades, "Bob", 90)
add_student(grades, "Charlie", 78)

# Print the dictionary
print(grades)  
# Output: {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# Remove a student
remove_student(grades, "Bob")
print(grades)  
# Output: {'Alice': 85, 'Charlie': 78}

# Get a grade
print(get_grade(grades, "Alice"))  
# Output: 85
print(get_grade(grades, "David"))  
# Output: None

# Calculate average grade
print(average_grade(grades))  
# Output: 81.5

# Get all students
print(get_all_students(grades))  
# Output: ['Alice', 'Charlie']
