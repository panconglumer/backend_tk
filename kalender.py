# kalender.py
from connection import db, client
import psycopg2


# Get all kalender
def get_kalender():
    try:
        db.execute("SELECT * FROM kalender ORDER BY id ASC")
        print("Got all kalender successfully")
        return db.fetchall()  # [] or [{}, {}, {}]
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

# Create a kalender
def create_kalender(tanggal, acara, keterangan, date):
    try:
        db.execute(
            "INSERT INTO kalender (tanggal, acara, keterangan, date) VALUES (%s, %s, %s, %s)", (tanggal, acara, keterangan, date))
        client.commit()
        print("Created kalender successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  get a kalender by id
def get_kalender_by_id(id):
    try:
        db.execute("SELECT * FROM kalender WHERE id = %s", (id,))
        print("Got kalender by id successfully")
        return db.fetchone()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  update a kalender
def update_kalender_by_id(id, tanggal, acara, keterangan, date):
    try:
        db.execute(
            "UPDATE kalender SET tanggal = %s, acara = %s, keterangan = %s, date = %s WHERE id = %s", (tanggal, acara, keterangan, date, id))
        client.commit()
        print("Updated kalender by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  delete a kalender
def delete_kalender_by_id(id):
    try:
        db.execute("DELETE FROM kalender WHERE id = %s", (id,))
        client.commit()
        print("Deleted kalender by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  Search for a kalender
def search_kalender(search):
    try:
        db.execute(
            "SELECT * FROM kalender WHERE tanggal LIKE %s OR acara LIKE %s OR keterangan LIKE %s OR date LIKE %s", (search, search))
        print("Searched for a kalender successfully")
        return db.fetchall()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


