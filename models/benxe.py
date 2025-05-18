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
        query = "SELECT * FROM BENXE WHERE idBen = %s"
        cursor.execute(query, (id_ben,))
        result = cursor.fetchone()  # Dùng fetchone() vì chỉ lấy 1 bản ghi
        conn.close()
        return result
    
    @staticmethod
    def get_by_name(ten_ben):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM BENXE WHERE TenBen = %s"
        cursor.execute(query, (ten_ben,))
        result = cursor.fetchall()  # Dùng fetchall() vì có thể có nhiều bến xe trùng tên
        conn.close()
        return result
    
    # tìm kiếm theo tên tỉnh
    @staticmethod
    def get_by_ten_tinh(ten_tinh):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT bx.*
            FROM BENXE bx
            JOIN TINHTHANH t ON bx.IDTinh = t.IDTinh
            WHERE LOWER(t.TenTinh) = LOWER(%s)
        """
        cursor.execute(query, (ten_tinh,))
        result = cursor.fetchall()
        conn.close()
        return result


    @staticmethod
    def generate_new_id():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT IDBen FROM BENXE WHERE IDBen LIKE 'BX____' ORDER BY IDBen DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()

        if result:
            last_id = result[0]  # Ví dụ: 'BX0042'
            number = int(last_id[2:]) + 1  # Lấy số và +1
            new_id = f"BX{str(number).zfill(4)}"  # Thành BX0043
        else:
            new_id = "BX0001"  # Nếu chưa có bản ghi nào
        return new_id

    
    @staticmethod
    def create(ten_ben, dia_chi, sdt, id_tinh):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            id_ben = BenXe.generate_new_id()

            cursor.execute(
                "INSERT INTO BENXE (IDBen, TenBen, DiaChi, SDTBen, IDTinh) VALUES (%s, %s, %s, %s, %s)",
                (id_ben, ten_ben, dia_chi, sdt, id_tinh),
            )
            conn.commit()
            return {"message": "Thêm thành công", "IDBen": id_ben}
        except Exception as e:
            conn.rollback()
            return {"error": str(e)}
        finally:
            conn.close()


    # @staticmethod
    # def create(id_ben, ten_ben, dia_chi, sdt, id_tinh):
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute(
    #             "INSERT INTO BENXE (IDBen, TenBen, DiaChi, SDTBen, IDTinh) VALUES (%s, %s, %s, %s, %s)",
    #             (id_ben, ten_ben, dia_chi, sdt, id_tinh),
    #         )
    #         conn.commit()
    #         return {"message": "Thêm thành công"}
    #     except Exception as e:
    #         conn.rollback()
    #         return {"error": str(e)}
    #     finally:
    #         conn.close()


    # @staticmethod
    # def update(id_ben, ten_ben, dia_chi, sdt, id_tinh):
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute(
    #             "UPDATE BENXE SET IDBen =%s, TenBen = %s, DiaChi = %s, SDT = %s, IDTinh = %s WHERE IDBen = %s",
    #             (ten_ben, dia_chi, sdt, id_tinh, id_ben),
    #         )
    #         conn.commit()
    #         return {"message": "Cập nhật thành công"} if cursor.rowcount else {"error": "Không tìm thấy bến xe"}
    #     except Exception as e:
    #         conn.rollback()
    #         return {"error": str(e)}
    #     finally:
    #         conn.close()
    @staticmethod
    def update(id_ben, ten_ben, dia_chi, sdt, id_tinh):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE BENXE SET TenBen = %s, DiaChi = %s, SDTBen = %s, IDTinh = %s WHERE IDBen = %s",
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
