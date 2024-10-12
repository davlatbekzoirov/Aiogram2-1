# import sqlite3
# from contextlib import contextmanager

# class Database:
#     def __init__(self, path_to_db="main.db"):
#         self.path_to_db = path_to_db

#     @contextmanager
#     def connection(self):
#         conn = sqlite3.connect(self.path_to_db)
#         try:
#             yield conn
#         finally:
#             conn.close()

#     def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
#         if not parameters:
#             parameters = ()
#         with self.connection() as conn:
#             cursor = conn.cursor()
#             data = None
#             cursor.execute(sql, parameters)

#             if commit:
#                 conn.commit()
#             if fetchall:
#                 data = cursor.fetchall()
#             if fetchone:
#                 data = cursor.fetchone()
#         return data

#     def create_table_users(self):
#         sql = """
#         CREATE TABLE IF NOT EXISTS Users (
#             id INTEGER PRIMARY KEY,
#             referral_code TEXT,
#             referral_link TEXT
#         );
#         """
#         self.execute(sql, commit=True)

#     def create_table_messages(self):
#         sql = """
#         CREATE TABLE IF NOT EXISTS Messages (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER,
#             referrer_id INTEGER,
#             message TEXT,
#             FOREIGN KEY (user_id) REFERENCES Users (id),
#             FOREIGN KEY (referrer_id) REFERENCES Users (id)
#         );
#         """
#         self.execute(sql, commit=True)

#     def add_user(self, id: int, referral_code: str):
#         sql = """
#         INSERT INTO Users(id, referral_code) VALUES(?, ?)
#         """
#         self.execute(sql, parameters=(id, referral_code), commit=True)

#     def select_user(self, **kwargs):
#         sql = "SELECT * FROM Users WHERE "
#         sql, parameters = self.format_args(sql, kwargs)
#         return self.execute(sql, parameters=parameters, fetchone=True)

#     def add_user_message(self, user_id: int, referrer_id: int, messages: list):
#         sql = """
#         INSERT INTO Messages(user_id, referrer_id, message) VALUES(?, ?, ?)
#         """
#         for message in messages:
#             self.execute(sql, parameters=(user_id, referrer_id, message), commit=True)

#     def select_user_message(self, user_id: int):
#         sql = "SELECT * FROM Messages WHERE user_id = ?"
#         return self.execute(sql, parameters=(user_id,), fetchone=True)

#     def format_args(self, sql, parameters: dict):
#         sql += " AND ".join([
#             f"{item} = ?" for item in parameters
#         ])
#         return sql, tuple(parameters.values())

import sqlite3
from contextlib import contextmanager

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @contextmanager
    def connection(self):
        conn = sqlite3.connect(self.path_to_db)
        try:
            yield conn
        finally:
            conn.close()

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        with self.connection() as conn:
            cursor = conn.cursor()
            data = None
            cursor.execute(sql, parameters)

            if commit:
                conn.commit()
            if fetchall:
                data = cursor.fetchall()
            if fetchone:
                data = cursor.fetchone()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            referral_code TEXT,
            referral_link TEXT
        );
        """
        self.execute(sql, commit=True)

    def create_table_messages(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            referrer_id INTEGER,
            message TEXT,
            FOREIGN KEY (user_id) REFERENCES Users (id),
            FOREIGN KEY (referrer_id) REFERENCES Users (id)
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, referral_code: str):
        sql = """
        INSERT INTO Users(id, referral_code) VALUES(?, ?)
        """
        self.execute(sql, parameters=(id, referral_code), commit=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def add_user_message(self, user_id: int, referrer_id: int, message: str):
        sql = """
        INSERT INTO Messages(user_id, referrer_id, message) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(user_id, referrer_id, message), commit=True)

    def select_user_messages(self, user_id: int):
        sql = "SELECT * FROM Messages WHERE user_id = ?"
        return self.execute(sql, parameters=(user_id,), fetchall=True)

    def get_user_ids(self):
        sql = "SELECT id FROM Users"
        return [row[0] for row in self.execute(sql, fetchall=True)]

    def get_referrer_id(self, user_id):
        sql = "SELECT referrer_id FROM Messages WHERE user_id = ?"
        result = self.execute(sql, parameters=(user_id,), fetchone=True)
        return result[0] if result else None

    def update_user(self, id: int, referral_code: str):
        sql = """
        UPDATE Users
        SET referral_code = ?
        WHERE id = ?
        """
        self.execute(sql, parameters=(referral_code, id), commit=True)
    
    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)[0]

    def format_args(self, sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
