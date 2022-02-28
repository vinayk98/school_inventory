# all crud operation about student
from config import get_db_cursor


class Student:
    table="tb_student"

    def __init__(self):
        pass

    def student_option_map(self):
        return {
            1: self.get_list,
            2: self.add,
            3: self.update,
            4: self.delete,
            5:self.associate,
            6:self.get_student_by_standard
        }

    def display_option(self):
        print("1, see list of students ")
        print("2, add students")
        print("3,update students")
        print("4,delete students")
        print("5 associate standard_id:")
        print("6 getting student by standard:")
        selected_input = int(input("select option:"))
        if selected_input == 2:
            name = input("enter the student name:")
            self.student_option_map().get(selected_input)(name)
        elif selected_input == 3:
            name = input("update the student name:")
            id = int(input("enter id ,where you want to update:"))
            self.student_option_map().get(selected_input)(id,name)
        elif selected_input==4:
            id = int(input("enter id ,where you want to delete:"))
            self.student_option_map().get(selected_input)(id)

        elif selected_input == 5:
            standard_id=int(input("enter the standard_id:"))
            student_id=int(input("enter the student_id:"))



        else:
            self.student_option_map().get(selected_input)()

    def get_list(self):
        connection = get_db_cursor()
        cursor=connection.cursor()
        cursor.execute(f"SELECT * from {self.table}")
        for student in cursor.fetchall():
            print(f"{student[0]}--{student[1]}")
        connection.close()

    def add(self,name):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {self.table}(name) values('{name}')")
        connection.commit()
        connection.close()
        print("successfully added 1 record")

    def update(self,id,name):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f" UPDATE {self.table}  SET name = '{name}' WHERE id = {id}; ")
        connection.commit()
        connection.close()
        print("successfully updated record")

    def delete(self,id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {self.table} WHERE id='{id}';")
        connection.commit()
        connection.close()
        print("successfully delete record")

    def associate(self,standard_id,student_id):
        connection=get_db_cursor()
        cursor=connection.cursor()
        cursor.execute(f"UPDATE {self.table} SET standard_id = {standard_id} WHERE id={student_id}")
        for student in cursor.fetchall():
            pass
        connection.commit()
        connection.close()
        print("record successfully")

    def get_student_by_standard(self,standard_id):
        connection=get_db_cursor()
        cursor=connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE standard_id={standard_id}")
        for student in cursor.fetchall():
            print(student[0])
        connection.commit()
        connection.close()
        print("successfully updated record")






