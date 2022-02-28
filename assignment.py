# all crud operation for assignment
from config import get_db_cursor


class Assignment:
    table5 = "tb_assignment"

    def __init__(self):
        pass

    def assignment_option_map(self):
        return {
            1 : self.get_list,
            2 :self.add,
            3: self.update,
            4 :self.delete,
            5: self.get_assignment_by_teacher,
            6: self.get_assignment_by_standard
        }

    def display_option(self):
        print("1. to get_list of all assignments:")
        print("2 add new assignment record:")
        print("3 UPDATE assignment here:")
        print("4 delete assignment here:")
        print("5  get all assignments given by a teacher:")
        print("6 get all the assignment given to a standard:")

        selected_input=int(input("select option:"))
        if selected_input==1:
            name=input("enter the assignment name here:")
            self.assignment_option_map().get(selected_input)(name)

        elif selected_input==3:
            name=input("enter the name you want to update:")
            id=int(input("enter the id where you want to update:"))
            self.assignment_option_map().get(selected_input)(name,id)

        elif selected_input==4:
            name=input("enter the name of the assignment:")
            id=int(input("enter the id where you want to delete the record:"))
            self.assignment_option_map().get(selected_input)(name,id)
        elif selected_input==5:
            teacher_id=int(input("enter the teacher_id ,you want to know the assignments:"))
            self.assignment_option_map().get(selected_input)(teacher_id)
        elif selected_input==6:
            standard_id=int(input("enter the standard_id ,you want to know the assignments:"))
            self.assignment_option_map().get(selected_input)(standard_id)
        else:
            self.assignment_option_map().get(selected_input)

    def get_list(self):
        connection=get_db_cursor()
        cursor=connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table5} ;")
        connection.commit()
        connection.close()
        print("get all the records successfully")

    def add(self,name):
        connection=get_db_cursor()
        cursor=connection.cursor()
        cursor.execute(f"INSERT IN TABLE {self.table5}(name) values('{name}')")
        connection.commit()
        connection.close()
        print("record added successfully")

    def update(self,id,name):
        connection=get_db_cursor()
        cursor=connection.cursor()
        cursor.execute(f" UPDATE {self.table5} SET name = '{name}' WHERE id = {id};")
        connection.commit()
        connection.close()
        print("record deleted successfully")

    def delete(self,id):
        connection=get_db_cursor()
        cursor=connection.cursor()
        cursor.execute(f"DELETE FROM {self.table5} WHERE id={id}")
        connection.commit()
        connection.close()
        print("record deleted successfully")

 #   def associate(self,id,name):
    def get_assignment_by_teacher(self,teacher_id,assignment_id):
        connection=get_db_cursor()
        cursor=connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table5}  WHERE teacher_id={teacher_id}")
        for assignment in cursor.fetchall():
            print(assignment[0])
        connection.commit()
        connection.close()
        print("fetch all records successfully")

    def get_assignment_by_standard(self,standard_id,assignment,id):
        connection=get_db_cursor()
        cursor=connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table5} WHERE standard_id={standard_id}")
        for assignment in cursor.fetchall():
            print(assignment[0])
        connection.commit()
        connection.close()
        print("fetch all record successfully")







