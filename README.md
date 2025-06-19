__Structure of modules and packages:__
project/
├── main.py
├── entities/
|   ├── __init__.py
|   ├── Grade.py
|   ├── School.py
|   ├── Subject.py
|   ├── people/
|       ├── __init.py
|       ├── Person.py
|       ├── Student.py
|       ├── Teacher.py
├── exceptions/
|   ├── __init__.py
|   ├──     ValidationException.py
├── inputFuncs/
|   ├── __init__.py
|   ├── functions.py
├── tests/
|   ├── __init__.py
|   ├── BoundaryTests.py
|   ├── FunctionalTests.py
|   ├── IntegrationTests.py
|   ├── TimeExecutionTests.py
|   ├── UnitTests.py
├── README.md


Example execution:
---------------------------
1. Actions with subjects.
2. Actions with teachers.
3. Actions with students.
4. Actions with grades.
5. Actions with export.
6. Actions with import.
7. Generate statistic for grades
8. Exit

Choose action:1

1. Add subject.
2. Edit subject.
3. Find subject.
4. Print all subjects

Choose action: 1

Provide name of the subject: Math

Provide grade from which this subject should be taught: 1

Provide grade till which this subject should be taught: 12

---------------------------

Subject added successfully!
---------------------------
---------------------------

1. Actions with subjects.
2. Actions with teachers.
3. Actions with students.
4. Actions with grades.
5. Actions with export.
6. Actions with import.
7. Generate statistic for grades
8. Exit

Choose action: 1

1. Add subject.
2. Edit subject.
3. Find subject.
4. Print all subjects.
5. 
Choose action: 4

---------------------------

Math: 1-12
---------------------------
---------------------------
1. Actions with subjects.
2. Actions with teachers.
3. Actions with students.
4. Actions with grades.
5. Actions with export.
6. Actions with import.
7. Generate statistic for grades
8. Exit

Choose action: 2

1. Add teacher.
2. Edit teacher.
3. Find teacher.
4. Print all teachers.

Choose action: 1

Provide name of new teacher: Jane

Provide lastname of new teacher: Doe

Provide age of new teacher: 24

Provide salary of new teacher 3000

---------------------------
Teacher added successfully!
---------------------------
---------------------------
1. Actions with subjects.
2. Actions with teachers.
3. Actions with students.
4. Actions with grades.
5. Actions with export.
6. Actions with import.
7. Generate statistic for grades
8. Exit

Choose action: 2

1. Add teacher.
2. Edit teacher.
3. Find teacher.
4. Print all teachers.

Choose action: 4

---------------------------

Doe Jane, 24, 3000.0$
---------------------------
---------------------------
1. Actions with subjects.
2. Actions with teachers.
3. Actions with students.
4. Actions with grades.
5. Actions with export.
6. Actions with import.
7. Generate statistic for grades
8. Exit

Choose action: 3

1. Add student.
2. Edit student.
3. Find student.
4. Print all students.

Choose action: 1

Provide name of new student: John

Provide lastname of new student: Smith

Provide age of new student: 10

Provide year of studying of new student: 4

Do you want to provide grades for him?no

---------------------------

Student added successfully!
---------------------------
---------------------------

1. Actions with subjects.
2. Actions with teachers.
3. Actions with students.
4. Actions with grades.
5. Actions with export.
6. Actions with import.
7. Generate statistic for grades
8. Exit

Choose action: 3

1. Add student.
2. Edit student.
3. Find student.
4. Print all students.

Choose action: 4

---------------------------

Smith John, 10 y.o, 4-th grade
---------------------------
---------------------------

1. Actions with subjects.
2. Actions with teachers.
3. Actions with students.
4. Actions with grades.
5. Actions with export.
6. Actions with import.
7. Generate statistic for grades
8. Exit

Choose action: 8

Bye!