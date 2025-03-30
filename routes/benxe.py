from flask import Blueprint, request, jsonify
from models.benxe import BenXe

benxe_bp = Blueprint("benxe_bp", __name__)

@benxe_bp.route("/benxe", methods=["GET"])
def get_all_benxe():
    return jsonify(BenXe.get_all())

@benxe_bp.route("/benxe/<string:id_ben>", methods=["GET"])
def get_benxe_by_id(id_ben):
    return jsonify(BenXe.get_by_id(id_ben))

@benxe_bp.route("/benxe", methods=["POST"])
def create_benxe():
    data = request.json
    return jsonify(BenXe.create(data["TenBen"], data["DiaChi"], data["SDT"], data["IDTinh"]))

@benxe_bp.route("/benxe/<string:id_ben>", methods=["PUT"])
def update_benxe(id_ben):
    data = request.json
    return jsonify(BenXe.update(id_ben, data["TenBen"], data["DiaChi"], data["SDT"], data["IDTinh"]))

@benxe_bp.route("/benxe/<string:id_ben>", methods=["DELETE"])
def delete_benxe(id_ben):
    return jsonify(BenXe.delete(id_ben))
