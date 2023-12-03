# users.py
from connection import db, client
import psycopg2


# Get all users
def get_users():
    try:
        db.execute("SELECT * FROM users ORDER BY id ASC")
        print("Got all users successfully")
        return db.fetchall()  # [] or [{}, {}, {}]
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

# Create a users
def create_users(fullname, username, password, email):
    try:
        db.execute(
            "INSERT INTO users (fullname, username, password, email) VALUES (%s, %s, %s, %s)", (fullname, username, password,  email))
        client.commit()
        print("Created users successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  get a users by id
def get_users_by_id(id):
    try:
        db.execute("SELECT * FROM users WHERE id = %s", (id,))
        print("Got users by id successfully")
        return db.fetchone()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  update a users
def update_users_by_id(id, fullname, username, password, email):
    try:
        db.execute(
            "UPDATE users SET fullname = %s, username = %s, password = %s,  email = %s WHERE id = %s", (fullname, username, password, email, id))
        client.commit()
        print("Updated users by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  delete a users
def delete_users_by_id(id):
    try:
        db.execute("DELETE FROM users WHERE id = %s", (id,))
        client.commit()
        print("Deleted users by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  Search for a users
def search_users(search):
    try:
        db.execute(
            "SELECT * FROM users WHERE fullname LIKE %s OR username LIKE %s OR password  LIKE %s OR email LIKE %s", (search, search))
        print("Searched for a users successfully")
        return db.fetchall()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False
