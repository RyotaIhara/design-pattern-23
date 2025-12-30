# ja_information.py
from information_builder import InformationBuilder
from datetime import datetime


class JaInformationBuilder(InformationBuilder):
    """日本語情報を構築するConcreteBuilder"""
    def make_title(self, title: str):
        self.information.title = "タイトル：" + title

    def make_body(self, body: str):
        self.information.body = "本文：" + body

    def make_start_date(self, start_date: datetime):
        self.information.start_date = "公開開始日：" + start_date.strftime("%Y-%m-%d")

    def make_end_date(self, end_date: datetime):
        self.information.end_date = "公開終了日：" + end_date.strftime("%Y-%m-%d")
