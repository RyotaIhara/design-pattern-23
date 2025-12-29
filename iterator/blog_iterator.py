# blog_iterator.py
## iteratorを継承して実装クラスを作成している
from typing import List
from iterator import Iterator
from blog_comment import BlogComment


class BlogIterator(Iterator[BlogComment]):
    """BlogComment のリストを走査する Iterator"""

    def __init__(self, comments: List[BlogComment]):
        self._comments = comments
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._comments)

    def next(self) -> BlogComment:
        if not self.has_next():
            raise StopIteration("これ以上コメントはありません")

        comment = self._comments[self._index]
        self._index += 1
        return comment
