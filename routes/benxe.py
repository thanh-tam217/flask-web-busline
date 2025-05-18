from flask import Blueprint, request, jsonify
from models.benxe import BenXe

benxe_bp = Blueprint("benxe_bp", __name__)

@benxe_bp.route("/benxe", methods=["GET"])
def get_all_benxe():
    return jsonify(BenXe.get_all())

# @benxe_bp.route("/benxe/<string:id_ben>", methods=["GET"])
# def get_benxe_by_id(id_ben):
#     return jsonify(BenXe.get_by_id(id_ben))

@benxe_bp.route("/benxe/<string:id_ben>", methods=["GET"])
def get_benxe_by_id(id_ben):
    benxe = BenXe.get_by_id(id_ben)
    if benxe:
        return jsonify(benxe)
    else:
        return jsonify({"error": "Bến xe không tồn tại"}), 404

@benxe_bp.route("/benxe/name/<string:ten_ben>", methods=["GET"])
def get_benxe_by_name(ten_ben):
    benxes = BenXe.get_by_name(ten_ben)
    if benxes:
        return jsonify(benxes)
    else:
        return jsonify({"error": "Không tìm thấy bến xe"}), 404

@benxe_bp.route("/benxe/tinh/name/<string:ten_tinh>", methods=["GET"])
def get_benxe_by_ten_tinh(ten_tinh):
    benxes = BenXe.get_by_ten_tinh(ten_tinh)
    if benxes:
        return jsonify(benxes)
    else:
        return jsonify({"error": "Không tìm thấy bến xe thuộc tỉnh này"}), 404

# @benxe_bp.route("/benxe", methods=["POST"])
# def create_benxe():
#     data = request.json
#     return jsonify(BenXe.create(data["TenBen"], data["DiaChi"], data["SDT"], data["IDTinh"]))


# @benxe_bp.route("/benxe", methods=["POST"])
# def create_benxe():
#     data = request.json
#     return jsonify(BenXe.create(data["IDBen"], data["TenBen"], data["DiaChi"], data["SDTBen"], data["IDTinh"]))
@benxe_bp.route("/benxe", methods=["POST"])
def create_benxe():
    try:
        data = request.get_json()
        # id_ben = data["IDBen"]
        ten_ben = data["TenBen"]
        dia_chi = data["DiaChi"]
        sdt = data["SDTBen"]
        id_tinh = data["IDTinh"]

        result = BenXe.create(ten_ben, dia_chi, sdt, id_tinh)

        if "error" in result:
            return jsonify(result), 400
        else:
            return jsonify(result), 201

    except KeyError as e:
        return jsonify({"error": f"Thiếu trường dữ liệu: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# @benxe_bp.route("/benxe/<string:id_ben>", methods=["PUT"])
# def update_benxe(id_ben):
#     data = request.json
#     return jsonify(BenXe.update(id_ben, data["TenBen"], data["DiaChi"], data["SDT"], data["IDTinh"]))
@benxe_bp.route("/benxe/<string:id_ben>", methods=["PUT"])
def update_benxe(id_ben):
    try:
        data = request.get_json()  # Lấy dữ liệu JSON
        if not data:
            return jsonify({"error": "Thiếu dữ liệu JSON"}), 400
        
        # Kiểm tra xem các trường có đầy đủ không
        required_fields = ["TenBen", "DiaChi", "SDTBen", "IDTinh"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Thiếu trường {field}"}), 400
        # Đảm bảo không thay đổi IDBen
        if "IDBen" in data and data["IDBen"] != id_ben:
            return jsonify({"error": "Không thể thay đổi IDBen"}), 400
        # Gọi hàm update
        result = BenXe.update(id_ben, data["TenBen"], data["DiaChi"], data["SDTBen"], data["IDTinh"])
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@benxe_bp.route("/benxe/<string:id_ben>", methods=["DELETE"])
def delete_benxe(id_ben):
    return jsonify(BenXe.delete(id_ben))
