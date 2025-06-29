import traceback
from typing import List
from app.external_data.repositories.demo_repository import DemoRepository
from app.models.member_demo import MemberDemo
from app.exceptions.service_exception import *


class DemoService:
    def __init__(self, demo_repository: DemoRepository):
        self.demo_repository = demo_repository

    def insert_member(self, member_demo: MemberDemo) -> None:
        try:
            self.demo_repository.create_member(member_demo)
        except Exception as e:
            raise ServiceBaseError(message=f"🔴[DEBUG]: {__name__} 發生非預期錯誤訊息: {e}"
                                           f"--- 打印錯誤追溯 ---\n"
                                           f"{traceback.format_exc()}")

    def get_members(self) -> List[MemberDemo]:
        try:
            return self.demo_repository.get_member_all_data()
        except Exception as e:
            raise ServiceBaseError(message=f"🔴[DEBUG]: {__name__} 發生非預期錯誤訊息: {e}"
                                           f"--- 打印錯誤追溯 ---\n"
                                           f"{traceback.format_exc()}")


if __name__ == "__main__":
    pass
