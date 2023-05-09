# By Peter
# 05/09/2023
# Program #1: Final Project
# This program allows the user to edit a student record.

# Import Sqlite3
import sqlite3

# Connect to the database.
conn = sqlite3.connect("student.db")

# Connect to the cursor.
cur = conn.cursor()

# Get a student name from the user.
student_name = input('Enter a student first name: ')

# Get the current price for that product.
cur.execute('''SELECT student_first_name, student_gpa 
From student_info WHERE student_first_name == ?''', [student_name])
results = cur.fetchone()

# Determine if student is in database
if results is not None:
    # Print the current gpa.
    print(f'The current gpa of {results[0]} '
          f'is {results[1]:.2f}')

    # Get the new gpa.
    new_gpa = float(input('Enter the new gpa: '))

    print()

    # Update the price in the Products table.
    cur.execute('''UPDATE student_info SET student_gpa = ? 
    WHERE student_first_name == ?''', (new_gpa, student_name))

    # Commit the changes
    conn.commit()
    print('The gpa was changed.')

    print()

else:
    # Error message.
    print(f'Student {student_name} not found.')

# Show work.
cur.execute('SELECT * FROM student_info')
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection.
conn.close()