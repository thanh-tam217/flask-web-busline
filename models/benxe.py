from config import get_db_connection

class BenXe:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM BENXE")
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def get_by_id(id_ben):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM BENXE WHERE IDBen = %s", (id_ben,))
        result = cursor.fetchone()
        conn.close()
        return result if result else {"error": "Không tìm thấy bến xe"}

    @staticmethod
    def create(ten_ben, dia_chi, sdt, id_tinh):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO BENXE (TenBen, DiaChi, SDT, IDTinh) VALUES (%s, %s, %s, %s)",
                (ten_ben, dia_chi, sdt, id_tinh),
            )
            conn.commit()
            return {"message": "Thêm thành công", "IDBen": cursor.lastrowid}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()

    @staticmethod
    def update(id_ben, ten_ben, dia_chi, sdt, id_tinh):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE BENXE SET TenBen = %s, DiaChi = %s, SDT = %s, IDTinh = %s WHERE IDBen = %s",
                (ten_ben, dia_chi, sdt, id_tinh, id_ben),
            )
            conn.commit()
            return {"message": "Cập nhật thành công"} if cursor.rowcount else {"error": "Không tìm thấy bến xe"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()

    @staticmethod
    def delete(id_ben):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM BENXE WHERE IDBen = %s", (id_ben,))
            conn.commit()
            return {"message": "Xóa thành công"} if cursor.rowcount else {"error": "Không tìm thấy bến xe"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()
