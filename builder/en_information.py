# en_information.py
from information_builder import InformationBuilder
from datetime import datetime


class EnInformationBuilder(InformationBuilder):
    """英語情報を構築するConcreteBuilder"""
    def make_title(self, title: str):
        self.information.title = "Title: " + title

    def make_body(self, body: str):
        self.information.body = "Body: " + body

    def make_start_date(self, start_date: datetime):
        self.information.start_date = "Start Date: " + start_date.strftime("%Y-%m-%d")

    def make_end_date(self, end_date: datetime):
        self.information.end_date = "End Date: " + end_date.strftime("%Y-%m-%d")

