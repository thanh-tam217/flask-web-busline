from flask import Flask, jsonify, request
from flask import Flask, render_template

from config import get_db_connection
from models.chuyenxe import ChuyenXe

from routes.tuyenxe import tuyenxe_bp
from routes.tinhthanh import tinhthanh_bp
from routes.benxe import benxe_bp
from routes.xe import xe_bp
from routes.chuyenxe import chuyenxe_bp
from routes.khach import khach_bp
from routes.vexe import vexe_bp
from routes.nhanvien import nhanvien_bp


app = Flask(__name__, template_folder='templates')

# Đăng ký các route
app.register_blueprint(tuyenxe_bp)
app.register_blueprint(tinhthanh_bp)
app.register_blueprint(benxe_bp)
app.register_blueprint(xe_bp)
app.register_blueprint(chuyenxe_bp)
app.register_blueprint(khach_bp)
app.register_blueprint(vexe_bp)
app.register_blueprint(nhanvien_bp)


@app.route('/danhsach_tinhthanh')
def show_tinhthanh():
    return render_template('tinhthanh.html')

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/api/tentinhthanh', methods=['GET'])
def get_tinhthanh():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT TenTinh FROM TINHTHANH")
    tinhthanh_list = cursor.fetchall()
    conn.close()
    return jsonify(tinhthanh_list)

@app.route('/timkiem_chuyenxe')
def timkiem_chuyenxe():
    diem_di = request.args.get('diem_di', "").strip()
    diem_den = request.args.get('diem_den', "").strip()

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Truy vấn lấy IDTuyen từ bảng TUYENXE
    cursor.execute("""
        SELECT IDTuyenXe FROM TUYENXE
        WHERE TenDiemDi = %s AND TenDiemDen = %s
    """, (diem_di, diem_den))
    tuyen = cursor.fetchone()


    # if not tuyen:  # Nếu không tìm thấy tuyến xe phù hợp
    #     return render_template("ketqua.html", chuyen_xe_list=[])

    id_tuyen = tuyen["IDTuyenXe"]

    # Truy vấn lấy dữ liệu từ bảng CHUYENXE
    # cursor.execute("""
    #     SELECT cx.IDChuyen, bx1.TenBen AS BenKhoiHanh, bx2.TenBen AS BenDen, 
    #            cx.NgayXuatPhat, cx.TG_XuatPhat, cx.GiaVe
    #     FROM CHUYENXE cx
    #     JOIN BENXE bx1 ON cx.IDBenKhoiHanh = bx1.IDBen
    #     JOIN BENXE bx2 ON cx.IDBenDen = bx2.IDBen
    #     WHERE cx.IDTuyenXe = %s
    # """, (str(id_tuyen),))
    cursor.execute("""
        SELECT cx.TG_XuatPhat, bx1.TenBen AS BenKhoiHanh, 
               cx.TG_DuDen, bx2.TenBen AS BenDen, cx.GiaVe
        FROM CHUYENXE cx
        JOIN BENXE bx1 ON cx.IDBenKhoiHanh = bx1.IDBen
        JOIN BENXE bx2 ON cx.IDBenDen = bx2.IDBen
        WHERE cx.IDTuyenXe = %s
    """, (str(id_tuyen),))


    chuyen_xe_list = cursor.fetchall()

    conn.close()

    return render_template("ketqua.html", chuyen_xe_list=chuyen_xe_list)

if __name__ == "__main__":
    app.run(debug=True)
