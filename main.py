import pandoc
from pandoc.types import *


if __name__ == '__main__':
    # 単純にフォーマットをmd->txtに変換
    doc = pandoc.read(file='./sample/sample.md', format='markdown')
    pandoc.write(doc, './sample/sample.txt', format='plain')

    contents = doc[1]

    for elm in contents:
        # こんな感じで型を指定すればトップレベルの箇条書きは取れるはず・・
        # OrderListの構文は OrderedList(ListAttributes, [[Block]])
        # elm[1]で[[Block]](箇条書きとか本文のところ)を取得
        index = 1
        for block in elm[1]:
            # OrderListの構造的にトップレベルの箇条書きタイトルは↓でアクセスできそう
            # 箇条書きの番号は消える・・・レンダリングの時に付与してるのかな
            print(f'{index}.{block[0][0][0][0]}')
            index += 1
