from config import get_db_connection

class Xe:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM XE")
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def get_by_id(id_xe):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM XE WHERE IDXe = %s", (id_xe,))
        result = cursor.fetchone()
        conn.close()
        return result if result else {"error": "Không tìm thấy xe"}
    
    @staticmethod
    def get_by_name(ten_xe):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM XE WHERE LoaiXe = %s"
        cursor.execute(query, (ten_xe,))
        result = cursor.fetchall()  # Dùng fetchall() vì có thể có nhiều bến xe trùng tên
        conn.close()
        return result
    
    # @staticmethod
    # def get_by_trangthai(trangthai):
    #     conn = get_db_connection()
    #     cursor = conn.cursor(dictionary=True)
    #     query = "SELECT * FROM XE WHERE TrangThai = %s"
    #     cursor.execute(query, (trangthai,))
    #     result = cursor.fetchall()  # Dùng fetchall() vì có thể có nhiều bến xe trùng tên
    #     conn.close()
    #     return result

    @staticmethod
    def generate_new_id():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT IDXe FROM XE WHERE IDXe LIKE 'XE____' ORDER BY IDXe DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()

        if result:
            last_id = result[0]
            number = int(last_id[2:]) + 1
            new_id = f"XE{str(number).zfill(4)}"  # Định dạng lại ID với 4 chữ số
        else:
            new_id = "XE0001"
        return new_id
    
    @staticmethod
    def create(bien_so, loai_xe, so_ghe, trang_thai):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            id_xe = Xe.generate_new_id()  # Tạo ID mới

            cursor.execute(
                "INSERT INTO XE (IDXe, BienSo, LoaiXe, SoGhe, TrangThai) VALUES (%s, %s, %s, %s, %s)",
                (id_xe, bien_so, loai_xe, so_ghe, trang_thai),
            )
            conn.commit()
            return {"message": "Thêm thành công"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()


    @staticmethod
    def update(id_xe, bien_so, loai_xe, so_ghe, trang_thai):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE XE SET BienSo = %s, LoaiXe = %s, SoGhe = %s, TrangThai = %s WHERE IDXe = %s",
                (bien_so, loai_xe, so_ghe, trang_thai, id_xe),
            )
            conn.commit()
            return {"message": "Cập nhật thành công"} if cursor.rowcount else {"error": "Không tìm thấy xe"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()

    @staticmethod
    def delete(id_xe):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM XE WHERE IDXe = %s", (id_xe,))
            conn.commit()
            return {"message": "Xóa thành công"} if cursor.rowcount else {"error": "Không tìm thấy xe"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()


    @staticmethod
    def search_by_bien_so(keyword):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM XE WHERE BienSo LIKE %s"
        cursor.execute(query, ('%' + keyword + '%',))
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def filter_by_loai_xe(loai_xe):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM XE WHERE LoaiXe = %s"
        cursor.execute(query, (loai_xe,))
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def filter_by_trang_thai(trang_thai):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM XE WHERE TrangThai = %s"
        cursor.execute(query, (trang_thai,))
        result = cursor.fetchall()
        conn.close()
        return result
