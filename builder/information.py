# information.py
from datetime import datetime


class Information:
    """構築される最終的なオブジェクト（Product）"""
    def __init__(self):
        self.title = None
        self.body = None
        self.start_date = None
        self.end_date = None
    
    def __str__(self):
        parts = []
        if self.title:
            parts.append(self.title)
        if self.body:
            parts.append(self.body)
        if self.start_date:
            parts.append(self.start_date)
        if self.end_date:
            parts.append(self.end_date)
        return "\n".join(parts)

