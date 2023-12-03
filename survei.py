# survei.py
from connection import db, client
import psycopg2


# Get all survei
def get_survei():
    try:
        db.execute("SELECT * FROM survei ORDER BY id ASC")
        print("Got all survei successfully")
        return db.fetchall()  # [] or [{}, {}, {}]
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

# Create a survei
def create_survei(nama, email, penggunaan, fitur, masukan, saran, date):
    try:
        db.execute(
            "INSERT INTO survei (nama, email, penggunaan, fitur, masukan, saran, date) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nama, email, penggunaan, fitur, masukan, saran, date))
        client.commit()
        print("Created survei successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  get a survei by id
def get_survei_by_id(id):
    try:
        db.execute("SELECT * FROM survei WHERE id = %s", (id,))
        print("Got survei by id successfully")
        return db.fetchone()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  update a survei
def update_survei_by_id(id, nama, email, penggunaan, fitur, masukan, saran, date):
    try:
        db.execute(
            "UPDATE survei SET nama = %s, email = %s, penggunaan = %s, fitur = %s, masukan = %s, saran = %s, date = %s WHERE id = %s", (nama, email, penggunaan, fitur, masukan, saran, date, id))
        client.commit()
        print("Updated survei by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  delete a survei
def delete_survei_by_id(id):
    try:
        db.execute("DELETE FROM survei WHERE id = %s", (id,))
        client.commit()
        print("Deleted survei by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  Search for a survei
def search_survei(search):
    try:
        db.execute(
            "SELECT * FROM survei WHERE nama LIKE %s OR email LIKE %s OR penggunaan  LIKE %s OR fitur LIKE %s OR masukan LIKE %s OR saran LIKE %s OR date LIKE %s", (search, search))
        print("Searched for a survei successfully")
        return db.fetchall()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


