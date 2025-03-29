from flask import Flask
from routes.tuyenxe import tuyenxe_bp
from routes.tinhthanh import tinhthanh_bp
from routes.benxe import benxe_bp
from routes.xe import xe_bp
from routes.chuyenxe import chuyenxe_bp

app = Flask(__name__)

# Đăng ký các route
app.register_blueprint(tuyenxe_bp)
app.register_blueprint(tinhthanh_bp)
app.register_blueprint(benxe_bp)
app.register_blueprint(xe_bp)
app.register_blueprint(chuyenxe_bp)

if __name__ == "__main__":
    app.run(debug=True)
