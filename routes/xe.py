from flask import Blueprint, request, jsonify
from models.xe import Xe

xe_bp = Blueprint("xe_bp", __name__)

@xe_bp.route("/xe", methods=["GET"])
def get_all_xe():
    return jsonify(Xe.get_all())

@xe_bp.route("/xe/<int:id_xe>", methods=["GET"])
def get_xe_by_id(id_xe):
    return jsonify(Xe.get_by_id(id_xe))

@xe_bp.route("/xe", methods=["POST"])
def create_xe():
    data = request.json
    return jsonify(Xe.create(data["BienSo"], data["LoaiXe"], data["SoGhe"], data["TrangThai"]))

@xe_bp.route("/xe/<int:id_xe>", methods=["PUT"])
def update_xe(id_xe):
    data = request.json
    return jsonify(Xe.update(id_xe, data["BienSo"], data["LoaiXe"], data["SoGhe"], data["TrangThai"]))

@xe_bp.route("/xe/<int:id_xe>", methods=["DELETE"])
def delete_xe(id_xe):
    return jsonify(Xe.delete(id_xe))
