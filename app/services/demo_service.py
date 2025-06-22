import logging
from typing import List
from app.external_data.repositories.demo_repository import DemoRepository
from app.models.member_demo import MemberDemo
from app.models.account_demo import AccountDemo


class DemoService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.demo_repository = DemoRepository()

    def insert_member_and_account(self, member_demo: MemberDemo,
                                  account_demo: AccountDemo):
        self.demo_repository.create_member(member_demo)
        self.demo_repository.create_account(account_demo)

    def insert_member(self, member_demo: MemberDemo, params) -> List[MemberDemo]:
        self.demo_repository.create_member(member_demo, params)


if __name__ == "__main__":
    member_demo = MemberDemo(
        username='testuser',
        email='test@example.com',
        phone='0987654321',
        age=28
    )
    DemoService().insert_member(member_demo=member_demo,
                                params=(member_demo.username, member_demo.email, member_demo.phone, member_demo.age))
