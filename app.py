import os
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, session
from flask_cors import CORS
from models import create_students, get_students, get_students_by_id, update_students_by_id, delete_students_by_id, search_students
from review import create_review, get_review, get_review_by_id, update_review_by_id, delete_review_by_id, search_review
from kalender import create_kalender, get_kalender, get_kalender_by_id, update_kalender_by_id, delete_kalender_by_id, search_kalender
from report import create_report, get_report, get_report_by_id, update_report_by_id, delete_report_by_id, search_report
from materi import create_materi, get_materi, get_materi_by_id, update_materi_by_id, delete_materi_by_id, search_materi
from forum import create_forum, get_forum, get_forum_by_id, update_forum_by_id, delete_forum_by_id, search_forum
from survei import create_survei, get_survei, get_survei_by_id, update_survei_by_id, delete_survei_by_id, search_survei
from connection import database_url
import psycopg2  # pip install psycopg2
import psycopg2.extras
import re
from werkzeug.security import generate_password_hash, check_password_hash
import configparser




app = Flask(__name__)
app.secret_key = 'your_secret_key'
CORS(app)

# # ================ Survei =====================================
def format_survey(survey):
    return [{
        'id': survei['id'],
        'nama': survei['nama'],
        'email': survei['email'],
        'penggunaan': survei['penggunaan'],
        'fitur': survei['fitur'],
        'masukan': survei['masukan'],
        'saran': survei['saran'],
        'date': survei['date']
    } for survei in survey]


@app.route('/survei', methods=['GET'])
def get_survei_route():
    surv = get_survei()
    new_surv = format_survey(surv)
    return jsonify(new_surv), 200


@app.route('/survei', methods=['POST'])
def create_survei_route():
    data = request.get_json()
    nama = data['nama']
    email = data['email']
    penggunaan = data['penggunaan']
    fitur = data['fitur']
    masukan = data['masukan']
    saran = data['saran']
    date = data['date']
    create_survei(nama, email, penggunaan, fitur, masukan, saran, date)
    return jsonify({'message': 'Survei created successfully'}), 201


@app.route('/survei/<int:id>', methods=['GET'])
def get_survei_by_id_route(id):
    surv = get_survei_by_id(id)
    new_surv = format_survey([surv])
    return jsonify(new_surv), 200


@app.route('/survei/<int:id>', methods=['PUT'])
def update_survei_route(id):
    data = request.get_json()
    nama = data['nama']
    email = data['email']
    penggunaan = data['penggunaan']
    fitur = data['fitur']
    masukan = data['masukan']
    saran = data['saran']
    date = data['date']
    update_survei_by_id(id, nama, email, penggunaan, fitur, masukan, saran, date)
    return jsonify({'message': 'Survei updated successfully'}), 200


@app.route('/survei/<int:id>', methods=['DELETE'])
def delete_survei_route(id):
    delete_survei_by_id(id)
    return jsonify({'message': 'Survei deleted successfully'}), 200


@app.route('/survei/search/<search>', methods=['GET'])
def search_survei_route(search):
    surv = search_survei(search)
    new_surv = format_survey(surv)
    return jsonify(new_surv), 200
# =================== End Survei ==============================

# ================= Students ==========================
def format_students(students):
    return [{
        'id': student['id'],
        'no': student['no'],
        'nis': student['nis'],
        'nama': student['nama'],
        'kelas': student['kelas'],
        'date': student['date']
    } for student in students]

@app.route('/todos', methods=['GET'])
def get_students_route():
    students = get_students()
    new_students = format_students(students)
    return jsonify(new_students), 200

@app.route('/todos', methods=['POST'])
def create_student_route():
    data = request.get_json()
    no = data['no']
    nis = data['nis']
    nama = data['nama']
    kelas = data['kelas']
    date = data['date']
    create_students(no, nis, nama, kelas, date)
    return jsonify({'message': 'Students created successfully'}), 201

@app.route('/todos/<int:id>', methods=['GET'])
def get_student_by_id_route(id):
    student = get_students_by_id(id)
    new_student = format_students([student])
    return jsonify(new_student), 200

@app.route('/todos/<int:id>', methods=['PUT'])
def update_student_route(id):
    data = request.get_json()
    no = data['no']
    nis = data['nis']
    nama = data['nama']
    kelas = data['kelas']
    date = data['date']
    update_students_by_id(id, no, nis, nama, kelas, date)
    return jsonify({'message': 'Students updated successfully'}), 200

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_student_route(id):
    delete_students_by_id(id)
    return jsonify({'message': 'Students deleted successfully'}), 200

@app.route('/todos/search/<search>', methods=['GET'])
def search_student_route(search):
    students = search_students(search)
    new_students = format_students(students)
    return jsonify(new_students), 200

# ================= End Students ================================

# ================= Review ======================================
# Review Routes
def format_reviews(reviews):
    return [{
        'id': review['id'],
        'siswa': review['siswa'],
        'mapel': review['mapel'],
        'nilai': review['nilai'],
        'kemajuan': review['kemajuan'],
        'follback': review['follback'],
        'date': review['date']
    } for review in reviews]

@app.route('/review', methods=['GET'])
def get_review_route():
    reviews = get_review()
    new_reviews = format_reviews(reviews)
    return jsonify(new_reviews), 200

@app.route('/review', methods=['POST'])
def create_review_route():
    data = request.get_json()
    siswa = data['siswa']
    mapel = data['mapel']
    nilai = data['nilai']
    kemajuan = data['kemajuan']
    follback = data['follback']
    date = data['date']
    create_review(siswa, mapel, nilai, kemajuan, follback, date)
    return jsonify({'message': 'Reviews created successfully'}), 201

@app.route('/review/<int:id>', methods=['GET'])
def get_review_by_id_route(id):
    review = get_review_by_id(id)
    new_review = format_reviews([review])
    return jsonify(new_review), 200

@app.route('/review/<int:id>', methods=['PUT'])
def update_review_route(id):
    data = request.get_json()
    siswa = data['siswa']
    mapel = data['mapel']
    nilai = data['nilai']
    kemajuan = data['kemajuan']
    follback = data['follback']
    date = data['date']
    update_review_by_id(id, siswa, mapel, nilai, kemajuan, follback, date)
    return jsonify({'message': 'Review updated successfully'}), 200

@app.route('/review/<int:id>', methods=['DELETE'])
def delete_review_route(id):
    delete_review_by_id(id)
    return jsonify({'message': 'Review deleted successfully'}), 200

@app.route('/review/search/<search>', methods=['GET'])
def search_review_route(search):
    reviews = search_review(search)
    new_reviews = format_reviews(reviews)
    return jsonify(new_reviews), 200
# ======================== End Review ===============================

# ==================== Kalender =====================================
def format_kalenders(kalenders):
    return [{
        'id': kalender['id'],
        'tanggal': kalender['tanggal'],
        'acara': kalender['acara'],
        'keterangan': kalender['keterangan'],
        'date': kalender['date']
    } for kalender in kalenders]

@app.route('/kalender', methods=['GET'])
def get_kalender_route():
    kalenders = get_kalender()
    new_kalenders = format_kalenders(kalenders)
    return jsonify(new_kalenders), 200

@app.route('/kalender', methods=['POST'])
def create_kalender_route():
    data = request.get_json()
    tanggal = data['tanggal']
    acara = data['acara']
    keterangan = data['keterangan']
    date = data['date']
    create_kalender(tanggal, acara, keterangan, date)
    return jsonify({'message': 'kalenders created successfully'}), 201

@app.route('/kalender/<int:id>', methods=['GET'])
def get_kalender_by_id_route(id):
    kalender = get_kalender_by_id(id)
    new_kalender = format_kalenders([kalender])
    return jsonify(new_kalender), 200

@app.route('/kalender/<int:id>', methods=['PUT'])
def update_kalender_route(id):
    data = request.get_json()
    tanggal = data['tanggal']
    acara = data['acara']
    keterangan = data['keterangan']
    date = data['date']
    update_kalender_by_id(id, tanggal, acara, keterangan, date)
    return jsonify({'message': 'kalender updated successfully'}), 200

@app.route('/kalender/<int:id>', methods=['DELETE'])
def delete_kalender_route(id):
    delete_kalender_by_id(id)
    return jsonify({'message': 'kalender deleted successfully'}), 200

@app.route('/kalender/search/<search>', methods=['GET'])
def search_kalender_route(search):
    kalenders = search_kalender(search)
    new_kalenders = format_kalenders(kalenders)
    return jsonify(new_kalenders), 200
# ================= End Kalender =================================

    # ==================== Report =====================================
def format_reports(reports):
    return [{
        'id': report['id'],
        'jenis': report['jenis'],
        'pesan': report['pesan'],
        'detail': report['detail'],
        'date': report['date']
    } for report in reports]

@app.route('/report', methods=['GET'])
def get_report_route():
    reports = get_report()
    new_reports = format_reports(reports)
    return jsonify(new_reports), 200

@app.route('/report', methods=['POST'])
def create_report_route():
    data = request.get_json()
    jenis = data['jenis']
    pesan = data['pesan']
    detail = data['detail']
    date = data['date']
    create_report(jenis, pesan, detail, date)
    return jsonify({'message': 'reports created successfully'}), 201

@app.route('/report/<int:id>', methods=['GET'])
def get_report_by_id_route(id):
    report = get_report_by_id(id)
    new_report = format_reports([report])
    return jsonify(new_report), 200

@app.route('/report/<int:id>', methods=['PUT'])
def update_report_route(id):
    data = request.get_json()
    jenis = data['jenis']
    pesan = data['pesan']
    detail = data['detail']
    date = data['date']
    update_report_by_id(id, jenis, pesan, detail, date)
    return jsonify({'message': 'report updated successfully'}), 200

@app.route('/report/<int:id>', methods=['DELETE'])
def delete_report_route(id):
    delete_report_by_id(id)
    return jsonify({'message': 'report deleted successfully'}), 200

@app.route('/report/search/<search>', methods=['GET'])
def search_report_route(search):
    reports = search_report(search)
    new_reports = format_reports(reports)
    return jsonify(new_reports), 200

# ================= End Report ====================================

# ======== Materi ========================
def format_materis(materis):
    return [{
        'id': materi['id'],
        'judul': materi['judul'],
        'mapel': materi['mapel'],
        'tingkat': materi['tingkat'],
        'tipe': materi['tipe'],
        'date': materi['date']
    } for materi in materis]

@app.route('/materi', methods=['GET'])
def get_materi_route():
    materis = get_materi()
    new_materis = format_materis(materis)
    return jsonify(new_materis), 200

@app.route('/materi', methods=['POST'])
def create_materi_route():
    data = request.get_json()
    judul = data['judul']
    mapel = data['mapel']
    tingkat = data['tingkat']
    tipe = data['tipe']
    date = data['date']
    create_materi(judul, mapel, tingkat, tipe, date)
    return jsonify({'message': 'materi created successfully'}), 201

@app.route('/materi/<int:id>', methods=['GET'])
def get_materi_by_id_route(id):
    materi = get_materi_by_id(id)
    new_materi = format_materis([materi])
    return jsonify(new_materi), 200

@app.route('/materi/<int:id>', methods=['PUT'])
def update_materi_route(id):
    data = request.get_json()
    judul = data['judul']
    mapel = data['mapel']
    tingkat = data['tingkat']
    tipe = data['tipe']
    date = data['date']
    update_materi_by_id(id, judul, mapel, tingkat, tipe, date)
    return jsonify({'message': 'materi updated successfully'}), 200

@app.route('/materi/<int:id>', methods=['DELETE'])
def delete_materi_route(id):
    delete_materi_by_id(id)
    return jsonify({'message': 'materi deleted successfully'}), 200

@app.route('/materi/search/<search>', methods=['GET'])
def search_materi_route(search):
    materis = search_materi(search)
    new_materis = format_materis(materis)
    return jsonify(new_materis), 200

# ============ Forum ======================
def format_forums(forums):
    return [{
        'id': forum['id'],
        'pengirim': forum['pengirim'],
        'judul': forum['judul'],
        'pesan': forum['pesan'],
        'date': forum['date']
    } for forum in forums]

@app.route('/forum', methods=['GET'])
def get_forum_route():
    foru = get_forum()
    new_foru = format_forums(foru)
    return jsonify(new_foru), 200

@app.route('/forum', methods=['POST'])
def create_forum_route():
    data = request.get_json()
    pengirim = data['pengirim']
    judul = data['judul']
    pesan = data['pesan']
    date = data['date']
    create_forum(pengirim, judul, pesan, date)
    return jsonify({'message': 'forums created successfully'}), 201

@app.route('/forum/<int:id>', methods=['GET'])
def get_forum_by_id_route(id):
    foru = get_forum_by_id(id)
    new_foru = format_forums([foru])
    return jsonify(new_foru), 200

@app.route('/forum/<int:id>', methods=['PUT'])
def update_forum_route(id):
    data = request.get_json()
    pengirim = data['pengirim']
    judul = data['judul']
    pesan = data['pesan']
    date = data['date']
    update_forum_by_id(id, pengirim, judul, pesan, date)
    return jsonify({'message': 'forum updated successfully'}), 200

@app.route('/forum/<int:id>', methods=['DELETE'])
def delete_forum_route(id):
    delete_forum_by_id(id)
    return jsonify({'message': 'forum deleted successfully'}), 200

@app.route('/forum/search/<search>', methods=['GET'])
def search_forum_route(search):
    foru = search_forum(search)
    new_foru = format_forums(foru)
    return jsonify(new_foru), 200

# ================ Users ==========================
@app.route('/')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return jsonify({'status': 'success', 'message': 'You are logged in', 'username': session['username']})
    # User is not loggedin redirect to login page
    return jsonify({'status': 'error', 'message': 'User not logged in'})

@app.route('/login/', methods=['POST'])
def login():
    # Check if "username" and "password" POST requests exist (user submitted form)
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        # Create a connection and cursor
        conn = psycopg2.connect(database_url)
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        try:
            # Check if account exists using PostgreSQL
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            # Fetch one record and return result
            account = cursor.fetchone()

            if account:
                password_rs = account['password']
                # If account exists in users table in our database
                if check_password_hash(password_rs, password):
                    # Create session data, we can access this data in other routes
                    session['loggedin'] = True
                    session['id'] = account['id']
                    session['username'] = account['username']
                    # Redirect to home page
                    return jsonify({'status': 'success', 'message': 'Login successful', 'username': account['username']})
                else:
                    # Incorrect username/password
                    return jsonify({'status': 'error', 'message': 'Incorrect username/password'})
            else:
                # Incorrect username/password
                return jsonify({'status': 'error', 'message': 'Incorrect username/password'})

        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

    return jsonify({'status': 'error', 'message': 'Invalid request'})

@app.route('/register', methods=['POST'])
def register():
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        _hashed_password = generate_password_hash(password)

        # Establish a connection
        conn = psycopg2.connect(database_url)

        try:
            # Create a cursor
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            # Check if account exists using PostgreSQL
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            account = cursor.fetchone()

            # If account exists, show error and validation checks
            if account:
                return jsonify({'status': 'error', 'message': 'Account already exists!'})
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                return jsonify({'status': 'error', 'message': 'Invalid email address!'})
            elif not re.match(r'[A-Za-z0-9]+', username):
                return jsonify({'status': 'error', 'message': 'Username must contain only characters and numbers!'})
            elif not username or not password or not email:
                return jsonify({'status': 'error', 'message': 'Please fill out the form!'})
            else:
                # Account doesn't exist and the form data is valid, now insert a new account into the users table
                cursor.execute("INSERT INTO users (fullname, username, password, email) VALUES (%s,%s,%s,%s)",
                               (fullname, username, _hashed_password, email))
                conn.commit()
                return jsonify({'status': 'success', 'message': 'You have successfully registered!'})
        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

    return jsonify({'status': 'error', 'message': 'Invalid request'})

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return jsonify({'status': 'success', 'message': 'Logout successful'})

@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        conn = psycopg2.connect(database_url)
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        try:
            cursor.execute('SELECT * FROM users WHERE id = %s', [session['id']])
            account = cursor.fetchone()
            # Show the profile page with account info
            return jsonify({'status': 'success', 'account': dict(account)})
        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()
    # User is not loggedin redirect to login page
    return jsonify({'status': 'error', 'message': 'User not logged in'})
# ==================== End Users ============================================

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
