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
    def create(ten_tinh):
        conn = get_db_connection()
        cursor = conn.cursor()

        # Lấy ID lớn nhất hiện có
        cursor.execute("SELECT IDTinh FROM TINHTHANH ORDER BY IDTinh DESC LIMIT 1")
        last_id = cursor.fetchone()

        # Sinh ID mới
        if last_id and last_id[0]:  # Nếu có ID cũ
            last_num = int(re.search(r'\d+', last_id[0]).group())  # Lấy số cuối
            new_id = f"TT{last_num + 1:04d}"  # Format ID mới
        else:
            new_id = "TT0001"  # Nếu chưa có dữ liệu, bắt đầu từ TT0001

        try:
            # Thêm tỉnh thành mới với IDTinh sinh ra
            cursor.execute("INSERT INTO TINHTHANH (IDTinh, TenTinh) VALUES (%s, %s)", (new_id, ten_tinh))
            conn.commit()
            return {"message": "Thêm thành công", "IDTinh": new_id, "TenTinh": ten_tinh}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
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
