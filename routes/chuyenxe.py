from flask import Blueprint, request, jsonify
from models.chuyenxe import ChuyenXe


chuyenxe_bp = Blueprint("chuyenxe_bp", __name__)

@chuyenxe_bp.route("/chuyenxe", methods=["GET"])
def get_all_chuyenxe():
    return jsonify(ChuyenXe.get_all())

@chuyenxe_bp.route("/chuyenxe/<string:id_chuyen>", methods=["GET"])
def get_chuyenxe_by_id(id_chuyen):
    return jsonify(ChuyenXe.get_by_id(id_chuyen))

@chuyenxe_bp.route("/chuyenxe", methods=["POST"])
def create_chuyenxe():
    data = request.json
    return jsonify(ChuyenXe.create(
        data["IDTaiXe"], data["IDXe"], data["IDTuyenXe"], data["IDBenKhoiHanh"],
        data["BenKhoiHanh"], data["IDBenDen"], data["BenDen"], data["NgayXuatPhat"],
        data["TG_XuatPhat"], data["TG_DuDen"], data["GiaVe"]
    ))

@chuyenxe_bp.route("/chuyenxe/string:id_chuyen>", methods=["PUT"])
def update_chuyenxe(id_chuyen):
    data = request.json
    return jsonify(ChuyenXe.update(
        id_chuyen, data["IDTaiXe"], data["IDXe"], data["IDTuyenXe"], data["IDBenKhoiHanh"],
        data["BenKhoiHanh"], data["IDBenDen"], data["BenDen"], data["NgayXuatPhat"],
        data["TG_XuatPhat"], data["TG_DuDen"], data["GiaVe"]
    ))

# @chuyenxe_bp.route('/tim-chuyen-xe', methods=['GET'])
# def tim_chuyen():
#     TenDiemDi = request.args.get('TenDiemDi')
#     TenDiemDen = request.args.get('TenDiemDen')

#     if not TenDiemDi or not TenDiemDen:
#         return jsonify({"error": "Vui lòng nhập TenDiemDi và TenDiemDen"}), 400

#     chuyen_xe = ChuyenXe.get_by_tinhthanh(TenDiemDi, TenDiemDen)
#     return jsonify(chuyen_xe)



@chuyenxe_bp.route("/chuyenxe/<string:id_chuyen>", methods=["DELETE"])
def delete_chuyenxe(id_chuyen):
    return jsonify(ChuyenXe.delete(id_chuyen))
