# forum.py
from connection import db, client
import psycopg2


# Get all forum
def get_forum():
    try:
        db.execute("SELECT * FROM forum ORDER BY id ASC")
        print("Got all forum successfully")
        return db.fetchall()  # [] or [{}, {}, {}]
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

# Create a forum
def create_forum(pengirim, judul, pesan, date):
    try:
        db.execute(
            "INSERT INTO forum (pengirim, judul, pesan, date) VALUES (%s, %s, %s, %s)", (pengirim, judul, pesan,  date))
        client.commit()
        print("Created forum successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  get a forum by id
def get_forum_by_id(id):
    try:
        db.execute("SELECT * FROM forum WHERE id = %s", (id,))
        print("Got forum by id successfully")
        return db.fetchone()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  update a forum
def update_forum_by_id(id, pengirim, judul, pesan, date):
    try:
        db.execute(
            "UPDATE forum SET pengirim = %s, judul = %s, pesan = %s,  date = %s WHERE id = %s", (pengirim, judul, pesan, date, id))
        client.commit()
        print("Updated forum by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  delete a forum
def delete_forum_by_id(id):
    try:
        db.execute("DELETE FROM forum WHERE id = %s", (id,))
        client.commit()
        print("Deleted forum by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  Search for a forum
def search_forum(search):
    try:
        db.execute(
            "SELECT * FROM forum WHERE pengirim LIKE %s OR judul LIKE %s OR pesan  LIKE %s OR date LIKE %s", (search, search))
        print("Searched for a forum successfully")
        return db.fetchall()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


