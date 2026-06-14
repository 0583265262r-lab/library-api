from databases.db_connection import *
conn1 = DBConnection()

class MemberDB:
    def __init__(self):
        pass
    def create_member(self,data):
        conn = conn1.get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO members (name ,email) VALUES (%s,%s)"
        val = [val for val in data.values()]
        str_val = ", ".join(val)
        print(val)
        print(str_val)
        cursor.execute(sql,val)
        conn.commit()
        conn.close()
        cursor.close()
        return "success"


        
    def get_all_members():
        conn = conn1.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM members"
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close
        cursor.close
        return rows
    def get_member_by_id(id):
        pass
    def update_member(id,data):
        pass
    def deactivate_member(id):
        pass
    def activate_member(id):
        pass
    def increment_borrows(id):
        pass
    def count_active_members():
        pass
    def get_top_member():
        pass
