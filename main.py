from School import School
from people.Student import Student
from people.Teacher import Teacher


def main():
    school = School("First school", "address")
    school.people = [Student("Test", "Test2", 12, 2, []), Teacher("Test3", "Test4", 19, 1000)]
    print(school.getAllStudents())


if __name__ == "__main__":
    main()
