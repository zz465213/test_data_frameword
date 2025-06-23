import logging
from app.controllers.demo_controller import DemoController
from app.external_data.repositories.demo_repository import DemoRepository
from app.services.demo_service import DemoService
from app.utils.file_tool import read_yaml
from configs.common_paths import CONFIGS_FILE
from flask import Flask, jsonify
from flasgger import Swagger
from flask_cors import CORS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


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

    # 初始化swagger
    Swagger(app)

    # 統一配置
    config = read_yaml(CONFIGS_FILE)
    mysql_config = config["mysql"]

    # 依賴注入
    demo_repository = DemoRepository(mysql_config)
    demo_service = DemoService(demo_repository)
    demo_controller = DemoController(demo_service)
    app.register_blueprint(demo_controller.bp, url_prefix='/api')  # 註冊 Controller 內部的藍圖

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to Demo API! Access Swagger UI at /apidocs"})

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad Request", "message": str(error)}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not Found", "message": "The requested URL was not found on the server."}), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        logging.error(f"An unhandled error occurred: {error}")
        return jsonify({"error": "Internal Server Error", "message": "Something went wrong on the server."}), 500

    return app


if __name__ == '__main__':
    # TODO: Model 限制條件確認
    # TODO: 思考是否run.py的DI注入需要保留
    # TODO: Logs 撰寫邏輯
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
