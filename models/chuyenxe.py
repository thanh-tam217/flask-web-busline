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

    # @staticmethod
    # def get_by_tinhthanh(diem_di, diem_den):
    #     conn = get_db_connection()  # Mở kết nối
    #     cursor = conn.cursor(dictionary=True)
        
    #     cursor.execute("""
    #         SELECT IDChuyen, IDTaiXe, IDXe, IDTuyenXe, IDBenKhoiHanh, BenKhoiHanh, 
    #             IDBenDen, BenDen, NgayXuatPhat, 
    #             TIME_FORMAT(TG_XuatPhat, '%H:%i:%s') AS TG_XuatPhat,
    #             TIME_FORMAT(TG_DuDen, '%H:%i:%s') AS TG_DuDen, GiaVe
    #         FROM CHUYENXE
    #         WHERE IDTuyenXe IN (
    #             SELECT IDTuyenXe FROM TUYENXE 
    #             WHERE IDDiemDi = %s AND IDDiemDen = %s
    #         )
    #     """, (diem_di, diem_den))

    #     result = cursor.fetchall()
    #     conn.close()  # Đóng kết nối sau khi truy vấn
    #     return result

    @staticmethod
    def get_by_tinhthanh(diem_di, diem_den):
        print(f"🔎 Tìm chuyến xe từ tỉnh {diem_di} đến tỉnh {diem_den}")  # Debug
        
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
        return result if result else {"error": "Không tìm thấy chuyến xe"}

    @staticmethod
    def create(id_tai_xe, id_xe, id_tuyen_xe, id_ben_khoi_hanh, ben_khoi_hanh, id_ben_den, ben_den, ngay_xuat_phat, tg_xuat_phat, tg_du_den, gia_ve):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """INSERT INTO CHUYENXE (IDTaiXe, IDXe, IDTuyenXe, IDBenKhoiHanh, BenKhoiHanh, IDBenDen, BenDen, NgayXuatPhat, TG_XuatPhat, TG_DuDen, GiaVe) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (id_tai_xe, id_xe, id_tuyen_xe, id_ben_khoi_hanh, ben_khoi_hanh, id_ben_den, ben_den, ngay_xuat_phat, tg_xuat_phat, tg_du_den, gia_ve),
            )
            conn.commit()
            return {"message": "Thêm thành công", "IDChuyen": cursor.lastrowid}
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
