# 模型定義
MEMBER_DEMO_DEFINITION = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string', 'description': '使用者名稱', 'example': 'john_doe'},
        'email': {'type': 'string', 'format': 'email', 'description': 'Email 地址', 'example': 'john.doe@example.com'},
        'phone': {'type': 'string', 'description': '電話號碼', 'example': '0912345678'},
        'age': {'type': 'integer', 'minimum': 1, 'maximum': 150, 'description': '年齡', 'example': 30}
    }
}

MEMBER_INPUT_DEFINITION = {
    'type': 'object',
    'required': ['username', 'email', 'phone', 'age'],
    'properties': {
        'username': {'type': 'string', 'minLength': 3, 'maxLength': 50, 'description': '使用者名稱',
                     'example': 'john_doe'},
        'email': {'type': 'string', 'format': 'email', 'description': 'Email 地址', 'example': 'john.doe@example.com'},
        'phone': {'type': 'string', 'pattern': '^09\\d{8}$', 'description': '台灣手機號碼', 'example': '0912345678'},
        'age': {'type': 'integer', 'minimum': 1, 'maximum': 150, 'description': '年齡', 'example': 30}
    }
}

MEMBER_REGISTER_SWAGGER_DEFINITIONS = {
    'definitions': {
        'MemberDemo': {
            'type': 'object',
            'properties': {
                'username': {'type': 'string', 'description': '使用者名稱', 'example': 'john_doe'},
                'email': {'type': 'string', 'format': 'email', 'description': 'Email 地址',
                          'example': 'john.doe@example.com'},
                'phone': {'type': 'string', 'description': '電話號碼', 'example': '0912345678'},
                'age': {'type': 'integer', 'format': 'int32', 'description': '年齡', 'example': 30}
            }
        }
    }
}

# 回應定義
SUCCESS_RESPONSE = {
    'type': 'object',
    'properties': {
        'message': {'type': 'string', 'example': 'Operation completed successfully'}
    }
}

ERROR_RESPONSE = {
    'type': 'object',
    'properties': {
        'error': {'type': 'string', 'example': 'Bad Request'},
        'message': {'type': 'string', 'example': 'Invalid input data'}
    }
}

# API 路由定義
CREATE_MEMBER_SPEC = {
    'tags': ['Member Management'],
    'summary': '新增成員資料',
    'description': '根據提供的成員資訊，創建一個新的成員記錄',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': MEMBER_INPUT_DEFINITION
        }
    ],
    'responses': {
        201: {'description': '成員資料創建成功', 'schema': SUCCESS_RESPONSE},
        400: {'description': '請求參數錯誤', 'schema': ERROR_RESPONSE},
        500: {'description': '內部伺服器錯誤', 'schema': ERROR_RESPONSE}
    }
}

GET_ALL_MEMBERS_SPEC = {
    'tags': ['Member Management'],
    'summary': '獲取所有成員資料',
    'description': '獲取資料庫中所有成員的詳細資訊',
    'responses': {
        200: {
            'description': '成功獲取成員列表',
            'schema': {
                'type': 'array',
                'items': MEMBER_DEMO_DEFINITION
            }
        },
        500: {'description': '內部伺服器錯誤', 'schema': ERROR_RESPONSE}
    }
}
