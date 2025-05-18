from config import get_db_connection
import re

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
    def get_by_name(ten_tinh):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM TINHTHANH WHERE TenTinh = %s"
        cursor.execute(query, (ten_tinh,))
        result = cursor.fetchall()  # Dùng fetchall() vì có thể có nhiều bến xe trùng tên
        conn.close()
        return result
        conn.close()

    @staticmethod
    def generate_new_id():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT IDTinh FROM TINHTHANH WHERE IDTinh LIKE 'TT__' ORDER BY IDTinh DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()

        if result:
            last_id = result[0]
            number = int(last_id[2:]) + 1
            new_id = f"TT{str(number).zfill(2)}"
        else:
            new_id = "TT01"  # Nếu chưa có bản ghi nào
        return new_id

    @staticmethod
    def create(ten_tinh):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            id_tinh = TinhThanh.generate_new_id()

            cursor.execute(
                "INSERT INTO TINHTHANH (IDTinh, TenTinh) VALUES (%s, %s)",
                (id_tinh, ten_tinh),
            )
            conn.commit()
            return {"message": "Thêm thành công", "IDTinh": id_tinh}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()

    # @staticmethod
    # def create(id_tinh, ten_tinh):
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute(
    #             "INSERT INTO TINHTHANH (IDTinh, TenTinh) VALUES (%s, %s)",
    #             (id_tinh, ten_tinh),
    #         )
    #         conn.commit()
    #         return {"message": "Thêm thành công"}
    #     except Exception as e:
    #         conn.rollback()
    #         return {"error": str(e)}
    #     finally:
    #         conn.close()

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
