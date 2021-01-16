# twint
Twitterからツイートをスクレイピングしてくれるtwintというツールの使い方とそのファイルからツイートのみを抽出する方法についてまとめました．

## 1.install 
下のコマンドでインストールする
```
pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
```

## 2.データをスクレイピングする
### CSVファイルの場合
```
# test.csvに出力
$ twint -u username(@は除く) -o test.csv --csv
```
### jsonファイルの場合
```
# test.jsonに出力
$ twint -u username(@は除く) -o test.json --json
```

## 3.落としてきた CSV データからツイート部のみを抽出する
```extraction.py```を編集する．まずはDLしたCSVファイルの指定を行う．

```
# get file path
directry = Path(str(Path.home()) + r"\*****")
csv_list = list(directry.glob("***.csv"))

# specified csv file name
csv_file = open("./*****.csv",'r')
```

次に出力するtxtデータの名前を指定する．

```
a_file = open("./*****.txt", "w")  
```

最後にしたのコマンドを実行する
```
$ python3 extraction.py
```
## 参考資料
