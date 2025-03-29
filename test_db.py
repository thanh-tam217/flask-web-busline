import mysql.connector
from config import get_db_connection

try:
    conn = get_db_connection()
    if conn.is_connected():
        print("Kết nối MySQL thành công!")
    else:
        print("Kết nối MySQL thất bại!")
    conn.close()
except mysql.connector.Error as err:
    print(f"Lỗi kết nối MySQL: {err}")
