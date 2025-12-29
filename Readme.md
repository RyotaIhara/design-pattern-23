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

