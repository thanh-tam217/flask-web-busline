from flask import Blueprint, request, jsonify
from models.nhanvien import NhanVien

nhanvien_bp = Blueprint("nhanvien_bp", __name__)

@nhanvien_bp.route("/nhanvien", methods=["GET"])
def get_all_nhanvien():
    return jsonify(NhanVien.get_all())

@nhanvien_bp.route("/nhanvien/<string:id_nhanvien>", methods=["GET"])
def get_nhanvien_by_id(id_nhanvien):
    return jsonify(NhanVien.get_by_id(id_nhanvien))

@nhanvien_bp.route("/nhanvien/name/<string:ten_nhanvien>", methods=["GET"])
def get_nhanvien_by_name(ten_nhanvien):
    nhanvien = NhanVien.get_by_name(ten_nhanvien)
    if nhanvien:
        return jsonify(nhanvien)
    else:
        return jsonify({"error": "Không tìm thấy nhân viên"}), 404

@nhanvien_bp.route("/nhanvien", methods=["POST"])
def create_nhanvien():
    data = request.json
    return jsonify(NhanVien.create(data["IDNhanVien"], data["HoTen"], data["SDT"], data["DiaChi"], data["GioiTinh"], data["CCCD"], data["ChucVu"]))

@nhanvien_bp.route("/nhanvien/<string:id_nhanvien>", methods=["PUT"])
def update_nhanvien(id_nhanvien):
    data = request.json
    return jsonify(NhanVien.update(id_nhanvien, data["HoTen"], data["SDT"], data["DiaChi"], data["GioiTinh"], data["CCCD"], data["ChucVu"]))

@nhanvien_bp.route("/nhanvien/<string:id_nhanvien>", methods=["DELETE"])
def delete_nhanvien(id_nhanvien):
    return jsonify(NhanVien.delete(id_nhanvien))
