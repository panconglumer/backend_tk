# connection.py
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read environment variables
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Construct the database URL
database_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

try:
    # Connect to the database
    client = psycopg2.connect(database_url)
    db = client.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # ========== CREATE TABLE 'students' ==========

    table_name_students = "students"

    def create_students_table():
        create_students_query = """ 
        CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        no VARCHAR(150) NOT NULL,
        nis VARCHAR(200) NOT NULL,
        nama VARCHAR(200) NOT NULL,
        kelas VARCHAR(100) NOT NULL,       
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        db.execute(create_students_query)
        client.commit()
        print(f"Table '{table_name_students}' created successfully in PostgreSQL ")

    def check_if_students_exists(table_name):
        try:
            db.execute("""
                        SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables
                        WHERE table_catalog = 'postgres'
                        AND table_schema = 'public'
                        AND table_name = %s
                        );
                    """, (table_name,))
            return db.fetchone()[0]
        except psycopg2.Error as e:
            print("Error: ", e)
            return False

    print(f"Table {table_name_students} exists: {check_if_students_exists(table_name_students)}")

    if not check_if_students_exists(table_name_students):
        create_students_table()
    else:
        print(f"Table '{table_name_students}' already exists")

    print(f"Table {table_name_students} exists: {check_if_students_exists(table_name_students)}")
    # ================== End Students =============================

    # ========== CREATE TABLE 'review' ===========================

    table_name_review = "review"

    def create_review_table():
        create_review_query = """ 
        CREATE TABLE IF NOT EXISTS review (
        id SERIAL PRIMARY KEY,
        siswa VARCHAR(150) NOT NULL,
        mapel VARCHAR(150) NOT NULL,
        nilai VARCHAR(120) NOT NULL,
        kemajuan VARCHAR(100) NOT NULL,
        follback VARCHAR(200) NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        db.execute(create_review_query)
        client.commit()
        print(f"Table '{table_name_review}' created successfully in PostgreSQL ")

    def check_if_review_exists(table_name):
        try:
            db.execute("""
                        SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables
                        WHERE table_catalog = 'postgres'
                        AND table_schema = 'public'
                        AND table_name = %s
                        );
                    """, (table_name,))
            return db.fetchone()[0]
        except psycopg2.Error as e:
            print("Error: ", e)
            return False

    print(f"Table {table_name_review} exists: {check_if_review_exists(table_name_review)}")

    if not check_if_review_exists(table_name_review):
        create_review_table()
    else:
        print(f"Table '{table_name_review}' already exists")

    print(f"Table {table_name_review} exists: {check_if_review_exists(table_name_review)}")
    # ================ End Review =================================

    # ========== CREATE TABLE 'kalender' ============================

    table_name_kalender = "kalender"

    def create_kalender_table():
        create_kalender_query = """ 
        CREATE TABLE IF NOT EXISTS kalender (
        id SERIAL PRIMARY KEY,
        tanggal DATE NOT NULL,
        acara VARCHAR(150) NOT NULL,
        keterangan TEXT NOT NULL,        
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        db.execute(create_kalender_query)
        client.commit()
        print(f"Table '{table_name_kalender}' created successfully in PostgreSQL ")

    def check_if_kalender_exists(table_name):
        try:
            db.execute("""
                        SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables
                        WHERE table_catalog = 'postgres'
                        AND table_schema = 'public'
                        AND table_name = %s
                        );
                    """, (table_name,))
            return db.fetchone()[0]
        except psycopg2.Error as e:
            print("Error: ", e)
            return False

    print(f"Table {table_name_kalender} exists: {check_if_kalender_exists(table_name_kalender)}")

    if not check_if_kalender_exists(table_name_kalender):
        create_kalender_table()
    else:
        print(f"Table '{table_name_kalender}' already exists")

    print(f"Table {table_name_kalender} exists: {check_if_kalender_exists(table_name_kalender)}")
    # ================ End Kalender =================================

    # ========== CREATE TABLE 'report' ============================

    table_name_report = "report"

    def create_report_table():
        create_report_query = """ 
        CREATE TABLE IF NOT EXISTS report (
        id SERIAL PRIMARY KEY,
        jenis VARCHAR(150) NOT NULL,
        pesan VARCHAR(200) NOT NULL,
        detail TEXT NOT NULL,             
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        db.execute(create_report_query)
        client.commit()
        print(f"Table '{table_name_report}' created successfully in PostgreSQL ")

    def check_if_report_exists(table_name):
        try:
            db.execute("""
                        SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables
                        WHERE table_catalog = 'postgres'
                        AND table_schema = 'public'
                        AND table_name = %s
                        );
                    """, (table_name,))
            return db.fetchone()[0]
        except psycopg2.Error as e:
            print("Error: ", e)
            return False

    print(f"Table {table_name_report} exists: {check_if_report_exists(table_name_report)}")

    if not check_if_report_exists(table_name_report):
        create_report_table()
    else:
        print(f"Table '{table_name_report}' already exists")

    print(f"Table {table_name_report} exists: {check_if_report_exists(table_name_report)}")
    # ==================== End Report =============================================================

    # ========== CREATE TABLE 'materi' ============================

    table_name_materi = "materi"

    def create_materi_table():
        create_materi_query = """ 
        CREATE TABLE IF NOT EXISTS materi (
        id SERIAL PRIMARY KEY,
        judul VARCHAR(150) NOT NULL,
        mapel VARCHAR(150) NOT NULL,
        tingkat VARCHAR(150) NOT NULL,
        tipe VARCHAR(150) NOT NULL,             
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        db.execute(create_materi_query)
        client.commit()
        print(f"Table '{table_name_materi}' created successfully in PostgreSQL ")

    def check_if_materi_exists(table_name):
        try:
            db.execute("""
                        SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables
                        WHERE table_catalog = 'postgres'
                        AND table_schema = 'public'
                        AND table_name = %s
                        );
                    """, (table_name,))
            return db.fetchone()[0]
        except psycopg2.Error as e:
            print("Error: ", e)
            return False

    print(f"Table {table_name_materi} exists: {check_if_materi_exists(table_name_materi)}")

    if not check_if_materi_exists(table_name_materi):
        create_materi_table()
    else:
        print(f"Table '{table_name_materi}' already exists")

    print(f"Table {table_name_materi} exists: {check_if_materi_exists(table_name_materi)}")

    # ================== End Materi ============================================================

    # ===================== Forum ============================================================

    table_name_forum = "forum"

    def create_forum_table():
        create_forum_query = """ 
        CREATE TABLE IF NOT EXISTS forum (
        id SERIAL PRIMARY KEY,
        pengirim VARCHAR(150) NOT NULL,
        judul VARCHAR(150) NOT NULL,
        pesan VARCHAR(150) NOT NULL,                     
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        db.execute(create_forum_query)
        client.commit()
        print(f"Table '{table_name_forum}' created successfully in PostgreSQL ")

    def check_if_forum_exists(table_name):
        try:
            db.execute("""
                        SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables
                        WHERE table_catalog = 'postgres'
                        AND table_schema = 'public'
                        AND table_name = %s
                        );
                    """, (table_name,))
            return db.fetchone()[0]
        except psycopg2.Error as e:
            print("Error: ", e)
            return False

    print(f"Table {table_name_forum} exists: {check_if_forum_exists(table_name_forum)}")

    if not check_if_forum_exists(table_name_forum):
        create_forum_table()
    else:
        print(f"Table '{table_name_forum}' already exists")

    print(f"Table {table_name_forum} exists: {check_if_forum_exists(table_name_forum)}")

# =================== End Forum ========================================================

# ==================== Users =======================================================

    table_name_users = "users"

    def create_users_table():
        create_users_query = """ 
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(150) NOT NULL,
        username VARCHAR(150) NOT NULL,
        password VARCHAR(255) NOT NULL,                     
        email VARCHAR(150) NOT NULL
        );
        """
        db.execute(create_users_query)
        client.commit()
        print(f"Table '{table_name_users}' created successfully in PostgreSQL ")

    def check_if_users_exists(table_name):
        try:
            db.execute("""
                        SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables
                        WHERE table_catalog = 'postgres'
                        AND table_schema = 'public'
                        AND table_name = %s
                        );
                    """, (table_name,))
            return db.fetchone()[0]
        except psycopg2.Error as e:
            print("Error: ", e)
            return False

    print(f"Table {table_name_users} exists: {check_if_users_exists(table_name_users)}")

    if not check_if_users_exists(table_name_users):
        create_users_table()
    else:
        print(f"Table '{table_name_users}' already exists")

    print(f"Table {table_name_users} exists: {check_if_users_exists(table_name_users)}")
# ==================== End Users ======================================================

# ================== Survei =============================================================

    table_name_survei = "survei"


    def create_survei_table():
        create_survei_query = """ 
                CREATE TABLE IF NOT EXISTS survei (
                id SERIAL PRIMARY KEY,
                nama VARCHAR(150) NOT NULL,
                email VARCHAR(150) NOT NULL,
                penggunaan VARCHAR(255) NOT NULL,                     
                fitur VARCHAR(150) NOT NULL,
                masukan TEXT NOT NULL,
                saran TEXT NOT NULL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
        db.execute(create_survei_query)
        client.commit()
        print(f"Table '{table_name_survei}' created successfully in PostgreSQL ")


    def check_if_survei_exists(table_name):
        try:
            db.execute("""
                                SELECT EXISTS (
                                SELECT 1 FROM information_schema.tables
                                WHERE table_catalog = 'postgres'
                                AND table_schema = 'public'
                                AND table_name = %s
                                );
                            """, (table_name,))
            return db.fetchone()[0]
        except psycopg2.Error as e:
            print("Error: ", e)
            return False


    print(f"Table {table_name_survei} exists: {check_if_survei_exists(table_name_survei)}")

    if not check_if_survei_exists(table_name_survei):
        create_survei_table()
    else:
        print(f"Table '{table_name_survei}' already exists")

    print(f"Table {table_name_survei} exists: {check_if_survei_exists(table_name_survei)}")


except psycopg2.Error as e:
    print("Error connecting to the database:", e)
