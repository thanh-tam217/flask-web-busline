from flask import Blueprint, request, jsonify
from models.chuyenxe import ChuyenXe


chuyenxe_bp = Blueprint("chuyenxe_bp", __name__)

@chuyenxe_bp.route("/chuyenxe", methods=["GET"])
def get_all_chuyenxe():
    return jsonify(ChuyenXe.get_all())

@chuyenxe_bp.route("/chuyenxe/<string:id_chuyen>", methods=["GET"])
def get_chuyenxe_by_id(id_chuyen):
    return jsonify(ChuyenXe.get_by_id(id_chuyen))

# @chuyenxe_bp.route("/chuyenxe", methods=["POST"])
# def create_chuyenxe():
#     data = request.json
#     return jsonify(ChuyenXe.create(
#         data["IDTaiXe"], data["IDXe"], data["IDTuyenXe"], data["IDBenKhoiHanh"],
#         data["BenKhoiHanh"], data["IDBenDen"], data["BenDen"], data["NgayXuatPhat"],
#         data["TG_XuatPhat"], data["TG_DuDen"], data["GiaVe"]
#     ))

@chuyenxe_bp.route("/chuyenxe/<id_chuyen>", methods=["PUT"])
def update_chuyenxe(id_chuyen):
    data = request.json

    # Kiểm tra các trường dữ liệu bắt buộc
    required_fields = [
        "IDTaiXe", "IDXe", "IDTuyenXe", "IDBenKhoiHanh", "BenKhoiHanh", 
        "IDBenDen", "BenDen", "TG_XuatPhat", "TG_DuDen", "GiaVe"
    ]
    
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Thiếu trường dữ liệu: {field}"}), 400

    # Dùng get() để lấy giá trị của "NgayXuatPhat", nếu không có thì mặc định là None (null)
    ngay_xuat_phat = data.get("NgayXuatPhat")  # None sẽ được gán nếu không có giá trị

    try:
        return jsonify(ChuyenXe.update(
            id_chuyen, 
            data["IDTaiXe"], 
            data["IDXe"], 
            data["IDTuyenXe"], 
            data["IDBenKhoiHanh"],
            data["BenKhoiHanh"],
            data["IDBenDen"], 
            data["BenDen"],
            ngay_xuat_phat,  # Nếu không có giá trị, nó sẽ là None (null)
            data["TG_XuatPhat"],
            data["TG_DuDen"],
            data["GiaVe"]
        ))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# @chuyenxe_bp.route("/chuyenxe/<string:id_chuyen>", methods=["PUT"])
# def update_chuyenxe(id_chuyen):
#     data = request.json
#     return jsonify(ChuyenXe.update(
#         id_chuyen, data["IDTaiXe"], data["IDXe"], data["IDTuyenXe"], data["IDBenKhoiHanh"],
#         data["BenKhoiHanh"], data["IDBenDen"], data["BenDen"], data["NgayXuatPhat"],
#         data["TG_XuatPhat"], data["TG_DuDen"], data["GiaVe"]
#     ))

# @chuyenxe_bp.route('/tim-chuyen-xe', methods=['GET'])
# def tim_chuyen():
#     TenDiemDi = request.args.get('TenDiemDi')
#     TenDiemDen = request.args.get('TenDiemDen')

#     if not TenDiemDi or not TenDiemDen:
#         return jsonify({"error": "Vui lòng nhập TenDiemDi và TenDiemDen"}), 400

#     chuyen_xe = ChuyenXe.get_by_tinhthanh(TenDiemDi, TenDiemDen)
#     return jsonify(chuyen_xe)
@chuyenxe_bp.route("/chuyenxe", methods=["POST"])
def create_chuyenxe():
    try:
        data = request.get_json()

        id_taixe = data["IDTaiXe"]
        id_xe = data["IDXe"]
        id_tuyenxe = data["IDTuyenXe"]
        id_benkhoihanh = data["IDBenKhoiHanh"]
        benkhoihanh = data["BenKhoiHanh"]
        id_benden = data["IDBenDen"]
        benden = data["BenDen"]
        tg_xuatphat = data["TG_XuatPhat"]
        tg_duden = data["TG_DuDen"]
        gia_ve = int(data["GiaVe"])

        result = ChuyenXe.create_chuyenxe(id_taixe, id_xe, id_tuyenxe,
                                          id_benkhoihanh, benkhoihanh,
                                          id_benden, benden,
                                          tg_xuatphat, tg_duden, gia_ve)

        if "error" in result:
            return jsonify(result), 400
        else:
            return jsonify(result), 201

    except KeyError as e:
        return jsonify({"error": f"Thiếu trường dữ liệu: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@chuyenxe_bp.route("/chuyenxe/<string:id_chuyen>", methods=["DELETE"])
def delete_chuyenxe(id_chuyen):
    return jsonify(ChuyenXe.delete(id_chuyen))


