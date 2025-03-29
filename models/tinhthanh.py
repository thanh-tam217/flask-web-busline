from config import get_db_connection

class TinhThanh:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM TINHTHANH")
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def get_by_id(id_tinh):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM TINHTHANH WHERE IDTinh = %s", (id_tinh,))
        result = cursor.fetchone()
        conn.close()
        return result

    @staticmethod
    def create(ten_tinh):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TINHTHANH (TenTinh) VALUES (%s)", (ten_tinh,))
        conn.commit()
        conn.close()

    @staticmethod
    def update(id_tinh, ten_tinh):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE TINHTHANH SET TenTinh = %s WHERE IDTinh = %s", (ten_tinh, id_tinh))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id_tinh):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM TINHTHANH WHERE IDTinh = %s", (id_tinh,))
        conn.commit()
        conn.close()
