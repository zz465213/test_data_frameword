import logging
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.models.member_demo import MemberDemo
from app.services.demo_service import DemoService
from app.swagger.member_definitions import CREATE_MEMBER_SPEC, GET_ALL_MEMBERS_SPEC, MEMBER_REGISTER_SWAGGER_DEFINITIONS


class DemoController:
    def __init__(self, demo_service: DemoService):
        self.bp = Blueprint('demo_api', __name__)
        self.logger = logging.getLogger(__name__)
        self.demo_service = demo_service  # 注入 Service 實例

        # 註冊路由
        self._register_routes()
        self._register_swagger_definitions()

    def _register_routes(self):
        self.bp.route('/members', methods=['POST'])(self.create_member)
        self.bp.route('/members', methods=['GET'])(self.get_all_members)

    def _register_swagger_definitions(self):
        # Flasgger 定義模型，掛載 app_errorhandler 這樣 Flasgger 才能掃描到
        @self.bp.app_errorhandler(404)
        @swag_from(MEMBER_REGISTER_SWAGGER_DEFINITIONS)
        def provide_member_demo_definition(error):  # 該函數僅用於 Flasgger 掃描
            pass

    @swag_from(CREATE_MEMBER_SPEC)
    def create_member(self):
        """
        新增成員資料
        """
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Bad Request", "message": "Request must be JSON"}), 400

            required_fields = ['username', 'email', 'phone', 'age']
            if not all(field in data for field in required_fields):
                return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

            member_demo = MemberDemo(
                username=data['username'],
                email=data['email'],
                phone=data['phone'],
                age=data['age']
            )

            # 呼叫注入的 Service 實例
            self.demo_service.insert_member(member_demo)

            return jsonify({"message": "Member created successfully!"}), 201

        except Exception as e:
            self.logger.error(f"🔴 建立成員 API 發生非預期錯誤: {e}", exc_info=True)
            return jsonify({"error": "Internal Server Error", "message": "Failed to create member."}), 500

    @swag_from(GET_ALL_MEMBERS_SPEC)
    def get_all_members(self):
        """
        獲取所有成員資料
        """
        try:
            # 呼叫注入的 Service 實例
            members = self.demo_service.get_members()
            return jsonify(members), 200

        except Exception as e:
            self.logger.error(f"🔴 獲取所有成員 API 發生非預期錯誤: {e}", exc_info=True)
            return jsonify({"error": "Internal Server Error", "message": "Failed to retrieve members."}), 500
