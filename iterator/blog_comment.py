# blog_comment.py
from dataclasses import dataclass


@dataclass
class BlogComment:
    author: str
    content: str
