# models.py
from connection import db, client
import psycopg2


# Get all students
def get_students():
    try:
        db.execute("SELECT * FROM students ORDER BY id ASC")
        print("Got all Students successfully")
        return db.fetchall()  # [] or [{}, {}, {}]
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

# Create a students
def create_students(no, nis, nama, kelas, date):
    try:
        db.execute(
            "INSERT INTO students (no, nis, nama, kelas, date) VALUES (%s, %s, %s, %s, %s)", (no, nis, nama, kelas, date))
        client.commit()
        print("Created Students successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  get a students by id
def get_students_by_id(id):
    try:
        db.execute("SELECT * FROM students WHERE id = %s", (id,))
        print("Got Students by id successfully")
        return db.fetchone()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  update a students
def update_students_by_id(id, no, nis, nama, kelas, date):
    try:
        db.execute(
            "UPDATE students SET no = %s, nis = %s, nama = %s, kelas = %s, date = %s WHERE id = %s", (no, nis, nama, kelas, date, id))
        client.commit()
        print("Updated students by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  delete a students
def delete_students_by_id(id):
    try:
        db.execute("DELETE FROM students WHERE id = %s", (id,))
        client.commit()
        print("Deleted students by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  Search for a students
def search_students(search):
    try:
        db.execute(
            "SELECT * FROM students WHERE no LIKE %s OR nis LIKE %s OR nama LIKE %s OR kelas LIKE %s OR date LIKE %s", (search, search))
        print("Searched for a Students successfully")
        return db.fetchall()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False