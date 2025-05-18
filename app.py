from flask import Flask, jsonify, redirect, request, session, url_for
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

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/admin.html')
def admin():
    return render_template('admin.html')

@app.route('/nvbanve.html')
def nvbanve():
    return render_template('nvbanve.html')

@app.route('/api/tentinhthanh', methods=['GET'])
def get_tinhthanh():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT TenTinh FROM TINHTHANH")
    tinhthanh_list = cursor.fetchall()
    conn.close()
    return jsonify(tinhthanh_list)

# @app.route('/admin.html#benxe')
# def get_benxe():
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM BENXE")
#     benxe_list = cursor.fetchall()
#     conn.close()
#     return render_template('admin.html', benxe_list=benxe_list)

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
    id_tuyen = tuyen["IDTuyenXe"]
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



@app.route('/api/chuyenxe/search')
def api_search_chuyenxe_json():
    diem_di = request.args.get('diem_di', "").strip()
    diem_den = request.args.get('diem_den', "").strip()

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT IDTuyenXe FROM TUYENXE
        WHERE TenDiemDi = %s AND TenDiemDen = %s
    """, (diem_di, diem_den))
    tuyen = cursor.fetchone()
    # cursor.fetchall()

    if not tuyen:
        conn.close()
        return jsonify([])

    id_tuyen = tuyen["IDTuyenXe"]

    cursor.close()
    cursor = conn.cursor(dictionary=True)


    cursor.execute("""
        SELECT cx.IDChuyen, cx.IDTaiXe, cx.IDXe, cx.IDTuyenXe,
               bx1.TenBen AS BenKhoiHanh, bx2.TenBen AS BenDen,
               cx.TG_XuatPhat, cx.TG_DuDen, cx.GiaVe
        FROM CHUYENXE cx
        JOIN BENXE bx1 ON cx.IDBenKhoiHanh = bx1.IDBen
        JOIN BENXE bx2 ON cx.IDBenDen = bx2.IDBen
        WHERE cx.IDTuyenXe = %s
    """, (str(id_tuyen),))
    
    chuyen_xe_list = cursor.fetchall()
    conn.close()
    from datetime import timedelta

    for chuyen in chuyen_xe_list:
        if isinstance(chuyen["TG_XuatPhat"], timedelta):
            chuyen["TG_XuatPhat"] = str(chuyen["TG_XuatPhat"])
        if isinstance(chuyen["TG_DuDen"], timedelta):
            chuyen["TG_DuDen"] = str(chuyen["TG_DuDen"])

    return jsonify(chuyen_xe_list)


@app.route("/logout")
def logout():
    return redirect(url_for("homePage"))

if __name__ == "__main__":
    app.run(debug=True)
