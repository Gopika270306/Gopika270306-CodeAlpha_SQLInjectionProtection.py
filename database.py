import sqlite3

DATABASE = "users.db"


# ---------------------------------
# Create Database Tables
# ---------------------------------

def create_database():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Users Table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Attack Logs Table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attack_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        attack_input TEXT,
        status TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


# ---------------------------------
# Add User
# ---------------------------------

def add_user(username, email, phone, password):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO users
        (username,email,phone,password)
        VALUES(?,?,?,?)
        """,
        (username, email, phone, password))

        conn.commit()
        result = True

    except:

        result = False

    conn.close()

    return result


# ---------------------------------
# Check Login
# ---------------------------------

def login_user(username, password):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE username=? AND password=?
    """,
    (username, password))

    user = cursor.fetchone()

    conn.close()

    return user


# ---------------------------------
# Save Attack Log
# ---------------------------------

def save_attack(attack_input, status, created_at):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO attack_logs
    (attack_input,status,created_at)
    VALUES(?,?,?)
    """,
    (attack_input, status, created_at))

    conn.commit()
    conn.close()


# ---------------------------------
# Get Dashboard Statistics
# ---------------------------------

def get_total_users():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_attacks():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM attack_logs")

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ---------------------------------
# Get Recent Attack Logs
# ---------------------------------

def get_logs():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT attack_input,
           status,
           created_at
    FROM attack_logs
    ORDER BY id DESC
    LIMIT 10
    """)

    logs = cursor.fetchall()

    conn.close()

    return logs


# ---------------------------------
# Get All Attack Logs
# ---------------------------------

def get_all_logs():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM attack_logs
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


# ---------------------------------
# Run Database
# ---------------------------------

if __name__ == "__main__":

    create_database()

    print("Database Created Successfully!")
