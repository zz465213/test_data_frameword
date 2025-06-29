from app.controllers.demo_controller import DemoController
from app.external_data.repositories.demo_repository import DemoRepository
from app.exceptions.custom_exception import CustomException
from app.exceptions.database_exception import *
from app.services.demo_service import DemoService
from flask import Flask, jsonify
from flasgger import Swagger
from flask_cors import CORS
from pydantic import ValidationError
from app.utils.log_tool import configure_logging


def create_app():
    # Flask建置
    app = Flask(__name__)
    CORS(app)

    # Swagger 配置
    app.config['SWAGGER'] = {
        'title': 'Demo API',
        'uiversion': 3,
        'swagger_ui_bundle_path': '/swagger/',
        'description': 'Demo API for Member Management',
        'version': '1.0.0',
        'termsOfService': '',
        'contact': {
            'name': 'API Support',
            'email': 'support@example.com'
        }
    }
    Swagger(app)

    # 依賴注入
    demo_repository = DemoRepository()
    demo_service = DemoService(demo_repository)
    demo_controller = DemoController(demo_service)
    app.register_blueprint(demo_controller.bp, url_prefix='/api')  # 註冊 demo_controller 內部的藍圖

    @app.route('/')
    def index():
        app.logger.info("⚪ 接收到首頁請求")
        return jsonify({"message": "Welcome to Demo API! Access Swagger UI at \'/apidocs\'"})

    # --- 全局異常處理器 ---
    @app.errorhandler(ValidationError)
    def handle_pydantic_validation_error(e):
        app.logger.error(e)
        return jsonify({"error_code": 40000, "message": "請求資料格式錯誤", "details": e.errors()}), 400

    @app.errorhandler(CustomException)
    def handle_custom_model_exception(e):
        app.logger.error(e)
        return jsonify({
            "error_code": e.error_code.value,
            "message": e.message,
            "details": e.details
        }), e.status_code

    @app.errorhandler(DatabaseException)
    def handle_database_exception(e):
        app.logger.error(e)
        return jsonify({
            "error_code": e.error_code.value,
            "message": e.message
        }), e.status_code

    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        app.logger.error(e)
        return jsonify({
            "error_code": 50001,
            "message": "發生了未預期的伺服器錯誤。"
        }), 500

    return app


if __name__ == '__main__':
    app = create_app()
    configure_logging(app)
    app.run(debug=False, host='0.0.0.0', port=5000)
