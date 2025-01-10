import sqlite3

class Database:
    def __init__(self, db_name='users.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
        
    def create_table(self):
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR (20) NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER

            )    
        """)
    def close_connect(self):
        self.connection.close()

class User(Database):
    def __init__(self, db_name='users.db'):
        super().__init__(db_name)
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
    def add_user(self, name,email,age):
        self.cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name,email,age))
        self.connection.commit()
        
    def get_user(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.cursor.fetchone()
    
    def delete_user_by_email(self, email):
        self.cursor.execute("DELETE FROM users WHERE email = ?", (email,))
        self.connection.commit()
        print(f'Пользоваьель  email {email} был удален')

user = User()
user.add_user('Sulsstan','aik7094s70s@gmail.com',134)
user.get_user(3)

class Admin(User):
    def __init__(self, db_name='users.db'):
        super().__init__(db_name)
    
    def add_user(self, name, email, age):
        return super().add_user(name, email, age)

class Customer(User):
    def __init__(self, db_name='users.db'):
        super().__init__(db_name)
    
    def delete_user_by_email(self, email):
        return super().delete_user_by_email(email)
    
    def get_user(self, id):
        return super().get_user(id)
    



    
    


       
        
