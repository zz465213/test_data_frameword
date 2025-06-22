import os

# ==== 路徑 ====
# -- 根目錄 --
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# -- 配置相關 --
CONFIGS_DIR = os.path.join(ROOT_DIR, "configs")
CONFIGS_FILE = os.path.join(CONFIGS_DIR, "configs.yaml")
# -- 主程式相關 --
APP_DIR = os.path.join(ROOT_DIR, "app")
# -- log相關 --
LOG_DIR = os.path.join(APP_DIR, "logs")

# ==== 目錄設定 ====
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(CONFIGS_DIR, exist_ok=True)