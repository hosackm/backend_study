import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:", check_same_thread=False)
        self.connection.execute(
            "create table users (user_id integer primary key, username text, hashed_password text)")

    def add_user(self, user, hashed_password):
        cursor = self.connection.execute("insert into users(username, hashed_password) values (?, ?)",
                                         (user, hashed_password))
        return cursor.lastrowid

    def get_hashed_pass_by_user_id(self, user_id):
        cursor = self.connection.execute("select hashed_password from users where user_id = ?", (user_id,))
        hashed_password = cursor.fetchone()
        if hashed_password:
            return hashed_password[0]
        return ""

    def get_username_by_user_id(self, user_id):
        cursor = self.connection.execute("select username from users where user_id = ?", (user_id,))
        username = cursor.fetchone()
        if username:
            return username[0]
        return ""

    def get_user_id_by_username(self, username):
        cursor = self.connection.execute("select user_id from users where username = ?", (username,))
        user_id = cursor.fetchone()
        if user_id:
            return user_id[0]
        return None

db = Database()

if __name__ == "__main__":
    db = Database()
    user_id = db.add_user("hello", "fakepassword")
    print(db.get_hashed_pass_by_user_id(user_id))
    print(db.get_username_by_user_id(user_id))
