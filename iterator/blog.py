# blog.py
from typing import List
from blog_comment import BlogComment
from blog_iterator import BlogIterator


class Blog:
    """Blog は BlogComment を保持し、Iterator を生成する"""

    def __init__(self, title: str):
        self.title = title
        self._comments: List[BlogComment] = []

    def add_comment(self, comment: BlogComment):
        self._comments.append(comment)

    def iterator(self) -> BlogIterator:
        """Iterator を生成して返す"""
        return BlogIterator(self._comments)
