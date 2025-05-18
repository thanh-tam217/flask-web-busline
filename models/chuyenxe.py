from datetime import datetime, timedelta
from config import get_db_connection
 # type: ignore
class ChuyenXe:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT IDChuyen, IDTaiXe, IDXe, IDTuyenXe, IDBenKhoiHanh, BenKhoiHanh, 
                IDBenDen, BenDen, NgayXuatPhat, 
                TIME_FORMAT(TG_XuatPhat, '%H:%i:%s') AS TG_XuatPhat,
                TIME_FORMAT(TG_DuDen, '%H:%i:%s') AS TG_DuDen, GiaVe
            FROM CHUYENXE
        """)
        result = cursor.fetchall()
        conn.close()
        return result



    @staticmethod
    def get_by_tinhthanh(diem_di, diem_den):
        print(f"Tìm chuyến xe từ tỉnh {diem_di} đến tỉnh {diem_den}")  # Debug
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
                            SELECT CX.*
                            FROM CHUYENXE CX
                            JOIN TUYENXE TX ON CX.IDTuyenXe = TX.IDTuyen
                            WHERE TX.TenDiemDi = %s AND TX.TenDiemDen = %s
                        """
        cursor.execute(query, (diem_di, diem_den))
        result = cursor.fetchall()

        cursor.close()
        conn.close()
        
        return result

        
    @staticmethod
    def get_by_id(id_chuyen):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM CHUYENXE WHERE IDChuyen = %s", (id_chuyen,))
        result = cursor.fetchone()
        conn.close()

        # Chuyển đổi kiểu không serialize được (timedelta hoặc datetime)
        if result:
            for key, value in result.items():
                if isinstance(value, (timedelta, datetime)):
                    result[key] = str(value)  # Hoặc value.strftime("%H:%M:%S") nếu cần định dạng cụ thể

        return result if result else {"error": "Không tìm thấy chuyến xe"}

    


    # @staticmethod
    # def get_by_id(id_chuyen):
    #     conn = get_db_connection()
    #     cursor = conn.cursor(dictionary=True)
    #     cursor.execute("SELECT * FROM CHUYENXE WHERE IDChuyen = %s", (id_chuyen,))
    #     result = cursor.fetchone()
    #     conn.close()
    #     return result if result else {"error": "Không tìm thấy chuyến xe"}

    # @staticmethod
    # def create(id_tai_xe, id_xe, id_tuyen_xe, id_ben_khoi_hanh, ben_khoi_hanh, id_ben_den, ben_den, ngay_xuat_phat, tg_xuat_phat, tg_du_den, gia_ve):
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute(
    #             """INSERT INTO CHUYENXE (IDTaiXe, IDXe, IDTuyenXe, IDBenKhoiHanh, BenKhoiHanh, IDBenDen, BenDen, NgayXuatPhat, TG_XuatPhat, TG_DuDen, GiaVe) 
    #             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
    #             (id_tai_xe, id_xe, id_tuyen_xe, id_ben_khoi_hanh, ben_khoi_hanh, id_ben_den, ben_den, ngay_xuat_phat, tg_xuat_phat, tg_du_den, gia_ve),
    #         )
    #         conn.commit()
    #         return {"message": "Thêm thành công", "IDChuyen": cursor.lastrowid}
    #     except Exception as e:
    #         conn.rollback()
    #         return {"error": str(e)}
    #     finally:
    #         conn.close()

    @staticmethod
    def generate_new_id():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT IDChuyen FROM CHUYENXE WHERE IDChuyen LIKE 'CX____' ORDER BY IDChuyen DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()

        if result:
            last_id = result[0]  # VD: 'CX0012'
            number = int(last_id[2:]) + 1
            new_id = f"CX{str(number).zfill(4)}"
        else:
            new_id = "CX0001"
        return new_id
    
    @staticmethod
    def create_chuyenxe(id_taixe, id_xe, id_tuyenxe, id_benkhoihanh, benkhoihanh, id_benden, benden, tg_xuatphat, tg_duden, gia_ve):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            id_chuyen = ChuyenXe.generate_new_id()
            cursor.execute("""
                INSERT INTO CHUYENXE (IDChuyen, IDTaiXe, IDXe, IDTuyenXe, IDBenKhoiHanh, BenKhoiHanh,
                                    IDBenDen, BenDen, NgayXuatPhat, TG_XuatPhat, TG_DuDen, GiaVe)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NULL, %s, %s, %s)
            """, (id_chuyen, id_taixe, id_xe, id_tuyenxe, id_benkhoihanh, benkhoihanh,
                id_benden, benden, tg_xuatphat, tg_duden, gia_ve))
            conn.commit()
            return {"message": "Thêm chuyến xe thành công", "IDChuyen": id_chuyen}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()



    @staticmethod
    def update(id_chuyen, id_tai_xe, id_xe, id_tuyen_xe, id_ben_khoi_hanh, ben_khoi_hanh, id_ben_den, ben_den, ngay_xuat_phat, tg_xuat_phat, tg_du_den, gia_ve):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """UPDATE CHUYENXE SET IDTaiXe = %s, IDXe = %s, IDTuyenXe = %s, IDBenKhoiHanh = %s, BenKhoiHanh = %s, 
                IDBenDen = %s, BenDen = %s, NgayXuatPhat = %s, TG_XuatPhat = %s, TG_DuDen = %s, GiaVe = %s 
                WHERE IDChuyen = %s""",
                (id_tai_xe, id_xe, id_tuyen_xe, id_ben_khoi_hanh, ben_khoi_hanh, id_ben_den, ben_den, ngay_xuat_phat, tg_xuat_phat, tg_du_den, gia_ve, id_chuyen),
            )
            conn.commit()
            return {"message": "Cập nhật thành công"} if cursor.rowcount else {"error": "Không tìm thấy chuyến xe"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()

    @staticmethod
    def delete(id_chuyen):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM CHUYENXE WHERE IDChuyen = %s", (id_chuyen,))
            conn.commit()
            return {"message": "Xóa thành công"} if cursor.rowcount else {"error": "Không tìm thấy chuyến xe"}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()
