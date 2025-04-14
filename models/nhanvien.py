from config import get_db_connection

class NhanVien:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM NHANVIEN")
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def get_by_id(id_nhanvien):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM NHANVIEN WHERE IDNhanVien = %s", (id_nhanvien,))
        result = cursor.fetchone()
        conn.close()
        return result if result else {"error": "Không tìm thấy nhân viên"}
    
    @staticmethod
    def get_by_name(ten_nhanvien):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM NHANVIEN WHERE HoTen = %s"
        cursor.execute(query, (ten_nhanvien,))
        result = cursor.fetchall()  # Dùng fetchall() vì có thể có nhiều bến xe trùng tên
        conn.close()
        return result

    @staticmethod
    def create(idnhan_vien, ho_ten, sdt, dia_chi, gioi_tinh, cccd, chuc_vu):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO NHANVIEN (IDNhanVien, HoTen, SDT, DiaChi, GioiTinh, CCCD, ChucVu) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (idnhan_vien, ho_ten, sdt, dia_chi, gioi_tinh, cccd, chuc_vu),
            )
            conn.commit()
            return {"message": "Thêm thành công"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()

    @staticmethod
    def update(id_nhanvien, ho_ten, sdt, dia_chi, gioi_tinh, cccd, chuc_vu):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """UPDATE NHANVIEN SET HoTen = %s, SDT = %s, DiaChi = %s, GioiTinh = %s, 
                CCCD = %s, ChucVu = %s WHERE IDNhanVien = %s""",
                (ho_ten, sdt, dia_chi, gioi_tinh, cccd, chuc_vu, id_nhanvien),
            )
            conn.commit()
            return {"message": "Cập nhật thành công"} if cursor.rowcount else {"error": "Không tìm thấy nhân viên"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()

    @staticmethod
    def delete(id_nhanvien):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM NHANVIEN WHERE IDNhanVien = %s", (id_nhanvien,))
            conn.commit()
            return {"message": "Xóa thành công"} if cursor.rowcount else {"error": "Không tìm thấy nhân viên"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()
