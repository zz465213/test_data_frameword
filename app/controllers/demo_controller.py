from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.models.member_demo import MemberDemo
from app.services.demo_service import DemoService
from app.exceptions.base_app_exception import *
from app.swagger.member_definitions import CREATE_MEMBER_SPEC, GET_ALL_MEMBERS_SPEC, MEMBER_REGISTER_SWAGGER_DEFINITIONS


class DemoController:
    def __init__(self, demo_service: DemoService):
        self.bp = Blueprint('demo_api', __name__)
        self.demo_service = demo_service
        self._register_routes()
        self._register_swagger_definitions()

    def _register_routes(self):
        self.bp.route('/members', methods=['POST'])(self.create_member)
        self.bp.route('/members', methods=['GET'])(self.get_all_members)

    def _register_swagger_definitions(self):
        @self.bp.app_errorhandler(404)
        @swag_from(MEMBER_REGISTER_SWAGGER_DEFINITIONS)
        def provide_member_demo_definition(error):
            pass

    @swag_from(CREATE_MEMBER_SPEC)
    def create_member(self):
        """
        新增成員資料
        """
        data = request.get_json()
        if not data:
            raise BadRequestError(message=f"🔴[DEBUG]: {__name__} Request Body 必須是 JSON 格式")

        required_fields = ['username', 'email', 'phone', 'age']
        if not all(field in data for field in required_fields):
            missing_fields = [field for field in required_fields if field not in data]
            raise BadRequestError(message=f"🔴[DEBUG]: {__name__} Request Body 缺少必填寫欄位{missing_fields}")

        # Model
        member_demo = MemberDemo(
            username=data['username'],
            email=data['email'],
            phone=data['phone'],
            age=data['age']
        )

        self.demo_service.insert_member(member_demo)
        return jsonify(f"🟢 成功建立成員資料: {member_demo}"), 201

    @swag_from(GET_ALL_MEMBERS_SPEC)
    def get_all_members(self):
        """
        獲取所有成員資料
        """
        members = self.demo_service.get_members()
        return jsonify(members), 200
