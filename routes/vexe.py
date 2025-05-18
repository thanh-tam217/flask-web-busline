from flask import Blueprint, request, jsonify
from models.vexe import VeXe

vexe_bp = Blueprint("vexe_bp", __name__)

@vexe_bp.route("/vexe", methods=["GET"])
def get_all_vexe():
    return jsonify(VeXe.get_all())

@vexe_bp.route("/vexe/<string:id_vexe>", methods=["GET"])
def get_vexe_by_id(id_vexe):
    return jsonify(VeXe.get_by_id(id_vexe))

@vexe_bp.route("/vexe/<string:id_vexe>", methods=["DELETE"])
def delete_vexe(id_vexe):
    return jsonify(VeXe.delete(id_vexe))

