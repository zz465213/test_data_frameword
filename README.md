# 測試資料建置框架
## 1. 如何執行
- 起測試資料微服務: `python run.py`

## 2. 架構圖:
```
your_test_data_framework/
├── app/
│   ├── __init__.py
│   ├── adapters/                     # 抽象化並管理所有外部通訊的細節 (資料庫 & API)
│   │   ├── __init__.py
│   │   ├── db_factory.py             # 統一管理資料庫
│   │   ├── api_factory.py            # 統一管理api
│   │   └── db_adapters/              # 資料庫適配器子資料夾
│   │       ├── __init__.py
│   │       ├── idatabase_adapter.py  # 資料庫介面
│   │       └── **_adapter.py         # Oracle, DB2, postgreSQL... 等資料庫方法
│   ├── controllers/                  # 處理 HTTP 請求，調用 Service
│   │   ├── __init__.py
│   │   └── **_controller.py
│   ├── external_data/                # 外部資料整合層
│   │   ├── integrations/             # 外部 API 整合層 (特殊 Repository)
│   │   │   ├── __init__.py
│   │   │   └── **_api.py
│   │   ├── repositories/             # 資料庫操作的抽象層，透過 DB Adapters 互動
│   │   │   ├── __init__.py
│   │   └── └── **_repository.py
│   ├── logs/                         # 日誌目錄
│   ├── models/                       # 資料結構定義 (ORM models 或 dataclasses)
│   │   ├── __init__.py
│   │   └── **_model.py   
│   ├── services/                     # 核心業務邏輯，協調 Repository 和外部 API
│   │   ├── __init__.py
│   │   └── **_service.py
│   ├── utils/                        # 共用類
│   │   ├── __init__.py
│   └── └── **_tool.py                # 小工具
├── configs/                          # 設置文件目錄
│   ├── __init__.py
│   ├── common_paths.py               # 共用路徑
│   ├── config.yaml                   # 設定檔 (例如: 資料庫連線字串, API key)
│   └── global_adapter.py             # 全域變數設定                 
├── tests/                            # 測試目錄
├── requirements.txt                  # 專案依賴套件
└── run.py                            # 啟動 Flask 應用程式的入口點 
```