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
    def create(ho_ten, gioi_tinh, cccd, sdt):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO KHACH (HoTen, GioiTinh, CCCD, SDT) VALUES (%s, %s, %s, %s)",
                (ho_ten, gioi_tinh, cccd, sdt),
            )
            conn.commit()
            return {"message": "Thêm thành công", "IDKhach": cursor.lastrowid}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()

    @staticmethod
    def update(id_khach, ho_ten, gioi_tinh, cccd, sdt):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE KHACH SET HoTen = %s, GioiTinh = %s, CCCD = %s, SDT = %s WHERE IDKhach = %s",
                (ho_ten, gioi_tinh, cccd, sdt, id_khach),
            )
            conn.commit()
            return {"message": "Cập nhật thành công"} if cursor.rowcount else {"error": "Không tìm thấy khách"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()

    @staticmethod
    def delete(id_khach):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM KHACH WHERE IDKhach = %s", (id_khach,))
            conn.commit()
            return {"message": "Xóa thành công"} if cursor.rowcount else {"error": "Không tìm thấy khách"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()
