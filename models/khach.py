from config import get_db_connection

class Khach:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM KHACH")
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def get_by_id(id_khach):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM KHACH WHERE IDKhach = %s", (id_khach,))
        result = cursor.fetchone()
        conn.close()
        return result if result else {"error": "Không tìm thấy khách"}
    

    @staticmethod
    def get_by_name(ten_khach):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM KHACH WHERE HoTen LIKE %s"
        cursor.execute(query, ('%' + ten_khach + '%',))
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def get_by_gioitinh(gioitinh):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM KHACH WHERE GioiTinh = %s"
        cursor.execute(query, (gioitinh,))
        result = cursor.fetchall()
        conn.close()
        return result

    # @staticmethod
    # def get_by_name(ten_khach):
    #     conn = get_db_connection()
    #     cursor = conn.cursor(dictionary=True)
    #     query = "SELECT * FROM KHACH WHERE HoTen = %s"
    #     cursor.execute(query, (ten_khach,))
    #     result = cursor.fetchall()  # Dùng fetchall() vì có thể có nhiều bến xe trùng tên
    #     conn.close()
    #     return result
    
    # @staticmethod
    # def get_by_gioitinh(gioitinh):
    #     conn = get_db_connection()
    #     cursor = conn.cursor(dictionary=True)
    #     query = "SELECT * FROM KHACH WHERE GioiTinh = %s"
    #     cursor.execute(query, (gioitinh,))
    #     result = cursor.fetchall()  # Dùng fetchall() vì có thể có nhiều bến xe trùng tên
    #     conn.close()
    #     return result
