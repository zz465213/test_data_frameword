import csv
import json
import logging
import os
import shutil
import yaml


def cleanup_folder(temp_dir):
    """清理臨時文件和目錄"""
    try:
        shutil.rmtree(temp_dir)
        logging.info(f"🟢 已清理臨時目錄: {temp_dir}")
    except FileNotFoundError as e:
        logging.error(f"🔴 目錄未找到: {temp_dir}，失敗訊息: {e}")
        raise
    except Exception as e:
        logging.error(f"🔴 清理目錄發生非預期錯誤，請檢查目錄: {temp_dir} ，失敗訊息: {e}")
        raise


def rename_file(old_path, new_path):
    """重命名文件"""
    try:
        os.rename(old_path, new_path)
        return new_path
    except FileNotFoundError as e:
        logging.error(f"🔴 找不到文件資料: {old_path}，失敗訊息: {e}")
        raise
    except Exception as e:
        logging.error(f"🔴 文件重命名發生非預期錯誤，請檢查新路徑{new_path}及舊路徑{old_path}，失敗訊息: {e}")
        raise


def read_yaml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            configs = yaml.safe_load(f)
            return configs
    except FileNotFoundError as e:
        logging.error(f"🔴 找不到文件資料: {file_path}，失敗訊息: {e}")
        raise
    except Exception as e:
        logging.error(f"🔴 讀取文件發生非預期錯誤，請檢查文件資料{file_path}，失敗訊息: {e}")
        raise


def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as e:
        logging.error(f"🔴 找不到文件資料: {file_path}，失敗訊息: {e}")
        raise
    except Exception as e:
        logging.error(f"🔴 讀取文件發生非預期錯誤，請檢查文件資料{file_path}，失敗訊息: {e}")
        raise


def read_data_from_csv(file_path, skip_header=True):
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            if skip_header:
                next(reader)
            for row in reader:
                data.append(tuple(row))  # 將每一行轉換為字典
        return data
    except FileNotFoundError as e:
        logging.error(f"🔴 找不到文件資料: {file_path}，失敗訊息: {e}")
        raise
    except Exception as e:
        logging.error(f"🔴 讀取文件發生非預期錯誤，請檢查文件資料{file_path}，失敗訊息: {e}")
        raise


def write_file(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except FileNotFoundError as e:
        logging.error(f"🔴 找不到文件資料: {file_path}，失敗訊息: {e}")
        raise
    except Exception as e:
        logging.error(f"🔴 寫入文件發生非預期錯誤，請檢查文件資料{file_path}，失敗訊息: {e}")
        raise