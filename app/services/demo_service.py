import logging
from typing import List
from app.external_data.repositories.demo_repository import DemoRepository
from app.models.member_demo import MemberDemo


class DemoService:
    def __init__(self, demo_repository: DemoRepository):
        self.logger = logging.getLogger(__name__)
        self.demo_repository = demo_repository

    def insert_member(self, member_demo: MemberDemo) -> None:
        self.demo_repository.create_member(member_demo)

    def get_members(self) -> List[MemberDemo]:
        return self.demo_repository.get_member_all_data()


if __name__ == "__main__":
    pass
