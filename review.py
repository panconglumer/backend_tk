# review.py
from connection import db, client
import psycopg2


# Get all review
def get_review():
    try:
        db.execute("SELECT * FROM review ORDER BY id ASC")
        print("Got all Review successfully")
        return db.fetchall()  # [] or [{}, {}, {}]
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

# Create a review
def create_review(siswa, mapel, nilai, kemajuan, follback, date):
    try:
        db.execute(
            "INSERT INTO review (siswa, mapel, nilai, kemajuan, follback, date) VALUES (%s, %s, %s, %s, %s, %s)", (siswa, mapel, nilai, kemajuan, follback, date))
        client.commit()
        print("Created Review successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  get a review by id
def get_review_by_id(id):
    try:
        db.execute("SELECT * FROM review WHERE id = %s", (id,))
        print("Got review by id successfully")
        return db.fetchone()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  update a review
def update_review_by_id(id, siswa, mapel, nilai, kemajuan, follback, date):
    try:
        db.execute(
            "UPDATE review SET siswa = %s, mapel = %s, nilai = %s, kemajuan = %s, follback = %s, date = %s WHERE id = %s", (siswa, mapel, nilai, kemajuan, follback, date, id))
        client.commit()
        print("Updated Review by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  delete a review
def delete_review_by_id(id):
    try:
        db.execute("DELETE FROM review WHERE id = %s", (id,))
        client.commit()
        print("Deleted review by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  Search for a review
def search_review(search):
    try:
        db.execute(
            "SELECT * FROM review WHERE siswa LIKE %s OR mapel LIKE %s OR nilai LIKE %s OR kemajuan LIKE %s OR follback LIKE %s OR date LIKE %s", (search, search))
        print("Searched for a review successfully")
        return db.fetchall()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


