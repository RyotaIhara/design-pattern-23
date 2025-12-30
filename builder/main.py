from ja_information import JaInformationBuilder
from en_information import EnInformationBuilder
from director import InformationDirector
from datetime import datetime


def main():
    print("=== Directorを使った構築方法 ===")
    # Directorを使う方法
    ja_builder = JaInformationBuilder()
    ja_director = InformationDirector(ja_builder)
    ja_info = ja_director.construct(
        "タイトルテスト",
        "本文テスト",
        datetime(2025, 1, 1),
        datetime(2042, 1, 31)
    )
    print(ja_info)
    print()

    en_builder = EnInformationBuilder()
    en_director = InformationDirector(en_builder)
    en_info = en_director.construct(
        "Title Test",
        "Body Test",
        datetime(2025, 2, 1),
        datetime(2042, 3, 31)
    )
    print(en_info)
    print()

    print("=== Builderを直接使った構築方法 ===")
    # Directorを使わない方法（Builderを直接使用）
    ja_builder2 = JaInformationBuilder()
    ja_builder2.make_title("直接構築タイトル")
    ja_builder2.make_body("直接構築本文")
    ja_builder2.make_start_date(datetime(2025, 1, 1))
    ja_builder2.make_end_date(datetime(2025, 12, 31))
    ja_info2 = ja_builder2.build()
    print(ja_info2)
    print()

    en_builder2 = EnInformationBuilder()
    en_builder2.make_title("Direct Build Title")
    en_builder2.make_body("Direct Build Body")
    en_builder2.make_start_date(datetime(2025, 1, 1))
    en_builder2.make_end_date(datetime(2025, 12, 31))
    en_info2 = en_builder2.build()
    print(en_info2)


if __name__ == "__main__":
    main()