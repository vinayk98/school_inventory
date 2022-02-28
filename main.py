# starting point of the project
from student import Student
from standard import Standard
from teacher import Teacher
from assignment import Assignment

option_map = {
    1: Student().display_option,
    2: Teacher().display_option,
    3: Standard().display_option,
    4: Assignment().display_option
}


def display_option():
    print("welcome to school inventory system")
    print("select your project")
    print("1. student")
    print("2. teacher")
    print("3. standard")
    print("4. assignments")


def option_router():
    selected_option = int(input("enter the option:"))
    return option_map.get(selected_option)()


if __name__ == '__main__':
    display_option()
    option_router()