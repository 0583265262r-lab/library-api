import mysql.connector

class DBConnection:
    def __init__(self):
        self.host="localhost"
        self.user="root"
        self.password="secret"
        self.database="library_db"
    def get_connection(self):
        return mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
connection1 = DBConnection()
connection1.get_connection()
def create_tables():
        conn = connection1.get_connection()
        curser = conn.cursor()
        create_table_book = "CREATE TABLE IF NOT EXISTS books (" \
                            "id INT PRIMARY KEY AUTO_INCREMENT," \
                            "title VARCHAR(50) NOT NULL," \
                            "author VARCHAR(50) NOT NULL," \
                            "genre ENUM('Fiction','Non-Fiction','Science','History','Other') NOT NULL," \
                            "available_is BOOLEAN DEFAULT TRUE NOT NULL," \
                            "borrowed_by_member_id INT NULL)"

        create_table_members = "CREATE TABLE IF NOT EXISTS members(" \
                            "id INT PRIMARY KEY AUTO_INCREMENT," \
                            "name VARCHAR(50) NOT NULL," \
                            "email VARCHAR(50) NOT NULL UNIQUE," \
                            "is_active BOOLEAN DEFAULT TRUE NOT NULL," \
                            "total_borrows INT DEFAULT 0)"

        curser.execute(create_table_book)
        curser.execute(create_table_members)
        conn.commit()
        curser.close()
        conn.close()
        return "The tables were created successfully."
    

