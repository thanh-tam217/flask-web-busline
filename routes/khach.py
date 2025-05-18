from flask import Blueprint, request, jsonify
from models.khach import Khach

khach_bp = Blueprint("khach_bp", __name__)

@khach_bp.route("/khach", methods=["GET"])
def get_all_khach():
    return jsonify(Khach.get_all())

@khach_bp.route("/khach/<string:id_khach>", methods=["GET"])
def get_khach_by_id(id_khach):
    return jsonify(Khach.get_by_id(id_khach))


@khach_bp.route("/khach/name/<string:ten_khach>", methods=["GET"])
def get_khach_by_name(ten_khach):
    khach = Khach.get_by_name(ten_khach)
    if khach:
        return jsonify(khach)
    else:
        return jsonify({"error": "Không tìm thấy khách hàng"}), 404

@khach_bp.route("/khach/gioitinh/<string:gioitinh>", methods=["GET"])
def get_khach_by_gioitinh(gioitinh):
    khach = Khach.get_by_gioitinh(gioitinh)
    if khach:
        return jsonify(khach)
    else:
        return jsonify({"error": "Không tìm thấy khách hàng"}), 404

# @khach_bp.route("/khach/name/<string:ten_khach>", methods=["GET"])
# def get_khach_by_name(ten_khach):
#     khach = Khach.get_by_name(ten_khach)
#     if khach:
#         return jsonify(khach)
#     else:
#         return jsonify({"error": "Không tìm thấy khách hàng"}), 404

# @khach_bp.route("/khach/gioitinh/<string:gioitinh>", methods=["GET"])
# def get_khach_by_gioitinh(gioitinh):
#     khach = Khach.get_by_gioitinh(gioitinh)
#     if khach:
#         return jsonify(khach)
#     else:
#         return jsonify({"error": "Không tìm thấy khách hàng"}), 404