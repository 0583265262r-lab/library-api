<!-- שם הפרוייקט -->
   "Library Management System"
<!-- תיאור הפרוייקט -->
     הפרוייקט הזה זה מערכת של ניהול ספרייה המאפשרת למשתמש 
     לנהל את החברים המנויים בספרייה(הוספת חברים , השאלה והחזרת ספרים , והצגת התגובות ) וניהול ספרים(הוספה ומחיקת ספרים)
מבנה תיקיות
library-api/  
│  
├── app/  
│   ├── main.py  
│   ├── database/  
│   │   ├── db_connection.py  
│   │   ├── book_db.py  
│   │   └── member_db.py  
│   ├── routes/  
│   │   ├── book_routes.py  
│   │   ├── member_routes.py  
│   │   └── report_routes.py  
│   └── logs/  
│       └── app.log  
│  
├── README.md  
├── requirements.txt  
└── .gitignore

<!-- טכנולוגיות בשימוש בפרוייקט -->
    - Python
      להרצת הפרוייקט
    - FastAPI
    לייצור ראוטר
    - MySQL
    דאטה בייס
    - Docker
    קונטיינר של mysql

<!-- הקוד ליצירת docker עם MySql -->
    <!-- Pull the MySQL image: -->
        docker pull mysql:latest
    <!-- Run the container -->
        docker run --name library-mysql \
        -e MYSQL_ROOT_PASSWORD=...\
        -e MYSQL_DATABASE=library_db \
        -p 3306:3306 \
        -d mysql:latest

    <!-- Verify it's running -->
        docker ps
    <!-- Connect via MySQL shell -->
        docker exec -it library-mysql mysql -u root -p
    <!-- Useful SQL commands -->
        SHOW DATABASES;
        USE library_db;
        SHOW TABLES;
<!-- Database Information -->
    library_db
<!-- טבלאות -->
   <!-- books -->
   | Column Name | Data Type | Constraints | Description |
   -------------------------------------------------------
   | "id"  | int  | PRIMARY KEY | id of book |
   |-------|------|-------------|------------|
   | "title" | str | NOT NULL, UNIQUE | name of the book|
   |---------|-----|------------------|-----------------|
   | "author" | str | NOT NULL | name of the author |
   |----------|-----|----------|--------------------|
   | "genre" | str | ENUM | genre of the book 
   |         |     |      | in the library     |
   |---------|-----|------|--------------------|
   | "available_is" | bool | NOT NULL | if book available_is |
   ---------------------------------------------------
   | "id_member_by_borrowed" | bool | ? | The ID of the friend holding the book |

   <!-- Table: `members` -->
   | Column Name | Data Type | Constraints | Description |
   -------------------------------------------------------
   | "id"   | int |  PRIMARY KEY | id of the member|
   ----------------------------------------------------
   |  "name" |str | NOT NULL | the name of member |
   ------------------------------------------------
   |  ""email" | str | NUT NULL ,UNIQUE | email adders|
   -----------------------------------------------------
   | "is_active" | bool | NUT NULL | if the member is active |
   ---------------------------------------------------------------
   | "total_borrows" |int | NOT NULL | AUTO_INCREMENT every borrow |
   -----------------------------------------------------------------
<!-- System Rules -->
1. Create a book: User sends genre/author/title — the system adds is_available=True, borrowed_by=NULL
2. genre: must be Fiction / Non-Fiction / Science / History / Other Any other value returns an error
Must be verified both in addition (POST) and in update (PUT)
3. Create a friend: User sends email/name — the system adds True=active_is total_borrows=0
4. email: must be unique — if already exists returns an error
5. Inactive friend: If False=active_is — a book cannot be borrowed
6. Book unavailable: A book that has already been borrowed cannot be borrowed (False=available_is)
7. Maximum books: A friend cannot have more than 3 books at a time
8. Return a book: A book can only be returned if it is borrowed by the same friend who is returning it

               <!-- System Flow -->
<!-- **Server Startup:** -->
   - The server connects to MySQL
   - Creates tables if they don't exist
   - Starts the FastAPI server
<!-- ** OOP - MemberDB** -->
- method `create_member(data)`
   - User sends POST request to `/members` with name and email
   - System validates the email is unique
   - System creates member with `is_active=True` and `total_borrows=0`
   - Returns the created member
- method `get_all_members()`
   - user send GET request to `/members`
   - returns all members
- method `get_member_by_id(id)`
   - user sent GET request `/members/{id}`
   - returns member by id or None
- method `update_member(id,data)`
   - user send PUT request `/members/{id}`
   - system update the data  to member by id 
- method `deactivate_member(id)`
   - user send PUT request to `/members/{id}/deactivate`
   - system update `is_active=False`
- method `activate_member(id)`
   - user send PUT request to `/members/{id}/activate`
   system update `is_active=True`
- method `increment_borrows(id)`
   - user send PUT request PUT `/books/{id}/borrow/{member_id}`
   - system increment the id by 1
- method `count_active_members()`
   - user send GET request `/reports/summary`
   - system counts the number of the members with `is_active=True`
- method `get_top_member()`
   - user send GET request `/reports/top-member`
   -  returns the member with the highest `borrows_total`
<!-- ** OOP - BookDB ** -->
- method `create_book(data)` 
   - User sends POST request to `/books` with title and author and genre
   - System creates book with `available_is=FALSE` and `id_member_by_borrowed=NULL`
   - Returns the created member
- method `get_all_books()` 
   - user send GET request to `/books`
   - returns all books

<!-- **Borrowing a Book:** -->
   - User sends PUT request to `/books/{id}/borrow/      {member_id}`
   - System checks if book exists
   - System checks if member exists and is active
   - System checks if book is available
   - System checks if member has less than 3 books
   - Updates book: `is_available=False`, `borrowed_by_member_id=member_id`
   - Increments member's `total_borrows` by 1
   - Returns success message




















