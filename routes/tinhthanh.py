from flask import Blueprint, jsonify, request
from models.tinhthanh import TinhThanh

tinhthanh_bp = Blueprint('tinhthanh', __name__)

# Lấy danh sách tất cả tỉnh thành
@tinhthanh_bp.route('/tinhthanh', methods=['GET'])
def get_all_tinhthanh():
    data = TinhThanh.get_all()
    return jsonify(data)

# Lấy thông tin tỉnh thành theo ID
@tinhthanh_bp.route('/tinhthanh/<string:id_tinh>', methods=['GET'])
def get_tinhthanh_by_id(id_tinh):
    data = TinhThanh.get_by_id(id_tinh)
    if data:
        return jsonify(data)
    return jsonify({"error": "Tỉnh thành không tồn tại"}), 404

# Thêm tỉnh thành mới
# @tinhthanh_bp.route('/tinhthanh', methods=['POST'])
# def create_tinhthanh():
#     data = request.json
#     TinhThanh.create(data['TenTinh'])
#     return jsonify({"message": "Thêm tỉnh thành thành công!"}), 201
@tinhthanh_bp.route('/tinhthanh', methods=['POST'])
def create_tinhthanh():
    # Kiểm tra xem request có phải JSON không
    if not request.is_json:
        return jsonify({"error": "Content-Type phải là application/json"}), 415

    data = request.get_json()

    # Kiểm tra có đủ dữ liệu không
    if 'ten_tinh' not in data:
        return jsonify({"error": "Thiếu tham số ten_tinh"}), 400

    result = TinhThanh.create(data['ten_tinh'])
    return jsonify(result), 201

# Cập nhật tỉnh thành
@tinhthanh_bp.route('/tinhthanh/<string:id_tinh>', methods=['PUT'])
def update_tinhthanh(id_tinh):
    data = request.json
    TinhThanh.update(id_tinh, data['TenTinh'])
    return jsonify({"message": "Cập nhật tỉnh thành thành công!"})

# Xóa tỉnh thành
@tinhthanh_bp.route('/tinhthanh/<string:id_tinh>', methods=['DELETE'])
def delete_tinhthanh(id_tinh):
    TinhThanh.delete(id_tinh)
    return jsonify({"message": "Xóa tỉnh thành thành công!"})
