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
        query = "SELECT * FROM NHANVIEN WHERE LOWER(HoTen) LIKE %s"
        cursor.execute(query, ("%" + ten_nhanvien.lower() + "%",))  # Dùng LIKE để tìm gần đúng
        result = cursor.fetchall()
        conn.close()
        return result



    # @staticmethod
    # def get_by_name(ten_nhanvien):
    #     conn = get_db_connection()
    #     cursor = conn.cursor(dictionary=True)
    #     query = "SELECT * FROM NHANVIEN WHERE HoTen = %s"
    #     cursor.execute(query, (ten_nhanvien,))
    #     result = cursor.fetchall()  # Dùng fetchall() vì có thể có nhiều bến xe trùng tên
    #     conn.close()
    #     return result
    
    @staticmethod
    def filter_nhanvien(gioi_tinh=None, chuc_vu=None):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM NHANVIEN WHERE 1=1"
        params = []

        if gioi_tinh:
            query += " AND GioiTinh = %s"
            params.append(gioi_tinh)
        if chuc_vu:
            query += " AND ChucVu = %s"
            params.append(chuc_vu)

        cursor.execute(query, tuple(params))
        result = cursor.fetchall()
        conn.close()
        return result

    
    @staticmethod
    def generate_new_id():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT IDNhanVien FROM NHANVIEN WHERE IDNhanVien LIKE 'NV____' ORDER BY IDNhanVien DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()

        if result:
            last_id = result[0]
            number = int(last_id[2:]) + 1   
            new_id = f"NV{str(number).zfill(4)}"
        else:
            new_id = "NV0001"
        return new_id
    
    @staticmethod
    def create(ho_ten, sdt, dia_chi, gioi_tinh, cccd, chuc_vu):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            idnhan_vien = NhanVien.generate_new_id()

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
