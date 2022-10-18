import pandoc
from pandoc.types import *


if __name__ == '__main__':
    # 単純にフォーマットをmd->txtに変換
    doc = pandoc.read(file='./sample/sample.md', format='markdown')
    pandoc.write(doc, './sample/sample.txt', format='plain')

    for elm in pandoc.iter(doc):
        # こんな感じで型を指定すればトップレベルの箇条書きは取れるはず・・
        if isinstance(elm, OrderedList):
            print(elm)
