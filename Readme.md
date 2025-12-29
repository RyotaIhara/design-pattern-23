# PythonでGof 23のデザインパターンをまとめたRepository。

## Iteratorフォルダ

```
Iteratorパターンの学習として、`Blog` と `BlogComment` を題材にプログラムを作成した。

まず、要素を順番に走査するためのインターフェースとして、`Iterator` 抽象クラスを定義する。

次に、1対多の関係を持つ `Blog` クラスと `BlogComment` クラスを用意する。

`Iterator` クラスを継承した `BlogIterator` クラスでは、`BlogComment` を走査するためのイテレータ（`Iterator[BlogComment]`）を実装する。

`Blog` クラスでは `iterator()` メソッドを定義し、このメソッドを呼び出すことで `BlogComment` を順番に参照するためのイテレータを生成できるようにしている。

これにより、`Blog` の内部構造を意識せずに、`BlogComment` を順番に処理できる。
```

このプログラムのUML図は、「uml/iterator.md」に作成しています。


## Adaptarフォルダ

```
Adaptarパターンの学習として、プログラムを作成した。

Adaptarパターンには「継承」と「委譲」の２種類があるため、それぞれ「inheritance」と「transfer」フォルダに分けて作成している。

「継承」パターンのプログラムはシンプルに、特定の文字を括弧をつけて表示」したり、アスタをつけて表示したりするプログラムです。

`print`というインターフェースと`banner`というクラスを継承した`print_banner`クラスを作成しています。

`print_banner`のコンストラクターに引数で文字を渡してインスタンを生成して、そのインスタンスから「print_weak」や「print_strong」メソッドを呼ぶことで、上記の処理を実現しています。

委譲のプログラムも使用しているクラス自体は同じですが、print_bannerがBannerを継承せず、コンストラクタでBannerのインスタンスを生成して保持している点が異なります。
```
