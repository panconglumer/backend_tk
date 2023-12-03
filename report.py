# report.py
from connection import db, client
import psycopg2


# Get all report
def get_report():
    try:
        db.execute("SELECT * FROM report ORDER BY id ASC")
        print("Got all report successfully")
        return db.fetchall()  # [] or [{}, {}, {}]
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

# Create a report
def create_report(jenis, pesan, detail, date):
    try:
        db.execute(
            "INSERT INTO report (jenis, pesan, detail, date) VALUES (%s, %s, %s, %s)", (jenis, pesan, detail, date))
        client.commit()
        print("Created report successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  get a report by id
def get_report_by_id(id):
    try:
        db.execute("SELECT * FROM report WHERE id = %s", (id,))
        print("Got report by id successfully")
        return db.fetchone()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  update a report
def update_report_by_id(id, jenis, pesan, detail, date):
    try:
        db.execute(
            "UPDATE report SET jenis = %s, pesan = %s, detail = %s, date = %s WHERE id = %s", (jenis, pesan, detail, date, id))
        client.commit()
        print("Updated report by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


#  delete a report
def delete_report_by_id(id):
    try:
        db.execute("DELETE FROM report WHERE id = %s", (id,))
        client.commit()
        print("Deleted report by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False

#  Search for a report
def search_report(search):
    try:
        db.execute(
            "SELECT * FROM report WHERE jenis LIKE %s OR pesan LIKE %s OR detail LIKE %s OR date LIKE %s", (search, search))
        print("Searched for a report successfully")
        return db.fetchall()
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


