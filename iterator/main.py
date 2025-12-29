# main.py
from blog import Blog
from blog_comment import BlogComment


def main():
    blog = Blog("Iteratorパターン入門")

    blog.add_comment(BlogComment("Alice", "わかりやすいです"))
    blog.add_comment(BlogComment("Bob", "Pythonいいですね"))
    blog.add_comment(BlogComment("Carol", "Javaとの比較助かる"))

    print(f"タイトル: {blog.title}")
    print("コメント一覧:")

    it = blog.iterator()

    while it.has_next():
        c = it.next()
        print(f"- {c.author}: {c.content}")


if __name__ == "__main__":
    main()
