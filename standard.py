# all crud operation about standard
from config import get_db_cursor


class Standard:
    table2 = "tb_standard"

    def __init__(self):
        pass

    def standard_option_map(self):
        return {
            1:self.get_list,
            2:self.add,
            3:self.update,
            4:self.delete,
            5:self.associate
        }

    def display_option(self):
        print("1,see list of standard")
        print("2,add  standard")
        print("3,update  standard")
        print("4,delete  standard")
        selected_input = int(input("enter the option:"))
        if selected_input == 2:
            name = input("enter the standard:")
            self.standard_option_map().get(selected_input)(name)
        elif selected_input == 3:
            name = input("enter the standard :")
            id = int(input("enter id where you want to update record:"))
            self.standard_option_map().get(selected_input)(id,name)
        elif selected_input == 4:
            id = int(input("enter id ,which record you want to delete:"))
            self.standard_option_map().get(selected_input)(id)
        else:
            self.standard_option_map().get(selected_input)()

    def get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table2}")
        for standard in cursor.fetchall():
            print(f"{standard[0]}---{standard[1]}")
        connection.close()

    def add(self, name):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {self.table2}(name) values('{name}')")
        connection.commit()
        connection.close()
        print("successfully added 1 record")

    def update(self,id,name):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {self.table2}  SET name = '{name}' WHERE id = {id}; ")
        connection.commit()
        connection.close()
        print("successfully updated record")

    def delete(self, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {self.table2} WHERE id={id};")
        connection.commit()
        connection.close()
        print("record deleted successfully")

    def associate(self,student_id,standard_id):
        connection=get_db_cursor()
        cursor=connection.cursor()
        cursor.execute(f"UPDATE {self.table2} SET student_id={student_id} WHERE standard_id={standard_id}")
        for standard in cursor.fetchall():
            pass
        connection.commit()
        connection.close()
        print("fetch the record successfully")









