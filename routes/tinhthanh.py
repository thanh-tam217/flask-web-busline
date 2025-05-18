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

@tinhthanh_bp.route("/tinhthanh/name/<string:ten_tinh>", methods=["GET"])
def get_tinhthanh_by_name(ten_tinh):
    tinhthanh = TinhThanh.get_by_name(ten_tinh)
    if tinhthanh:
        return jsonify(tinhthanh)
    else:
        return jsonify({"error": "Không tìm thấy tỉnh thành"}), 404


@tinhthanh_bp.route("/tinhthanh", methods=["POST"])
def create_tinhthanh():
    try:
        data = request.get_json()
        ten_tinh = data["TenTinh"]

        return jsonify(TinhThanh.create(ten_tinh)), 201
    except KeyError as e:
        return jsonify({"error": f"Thiếu trường dữ liệu: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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
