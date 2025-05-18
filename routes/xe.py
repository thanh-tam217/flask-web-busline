from flask import Blueprint, request, jsonify
from models.xe import Xe

xe_bp = Blueprint("xe_bp", __name__)

@xe_bp.route("/xe", methods=["GET"])
def get_all_xe():
    return jsonify(Xe.get_all())

@xe_bp.route("/xe/<string:id_xe>", methods=["GET"])
def get_xe_by_id(id_xe):
    return jsonify(Xe.get_by_id(id_xe))

@xe_bp.route("/xe/name/<string:ten_xe>", methods=["GET"])
def get_xe_by_name(ten_xe):
    xe = Xe.get_by_name(ten_xe)
    if xe:
        return jsonify(xe)
    else:
        return jsonify({"error": "Không tìm thấy xe"}), 404
    

@xe_bp.route("/xe", methods=["POST"])
def create_xe():
    try:
        data = request.get_json()
        # id_xe = data["IDXe"]
        bien_so = data["BienSo"]
        loai_xe = data["LoaiXe"]
        so_ghe = data["SoGhe"]
        trang_thai = data["TrangThai"]

        result = Xe.create(bien_so, loai_xe, so_ghe, trang_thai)

        if "error" in result:
            return jsonify(result), 400
        else:
            return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# @xe_bp.route("/xe", methods=["POST"])
# def create_xe():
#     data = request.json
#     return jsonify(Xe.create(data["IDXe"],data["BienSo"], data["LoaiXe"], data["SoGhe"], data["TrangThai"]))

@xe_bp.route("/xe/<string:id_xe>", methods=["PUT"])
def update_xe(id_xe):
    data = request.json
    return jsonify(Xe.update(id_xe, data["BienSo"], data["LoaiXe"], data["SoGhe"], data["TrangThai"]))

@xe_bp.route("/xe/<string:id_xe>", methods=["DELETE"])
def delete_xe(id_xe):
    return jsonify(Xe.delete(id_xe))


# @xe_bp.route("/xe/trangthai/<string:trangthai", methods=["GET"])
# def get_xe_by_trangthai(trangthai):
#     xe = Xe.get_by_trangthai(trangthai)
#     if xe:
#         return jsonify(xe)
#     else:
#         return jsonify({"error": "Không tìm thấy xe"}), 404

@xe_bp.route("/xe/search", methods=["GET"])
def search_xe_by_bien_so():
    keyword = request.args.get("bien_so", "")
    return jsonify(Xe.search_by_bien_so(keyword))

@xe_bp.route("/xe/filter/loai", methods=["GET"])
def filter_xe_by_loai():
    loai = request.args.get("loai_xe")
    if not loai:
        return jsonify({"error": "Thiếu tham số loai_xe"}), 400
    return jsonify(Xe.filter_by_loai_xe(loai))

@xe_bp.route("/xe/filter/trangthai", methods=["GET"])
def filter_xe_by_trang_thai():
    trang_thai = request.args.get("trang_thai")
    if not trang_thai:
        return jsonify({"error": "Thiếu tham số trang_thai"}), 400
    return jsonify(Xe.filter_by_trang_thai(trang_thai))
