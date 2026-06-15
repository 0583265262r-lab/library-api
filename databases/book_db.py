from databases.db_connection import *

from databases.member_db import *
connection1 = DBConnection()
memberdb = MemberDB()
class BookDB:
    def __init__(self):
        pass
    
    def create_book(self,data:dict)->None:
        conn = connection1.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO books (title,author, genre)VALUES(%s,%s,%s)"
        val = [val for val in data.values()]
        str_val = ", ".join(val)
        print(val)
        print(str_val)
        cursor.execute(query,val)
        conn.commit()
        conn.close()
        cursor.close()
        return "success"
    
        

        
    def get_all_books(self):
        conn = connection1.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM books"
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close
        cursor.close
        return rows
        
    def get_book_by_id(self,id):
        conn =connection1.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM books WHERE id =%s"
        cursor.execute(sql,(id,))
        row = cursor.fetchone()
        conn.close()
        cursor.close()
        if not row:
            raise f"{ValueError} book not found"
        return row

    def update_book(self,id:int,data:dict):
        # self.get_book_by_id(id)
        conn = connection1.get_connection()
        cursor = conn.cursor(dictionary=True)
        set_parts = []
        for key in data.keys():
            set_parts.append(f"{key}=%s")
        set_keys = ", ".join(set_parts)
        query = f"UPDATE books SET {set_keys} WHERE id = %s"
        values = list(data.values()) + [id]
        cursor.execute(query,values)
        conn.commit()
        changed = cursor.rowcount > 0
        conn.close()
        cursor.close()
        if not changed:
            raise ValueError
        return changed


        
    def set_available(self,id,val,member_id):
        current_book = self.get_book_by_id(id) 
        if not current_book:
            raise "book not found"
        borrowed_books = self.count_borrowed_books(member_id)
        if not val:
            if not current_book["is_available"]:
                raise ValueError("Book isn't available")
            if borrowed_books["count_borrowed_books"] >= 3:
                raise ValueError("Member has reached maximum borrows")
            if not memberdb.get_member_by_id(member_id)["is_active"]:
                raise ValueError("Member is not active")
            borrowing_book = self.update_book(id,{"is_available":val,"borrowed_by_member_id":member_id})
            return borrowing_book
        elif val:
            if not current_book["borrowed_by_member_id"] == member_id:
                raise ValueError("The book is not lent to this member.")
            return_book = self.update_book(id,{"is_available":val,"borrowed_by_member_id":None})
            return return_book
        else:
            raise ValueError

        

        
    def count_total_books(self):
        conn = connection1.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT COUNT(id) AS number_of_books FROM books"
        cursor.execute(query)
        books = cursor.fetchall()
        conn.close()
        cursor.close()
        return books
        
    def count_available(self):
        conn = connection1.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT COUNT(id) AS available_books FROM books WHERE is_available = TRUE"
        cursor.execute(query)
        books = cursor.fetchall()
        conn.close()
        cursor.close()
        return books
        pass
    def count_borrowed_books(self,member_id):
        conn = connection1.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            memberdb.get_member_by_id(member_id)
        
            query = "SELECT COUNT(borrowed_by_member_id) AS count_borrowed_books FROM books WHERE borrowed_by_member_id = %s "
            cursor.execute(query,(member_id,))
            count_borrowed = cursor.fetchone()
            conn.close()
            cursor.close()
            return count_borrowed
        except:
            return (f"{ValueError} member not found")


    
    def count_by_genre(self,genre):
        genres = {'Fiction','Non-Fiction','Science','History','Other'}
        if genre not in genres:
            raise f"{ValueError} genre not exist"
        conn = connection1.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT COUNT(id) AS count FROM books WHERE genre = %s"
        cursor.execute(query,(genre,))
        books = cursor.fetchall()
        conn.close()
        cursor.close()
        return books
        
        
    def count_active_borrows_by_member(self,member_id):
        pass

if __name__ == "__main__":
    c1 = BookDB()
#     c1.update_book(1,{
#   "genre": "Science",
#   "available_is": 0,
#   "borrowed_by_member_id": 1
# })
    # print(c1.count_borrowed_books(6))
    # print(c1.set_available(2,False,6))
    # print(c1.count_available())
    print(c1.count_by_genre("Non-Fiction"))