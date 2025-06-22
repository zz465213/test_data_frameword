import requests
import logging
import requests.cookies


class APIFactory:
    def __init__(self, url):
        self.logger = logging.getLogger(__name__)
        self.session = requests.Session()
        self.url = url

    def _send_request(self, method, **kwargs):
        self.logger.info(f"⚪ 使用 {method.upper()} 方法到網址: {self.url}")
        try:
            response = self.session.request(method, self.url, **kwargs)
            response.raise_for_status()  # 對於狀態 400 ~ 599 拋出 HTTPError
            self.logger.info(f"🟢 成功接收到 {self.url} 的回應 - Statu={response.status_code}")
            return response
        except requests.exceptions.HTTPError as e:
            self.logger.error(f"🔴 {self.url} 錯誤 Statu={e.response.status_code} - 產生 HTTP 錯誤: {e.response.text}")
            raise
        except requests.exceptions.ConnectionError as e:
            self.logger.error(f"🔴 {self.url} 產生連線錯誤: {e}")
            raise
        except requests.exceptions.Timeout as e:
            self.logger.error(f"🔴 {self.url} 產生超時錯誤: {e}")
            raise
        except requests.exceptions.RequestException as e:
            self.logger.error(f"🔴 {self.url} 產生非預期錯誤: {e}")
            raise

    def get(self, params=None, **kwargs):
        return self._send_request("GET", params=params, **kwargs)

    def post(self, **kwargs):
        return self._send_request("POST", **kwargs)

    def put(self, **kwargs):
        return self._send_request("PUT", **kwargs)

    def delete(self, **kwargs):
        return self._send_request("DELETE", **kwargs)

    def get_json(self, params=None, **kwargs):
        return self.get(params=params, **kwargs).json()

    def get_text(self, params=None, **kwargs):
        return self.get(params=params, **kwargs).text

    def get_content(self, params=None, **kwargs):
        return self.get(params=params, **kwargs).content

    def get_raw(self, params=None, **kwargs):
        return self.get(params=params, **kwargs).raw

    def post_text(self, **kwargs):
        return self.post(**kwargs).text

    def post_json(self, **kwargs):
        return self.post(**kwargs).json()
