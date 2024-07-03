import psycopg2

conn = psycopg2.connect(database='homework',
                        user='postgres',host='localhost',password='1234',port='5432')
cursor = conn.cursor()
class Users:
    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

    def get_user(self):
        return f'{self.first_name} {self.last_name} {self.username} {self.email} {self.password}'

    def save_user(self):
        save_query = """
        INSERT INTO Users (first_name, last_name, username, email, password) values (%s, %s, %s, %s, %s)
        """
        cursor.execute(save_query, (self.first_name, self.last_name, self.username, self.email, self.password))
        conn.commit()

    def delete_user(self):
        delete_query = """delete * from Users where username = not_habibulloh"""
        cursor.execute(delete_query, (self.username))
        conn.commit()
        print('User deleted')

    def update_user(self):
        update_query = """update Users set first_name = %s where first_name =Sasha"""
        cursor.execute(update_query, (self.first_name))
        conn.commit()
        print('User updated')


    @staticmethod
    def get_users():
        select_query = """select * from Users"""
        cursor.execute(select_query)
        users = cursor.fetchall()
        for user in users:
            print(user)

print(Users.get_users)