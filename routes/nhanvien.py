from flask import Blueprint, request, jsonify
from models.nhanvien import NhanVien

nhanvien_bp = Blueprint("nhanvien_bp", __name__)

@nhanvien_bp.route("/nhanvien", methods=["GET"])
def get_all_nhanvien():
    return jsonify(NhanVien.get_all())

@nhanvien_bp.route("/nhanvien/<string:id_nhanvien>", methods=["GET"])
def get_nhanvien_by_id(id_nhanvien):
    return jsonify(NhanVien.get_by_id(id_nhanvien))

@nhanvien_bp.route("/nhanvien", methods=["POST"])
def create_nhanvien():
    data = request.json
    return jsonify(NhanVien.create(data["HoTen"], data["ChucVu"], data["SDT"], data["DiaChi"]))

@nhanvien_bp.route("/nhanvien/<string:id_nhanvien>", methods=["PUT"])
def update_nhanvien(id_nhanvien):
    data = request.json
    return jsonify(NhanVien.update(id_nhanvien, data["HoTen"], data["ChucVu"], data["SDT"], data["DiaChi"]))

@nhanvien_bp.route("/nhanvien/<string:id_nhanvien>", methods=["DELETE"])
def delete_nhanvien(id_nhanvien):
    return jsonify(NhanVien.delete(id_nhanvien))
