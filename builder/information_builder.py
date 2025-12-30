# information_builder.py
from abc import ABC, abstractmethod
from datetime import datetime
from information import Information


class InformationBuilder(ABC):
    """Builder（抽象クラス）"""
    def __init__(self):
        self.information = Information()
    
    @abstractmethod
    # タイトル
    def make_title(self, title: str):
        pass

    @abstractmethod
    # 本文
    def make_body(self, body: str):
        pass

    @abstractmethod
    # 公開開始日
    def make_start_date(self, start_date: datetime):
        pass

    @abstractmethod
    # 公開終了日
    def make_end_date(self, end_date: datetime):
        pass
    
    def build(self) -> Information:
        """構築されたオブジェクトを返す"""
        return self.information
