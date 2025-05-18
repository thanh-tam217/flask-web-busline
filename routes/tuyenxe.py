from flask import Blueprint, jsonify, request
from models.tuyenxe import TuyenXe

tuyenxe_bp = Blueprint('tuyenxe', __name__)

# Lấy danh sách tất cả tuyến xe
@tuyenxe_bp.route('/tuyenxe', methods=['GET'])
def get_all_tuyenxe():
    data = TuyenXe.get_all()
    return jsonify(data)

# Lấy thông tin tuyến xe theo ID
@tuyenxe_bp.route('/tuyenxe/<string:id_tuyenxe>', methods=['GET'])
def get_tuyenxe_by_id(id_tuyenxe):
    data = TuyenXe.get_by_id(id_tuyenxe)
    if data:
        return jsonify(data)
    return jsonify({"error": "Tuyến xe không tồn tại"}), 404

# Thêm tuyến xe mới
@tuyenxe_bp.route('/tuyenxe', methods=['POST'])
def create_tuyenxe():
    try:
        data = request.get_json()
        result = TuyenXe.create(data)
        return jsonify({"message": "Thêm tuyến xe thành công!"}), 201
    except KeyError as e:
        return jsonify({"error": f"Thiếu trường dữ liệu: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Cập nhật tuyến xe
@tuyenxe_bp.route('/tuyenxe/<string:id_tuyenxe>', methods=['PUT'])
def update_tuyenxe(id_tuyenxe):
    data = request.json
    TuyenXe.update(id_tuyenxe, data)
    return jsonify({"message": "Cập nhật tuyến xe thành công!"})

# Xóa tuyến xe
@tuyenxe_bp.route('/tuyenxe/<string:id_tuyenxe>', methods=['DELETE'])
def delete_tuyenxe(id_tuyenxe):
    TuyenXe.delete(id_tuyenxe)
    return jsonify({"message": "Xóa tuyến xe thành công!"})
