import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",      # Thay đổi nếu có mật khẩu
        password="",      # Thay đổi nếu có mật khẩu
        database="da2buslineweb" # Tên cơ sở dữ liệu
    )
