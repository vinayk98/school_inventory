# utilities for teacher table

from config import get_db_cursor


class Teacher:
    table1 = "tb_teacher"
    table4="tb_teacher_standard"

    def __init__(self):
        pass

    def teacher_option_map(self):
        return {
            1: self.get_list,
            2: self.add,
            3: self.update,
            4: self.delete,
            5: self.get_teacher_by_standard,
            6:self.add_teacher
        }

    def display_option(self):
        print("1,see list of teacher")
        print("2,add  teacher")
        print("3,update  teacher")
        print("4,delete  teacher")
        print("5,fetch teacher teach which standard")
        print("6 add teacher_standard:")
        selected_input = int(input("enter the option:"))
        if selected_input == 2:
            name = input("enter the student name:")
            self.teacher_option_map().get(selected_input)(name)
        elif selected_input == 3:
            name = input("enter name of teacher you want to update:")
            id = int(input("enter id ,which record you want to delete:"))
            self.teacher_option_map().get(selected_input)(id,name)
        elif selected_input == 4:
            id = int(input("enter id ,which record you want to delete:"))
            self.teacher_option_map().get(selected_input)(id)
        elif selected_input == 5:
            teacher_id=int(input("enter the teacher_id you want to know the standards:"))
            self.teacher_option_map().get(selected_input)(teacher_id)
        elif selected_input==6:
            teacher_id=int(input("enter the teacher_id :"))
            standard_id=int(input("enter the standard_id:"))
            self.teacher_option_map().get(selected_input)(teacher_id,standard_id)
        else:
            self.teacher_option_map().get(selected_input)()

    def get_list(self):
        connection = get_db_cursor()
        cursor=connection.cursor()
        cursor.execute(f"SELECT * from {self.table1}")
        for teacher in cursor.fetchall():
            print(f"{teacher[0]}--{teacher[1]}")
        connection.close()

    def add(self, name):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {self.table1}(name) values('{name}')")
        connection.commit()
        connection.close()
        print("successfully added 1 record")

    def update(self, id, name):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {self.table1}  SET name = '{name}' WHERE id = {id}; ")
        connection.commit()
        connection.close()
        print("successfully updated record")

    def delete(self, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {self.table1} WHERE id = {id};")
        connection.commit()
        connection.close()
        print("record deleted successfully")

    def add_teacher(self,teacher_id,standard_id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {self.table4} (teacher_id ,standard_id) values({teacher_id},{standard_id})")
        connection.commit()
        connection.close()
        print("add record successfully")

    def get_teacher_by_standard(self,teacher_id):
        connection=get_db_cursor()
        cursor=connection.cursor()
        cursor.execute(f"SELECT standard_id  FROM {self.table4} WHERE teacher_id={teacher_id} ; ")
        for teacher in cursor.fetchall():
            print(teacher[0])
        connection.commit()
        connection.close()
        print("fetch record successfully")



