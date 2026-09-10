# Student Marks Report

A simple Python program that calculates the **total marks, average marks, and grade** of students. It also finds the **class average** and identifies the **topper**.

## Features

* Stores student names and marks in a list.
* Calculates the total marks of each student.
* Calculates the average marks of each student.
* Assigns grades based on the average marks.
* Displays a report for all students.
* Calculates the overall class average.
* Identifies the student with the highest average marks.

## Requirements

* Python 3.x
* No external libraries are required.

## Usage

Run the Python program using:

```bash
python filename.py
```

The program automatically processes the student data already stored in the code.

## How It Works

The program contains student data in the following format:

```text
Name, Subject 1, Subject 2, Subject 3
```

For each student, the program:

1. Adds the marks of all three subjects.
2. Calculates the average using:

```text
Average = Total Marks / 3
```

3. Assigns a grade according to the average:

| Average     | Grade |
| ----------- | ----- |
| 90 or above | A     |
| 80–89       | B     |
| 70–79       | C     |
| 60–69       | D     |
| Below 60    | F     |

4. Prints the student's name, total, average, and grade.

## Class Average

After processing all students, the program calculates the **average of all students' averages** and displays it as the class average.

## Topper

The program compares the average marks of all students and identifies the student with the **highest average** as the topper.

## Example

For the given student data, the program calculates:

* Rahul: Total = 258, Average = 86.0, Grade = B
* Priya: Total = 205, Average ≈ 68.33, Grade = D
* Amit: Total = 269, Average ≈ 89.67, Grade = B
* Sneha: Total = 173, Average ≈ 57.67, Grade = F
* Vikram: Total = 249, Average = 83.0, Grade = B

The class average is approximately **76.93**, and **Amit** is the topper with an average of approximately **89.67**.

## Note

The program uses the `math` module, although no function from the module is actually used in the current code.
