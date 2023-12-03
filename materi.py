# materi.py
from connection import db, client
import psycopg2


# Get all materi
def get_materi():
    try:
        db.execute("SELECT * FROM materi ORDER BY id ASC")
        print("Got all materi successfully")
        return db.fetchall()  # [] or [{}, {}, {}]
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

# Create a materi
def create_materi(judul, mapel, tingkat, tipe, date):
    try:
        db.execute(
            "INSERT INTO materi (judul, mapel, tingkat, tipe, date) VALUES (%s, %s, %s, %s,%s)", (judul, mapel, tingkat, tipe, date))
        client.commit()
        print("Created materi successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  get a materi by id
def get_materi_by_id(id):
    try:
        db.execute("SELECT * FROM materi WHERE id = %s", (id,))
        print("Got materi by id successfully")
        return db.fetchone()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  update a materi
def update_materi_by_id(id, judul, mapel, tingkat, tipe, date):
    try:
        db.execute(
            "UPDATE materi SET judul = %s, mapel = %s, tingkat = %s, tipe = %s, date = %s WHERE id = %s", (judul, mapel, tingkat, tipe, date, id))
        client.commit()
        print("Updated materi by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  delete a materi
def delete_materi_by_id(id):
    try:
        db.execute("DELETE FROM materi WHERE id = %s", (id,))
        client.commit()
        print("Deleted materi by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  Search for a materi
def search_materi(search):
    try:
        db.execute(
            "SELECT * FROM materi WHERE judul LIKE %s OR mapel LIKE %s OR tingkat LIKE %s OR tipe LIKE %s OR date LIKE %s", (search, search))
        print("Searched for a materi successfully")
        return db.fetchall()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


