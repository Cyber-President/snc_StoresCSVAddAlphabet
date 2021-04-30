# -*- coding:utf-8 -*-
import pykakasi
import csv
import os, tkinter, tkinter.filedialog, tkinter.messagebox
import re

def main():
    # ファイル選択ダイアログの表示
    root = tkinter.Tk()
    root.withdraw()
    # ファイルタイプを制限　fTyp = [("","*")]
    fTyp = [("","*.csv")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('STORES CSV 購入者氏名アルファベット追加システム','Please Select a File.')
    csv_src = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

    csv_export = csv_src[:-4] + "_export.csv"

    # csv -> list
    with open(csv_src, encoding='cp932') as f:
        reader = csv.reader(f)
        l = [row for row in reader]

    # オブジェクトをインスタンス化
    kakasi = pykakasi.kakasi()
    # モードの設定
    kakasi.setMode('J', 'a')
    kakasi.setMode("H","a")
    kakasi.setMode("K","a")
    kakasi.setMode("r","Hepburn")
    # 変換して出力
    conv = kakasi.getConverter()

    # リスト追加
    for row in l:
        # ローマ字変換
        name_last = conv.do(row[39])
        name_last = re.sub(r"[^a-zA-Z]", "", name_last)
        name_first = conv.do(row[40])
        name_first = re.sub(r"[^a-zA-Z]", "", name_first)
        name_full = name_last + name_first
        row.append(name_last)
        row.append(name_first)
        row.append(name_full)

    # list -> csv
    with open(csv_export, 'w', ) as g:
        writer = csv.writer(g)
        writer.writerows(l)

    # 完了通知
    tkinter.messagebox.showinfo('STORES CSV 購入者氏名アルファベット追加システム', 'Completed!\n' + csv_export)

main()
