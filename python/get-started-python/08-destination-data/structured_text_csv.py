#!/usr/bin/env python3

if __name__ == "__main__":
    #csv
    import csv
    villains = [
        ['Doctor', 'No'],
        ['Rosa', 'Klebb'],
        ['Mister', 'Big'],
        ['Auric', 'Goldfinger'],
        ['Ernst', 'Blofeld'],
    ]

# ファイルにcsvを書き込む(writerows())
with open('villains', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)
    # Doctor,No
    # Rosa,Klebb
    # Mister,Big
    # Auric,Goldfinger
    # Ernst,Blofeld

# ファイルにcsvを書き込む(writerow())
with open('villains2', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerow(villains)
    # "['Doctor', 'No']","['Rosa', 'Klebb']","['Mister', 'Big']","['Auric', 'Goldfinger']","['Ernst', 'Blofeld']"

# 書き込んだ内容を2重リストに戻す
with open('villains', 'rt') as fin:
    cin = csv.reader(fin)
    print('csv.reader(fin)', type(cin))
    villains = [row for row in cin]
    print(villains)
    # リスト内包表記
    # [expression for item in iterable]

# 書き込んだ内容を辞書のリストにする
import pprint
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]

pprint.pprint(villains)

# 辞書のリストをフィールド名付きでファイルに書き込む
with open('villains3', 'wt') as fout:
    cout = csv.DictWriter(fout, fieldnames=['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

# フィールド名付きで書き込まれた辞書にリストを読み込む
with open('villains3', 'rt') as fin:
    cin = csv.DictReader(fin)  # fieldnamesを省略することで最初の1行目をフィールド名として認識する
    villains = [row for row in cin]

pprint.pprint(villains)