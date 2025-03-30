from flask import Blueprint, request, jsonify
from models.khach import Khach

khach_bp = Blueprint("khach_bp", __name__)

@khach_bp.route("/khach", methods=["GET"])
def get_all_khach():
    return jsonify(Khach.get_all())

@khach_bp.route("/khach/string:id_khach>", methods=["GET"])
def get_khach_by_id(id_khach):
    return jsonify(Khach.get_by_id(id_khach))

