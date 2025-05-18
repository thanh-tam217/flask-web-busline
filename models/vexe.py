from config import get_db_connection

class VeXe:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM VEXE")
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def get_by_id(id_ve):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM VEXE WHERE IDVe = %s", (id_ve,))
        result = cursor.fetchone()
        conn.close()
        return result if result else {"error": "Không tìm thấy vé"}

    # @staticmethod
    # def create(id_chuyen, id_khach, id_xe, so_ghe, ngay_dat_ve, gia_ve):
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute(
    #             "INSERT INTO VEXE (IDChuyen, IDKhach, IDXe, SoGhe, NgayDatVe, GiaVe) VALUES (%s, %s, %s, %s, %s, %s)",
    #             (id_chuyen, id_khach, id_xe, so_ghe, ngay_dat_ve, gia_ve),
    #         )
    #         conn.commit()
    #         return {"message": "Thêm thành công", "IDVe": cursor.lastrowid}
    #     except Exception as e:
    #         conn.rollback()
    #         return {"error": str(e)}
    #     finally:
    #         conn.close()

    # @staticmethod
    # def update(id_ve, id_chuyen, id_khach, id_xe, so_ghe, ngay_dat_ve, gia_ve):
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute(
    #             """UPDATE VEXE SET IDChuyen = %s, IDKhach = %s, IDXe = %s, SoGhe = %s, 
    #             NgayDatVe = %s, GiaVe = %s WHERE IDVe = %s""",
    #             (id_chuyen, id_khach, id_xe, so_ghe, ngay_dat_ve, gia_ve, id_ve),
    #         )
    #         conn.commit()
    #         return {"message": "Cập nhật thành công"} if cursor.rowcount else {"error": "Không tìm thấy vé"}
    #     except Exception as e:
    #         conn.rollback()
    #         return {"error": str(e)}
    #     finally:
    #         conn.close()

    @staticmethod
    def delete(id_ve):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM VEXE WHERE IDVe = %s", (id_ve,))
            conn.commit()
            return {"message": "Xóa thành công"} if cursor.rowcount else {"error": "Không tìm thấy vé"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()
