from databases.db_connection import *
conn1 = DBConnection()

class MemberDB:
    def __init__(self):
        pass
    def create_member(self,data:dict):
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


        
    def get_all_members(self):
        conn = conn1.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM members"
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close
        cursor.close
        return rows
    def get_member_by_id(self,id:int):
        conn = conn1.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM members WHERE id = %s"
        cursor.execute(query,(id,))
        member = cursor.fetchone()
        conn.close()
        cursor.close()
        if not member:
            raise KeyError
        return member
        

        
    def update_member(self,id:int,data:dict):
        conn = conn1.get_connection()
        cursor = conn.cursor(dictionary=True)
        set_parts = []
        for key in data.keys():
            set_parts.append(f"{key}=%s")
        set_keys = ", ".join(set_parts)
        query = f"UPDATE members SET {set_keys} WHERE id = %s"
        val = list(data.values()) + [id]
        cursor.execute(query,val)
        conn.commit()
        changed = cursor.rowcount > 0
        conn.close()
        cursor.close()
        if not changed:
            raise ValueError
        return changed



    def deactivate_member(self,id):
        pass
    def activate_member(self,id):
        pass
    def increment_borrows(self,id):
        pass
    def count_active_members(self):
        pass
    def get_top_member(self):
        pass
