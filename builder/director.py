# director.py
from information_builder import InformationBuilder
from datetime import datetime
from information import Information


class InformationDirector:
    """Director（構築プロセスを管理するクラス）"""
    def __init__(self, builder: InformationBuilder):
        self.builder = builder
    
    def construct(self, title: str, body: str, start_date: datetime, end_date: datetime) -> Information:
        """構築プロセスを実行して完成したオブジェクトを返す"""
        self.builder.make_title(title)
        self.builder.make_body(body)
        self.builder.make_start_date(start_date)
        self.builder.make_end_date(end_date)
        return self.builder.build()

