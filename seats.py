import numpy as np
from numpy import random

rows = int(input("Enter the number of rows in the classroom: "))
cols = int(input("Enter the number of chairs per row: "))

names = [
    "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah",
    "Ivy", "Jack", "Kenny", "Liam", "Mona", "Nina", "Oscar", "Paul", "Quincy",
    "Rachel", "Sam", "Tina", "Ursula", "Victor", "Wendy", "Xander", "Yvonne", "Zach"
]
names = names[:rows * cols] 

names_array = np.array(names)
random.shuffle(names_array)
seating_chart = names_array.reshape(rows, cols)

max_name_length = max(len(name) for name in names)
col_width = max_name_length + 4  # Padding for spacing

print("\nSeating Chart:\n")

for row in range(rows):
    for col in range(cols):
        print(f"{seating_chart[row, col]:>{col_width}}", end=" ")
    print()
    for col in range(cols):
        print(f"({row},{col})".rjust(col_width), end=" ")
    print()

