from flask import jsonify
from config import get_db_connection

class TuyenXe:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM TUYENXE")
        result = cursor.fetchall()
        conn.close()
        return result
# class TinhThanh:
#     @staticmethod
#     def get_all():
#         conn = get_db_connection()
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute("SELECT * FROM TINHTHANH")
#         result = cursor.fetchall()
#         conn.close()
#         return result
    # @staticmethod
    # def get_by_id(id_tuyenxe):
    #     conn = get_db_connection()
    #     cursor = conn.cursor(dictionary=True)
    #     cursor.execute("SELECT * FROM TUYENXE WHERE IDTuyenXe = %s", (id_tuyenxe,))
    #     result = cursor.fetchone()
    #     conn.close()
    #     return result
        

    @staticmethod
    def create(data):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO TUYENXE (IDTuyenXe, IDDiemDi, TenDiemDi, IDDiemDen, TenDiemDen, TG_DiChuyen, QuangDuong) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (data ['IDTuyenXe'], data['IDDiemDi'], data['TenDiemDi'], data['IDDiemDen'], data['TenDiemDen'], data['TG_DiChuyen'], data['QuangDuong'])
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

    @staticmethod
    def update(id_tuyenxe, data):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """UPDATE TUYENXE 
                 SET IDDiemDi = %s, TenDiemDi = %s, IDDiemDen = %s, TenDiemDen = %s, TG_DiChuyen = %s, QuangDuong = %s 
                 WHERE IDTuyenXe = %s"""
        values = (data['IDDiemDi'], data['TenDiemDi'], data['IDDiemDen'], data['TenDiemDen'], data['TG_DiChuyen'], data['QuangDuong'], id_tuyenxe)
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id_tuyenxe):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM TUYENXE WHERE IDTuyenXe = %s", (id_tuyenxe,))
        conn.commit()
        conn.close()
