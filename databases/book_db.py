from databases.db_connection import get_connection


class BookDB:
    def __init__(self):
        self.conn = get_connection
    
    def create_book(self,data:dict)->None:
        conn =self.conn()
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
        conn =self.conn()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM books"
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close
        cursor.close
        return rows
        
    def get_book_by_id(self,id):
        conn =self.conn()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM books WHERE id =%s"
        cursor.execute(sql,(id,))
        row = cursor.fetchone()
        conn.close()
        cursor.close()
        if not row:
            raise KeyError
        return row

    def update_book(self,id):
        conn =self.conn()
        cursor = conn.cursor(dictionary=True)
        
        pass
    def set_available(self,id,val,member_id):
        pass
    def count_total_books(self):
        pass
    def count_available(self):
        pass
    def count_borrowed_books(self):
        pass
    def count_by_genre(self,genre):
        pass
    def count_active_borrows_by_member(self,member_id):
        pass